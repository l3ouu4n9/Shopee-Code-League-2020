import fasttext

# Train the model
model = fasttext.train_supervised('/home/lai/shopee/challenge_6/leo/fasttext/fasttext_train.txt', lr=0.001, dim=300, epoch=800, wordNgrams=2)
# Evaluate the model
model.test('/home/lai/shopee/challenge_6/leo/fasttext/fasttext_val.txt')

model.save_model('model_lr0001_dim300_epoch800_wordNgrams2.bin')
