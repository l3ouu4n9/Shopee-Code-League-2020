from data_args import *
import math
import csv
import random
import numpy as np
import keras
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.applications.resnet50 import preprocess_input

img_generator = ImageDataGenerator(shear_range=0.5, 
                                   rotation_range=50, 
                                   zoom_range=0.2, 
                                   width_shift_range=0.2, 
                                   height_shift_range=0.2, 
                                   fill_mode='reflect')

class DataGenerator(keras.utils.Sequence):
    def __init__(self, datas, shuffle=True):
        self.batch_size = args.bs
        self.class_num = args.class_num
        self.datas = datas
        self.indexes = np.arange(len(self.datas))
        self.shuffle = shuffle

    def __len__(self):
        return math.ceil(len(self.datas) / float(self.batch_size))

    def __getitem__(self, index):
        # generate batch
        batch_indexs = self.indexes[index*self.batch_size:(index+1)*self.batch_size]
        batch_datas = [self.datas[k] for k in batch_indexs]
        x, y = self.data_generation(batch_datas)
        return x, y

    def on_epoch_end(self):
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def data_generation(self, batch_datas):
        datas = []
        labels = []
        # generate data
        for data in batch_datas:
            x=data['data']
            y=data['label']
            img = load_img(x, target_size=(args.width, args.height))
            img = img_to_array(img)
            img = preprocess_input(img)
            img = np.expand_dims(img, axis=0)
            gen_img = img_generator.flow(img, batch_size=1)
            gen_img = next(gen_img)
            datas.append(gen_img[0])
            labels.append(y)
        return np.array(datas), np.array(labels)

# read data
def read_data(filename=args.data_path):
    data = []
    train_datas = []
    validation_datas=[]
    validation_ratio = 0.1
    with open(filename) as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            data.append(row)
    
    # data shuffle
    data = data[1:]
    random.shuffle(data)
    
    pivot =  int((1 - validation_ratio) * len(data))
    print(pivot)
    for x, y in data[0 : pivot]:
        _data='{}/{}/{}'.format(args.pic_path, y,x)
        _label=np.zeros((args.class_num))
        _label[int(y)]=1
        data_dict={'data':_data, 'label':_label}
        train_datas.append(data_dict)
    for x, y in data[pivot :]:
        _data='{}/{}/{}'.format(args.pic_path, y,x)
        _label=np.zeros((args.class_num))
        _label[int(y)]=1
        data_dict={'data':_data, 'label':_label}
        validation_datas.append(data_dict)
    
    return train_datas, validation_datas
