import os
import numpy as np
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras.models import load_model
from keras.utils import multi_gpu_model
from data_args import *
from data_load import *
from model import *
from keras.models import load_model

os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,3"
train_data, validation_data = read_data()


training_generator = DataGenerator(train_data)
validation_generator = DataGenerator(validation_data)


model = resnet_model()
#model = load_model(args.save_path)
#model = AttentionResNet56()
checkpoint = ModelCheckpoint(args.save_path, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

parallel_model = multi_gpu_model(model, gpus=3)
parallel_model.compile(optimizer=Adam(lr=args.lr), 
                       loss='categorical_crossentropy',
                       metrics=['accuracy'])

parallel_model.fit_generator(training_generator, epochs=args.epoch, workers=args.workers, verbose=1, validation_data=validation_generator, callbacks=callbacks_list)
