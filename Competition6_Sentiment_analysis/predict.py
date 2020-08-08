import fasttext
import pandas as pd
from sacremoses import MosesTokenizer
import re

def clean(series):
    series = series.str.lower()
    series = series.str.replace(r'’', '\'')
    series = series.str.replace(r'#[a-z]+', ' ')
    series = series.str.replace(r'@[a-z]+', ' ')
    series = series.str.replace(r'[\+\*=@#<>\(\)\[\]\^_]+', ' ')
    series = series.apply(mtk.tokenize)
    return series

def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"
                           u"\U0001F300-\U0001F5FF"
                           u"\U0001F680-\U0001F6FF"
                           u"\U0001F1E0-\U0001F1FF"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', str(text))

mtk = MosesTokenizer()

test = pd.read_csv('/home/lai/shopee/challenge_6/dataset/test.csv', index_col='review_id')
test['review_clean'] = remove_emoji(test['review'])
test['review_clean'] = clean(test['review'])
test['review_clean'] = test['review_clean'].str.join(' ')

model = fasttext.load_model('model_lr0001_dim300_epoch800_wordNgrams2.bin')

test['label'] = test['review_clean'].apply(model.predict)
test['rating'] = test['label'].apply(lambda x: x[0][0][-1])
test['rating'].to_csv('submission.csv')
