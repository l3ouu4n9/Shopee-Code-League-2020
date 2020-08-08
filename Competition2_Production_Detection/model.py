from keras.applications.resnet50 import ResNet50
from keras.models import Model
from keras.layers import Flatten, Dense, Dropout
from keras.regularizers import l2
from data_args import *

def resnet_model(img_shape=(args.width, args.height, 3), n_classes=args.class_num, l2_reg=0.01,
                load_pretrained=True, freeze_layers_from='base_model'):
    # Decide if load pretrained weights from imagenet
    if load_pretrained:
        weights = 'imagenet'
    else:
        weights = None

    # Get base model
    base_model = ResNet50(include_top=False, weights=weights,
                       input_tensor=None, input_shape=img_shape)
    # Add final layers
    x = base_model.output
    x = Flatten()(x)
    #predictions = Dense(n_classes, activation='softmax', name='output')(x)
    x = Dropout(0.1)(x)
    regularizer = l2(l2_reg)
    predictions = Dense(n_classes, kernel_regularizer=regularizer, activation='softmax')(x)
    # This is the model we will train
    model = Model(base_model.input, predictions)

    # Freeze some layers
    if freeze_layers_from is not None:
        if freeze_layers_from == 'base_model':
            print ('   Freezing base model layers')
            for layer in base_model.layers:
                layer.trainable = False
        else:
            for i, layer in enumerate(model.layers):
                print(i, layer.name)
            print ('   Freezing from layer 0 to ' + str(freeze_layers_from))
            for layer in model.layers[:freeze_layers_from]:
               layer.trainable = False
            for layer in model.layers[freeze_layers_from:]:
               layer.trainable = True

    return model 

def AttentionResNet56(shape=(args.width, args.height, 3), n_channels=64, n_classes=args.class_num,
                      dropout=0, regularization=0.01):
    """
    Attention-56 ResNet
    https://arxiv.org/abs/1704.06904
    """

    regularizer = l2(regularization)

    input_ = Input(shape=shape)
    x = Conv2D(n_channels, (7, 7), strides=(2, 2), padding='same')(input_) # 112x112
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = MaxPool2D(pool_size=(3, 3), strides=(2, 2), padding='same')(x)  # 56x56

    x = residual_block(x, output_channels=n_channels * 4)  # 56x56
    x = attention_block(x, encoder_depth=3)  # bottleneck 7x7

    x = residual_block(x, output_channels=n_channels * 8, stride=2)  # 28x28
    x = attention_block(x, encoder_depth=2)  # bottleneck 7x7

    x = residual_block(x, output_channels=n_channels * 16, stride=2)  # 14x14
    x = attention_block(x, encoder_depth=1)  # bottleneck 7x7

    x = residual_block(x, output_channels=n_channels * 32, stride=2)  # 7x7
    x = residual_block(x, output_channels=n_channels * 32)
    x = residual_block(x, output_channels=n_channels * 32)

    pool_size = (x.get_shape()[1].value, x.get_shape()[2].value)
    x = AveragePooling2D(pool_size=pool_size, strides=(1, 1))(x)
    x = Flatten()(x)
    if dropout:
        x = Dropout(dropout)(x)
    output = Dense(n_classes, kernel_regularizer=regularizer, activation='softmax')(x)

    model = Model(input_, output)
    return model