from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-lr", help="leraning rate", default=1e-5)
parser.add_argument("-bs", help="Batch_Size", default=100)
parser.add_argument("-height", help="height of pic", default=640)
parser.add_argument("-width", help="width of pic", default=640)
parser.add_argument("-class_num", help="Length of class", default=42)
parser.add_argument("-epoch", help="epoch", default=50)
parser.add_argument("-workers", help="workers", default=30)
parser.add_argument("-data_path", help="The path of training data", default='/home/lai/shopee/dataset/train.csv')
parser.add_argument("-pic_path", help="The path of pic data", default='/home/lai/shopee/dataset/train/train')
parser.add_argument("-save_path", help="The path of save model", default='/home/lai/shopee/classify.h5')
args = parser.parse_args()