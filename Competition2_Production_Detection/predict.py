import numpy as np
import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import os
import csv
from os import listdir
from os.path import isfile, join

model_path = '/home/lai/shopee/leo/trained_model/classify.h5'
test_path = '/home/lai/shopee/dataset/test/test/'


#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["CUDA_VISIBLE_DEVICES"] = "1"


# load model
model = load_model(model_path)

# summarize model.
# model.summary()

# input csv
input_file = open('/home/lai/shopee/dataset/test.csv', 'r')
rows = csv.reader(input_file)
next(rows)

# output csv
output_file = open('/home/lai/shopee/leo/predict/ans.csv', 'w')
writer = csv.writer(output_file)
writer.writerow(['filename', 'category'])

i = 0
for row in rows:
    img_path = test_path + row[0]
    # print('Img Path: ', img_path)
    img = image.load_img(img_path, target_size=(640, 640))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)


    # model predict
    preds = model.predict(x)
    preds2 = np.argmax(model.predict(x))
    preds2 = "{:0>2d}".format(preds2)
    # print('Predicted: ', preds2)
    writer.writerow([row[0], preds2])
    i += 1
    if i % 2000 == 0:
        print(i)
    
    
input_file.close()
output_file.close()