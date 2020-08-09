import pandas as pd
import numpy as np
import re

from sklearn.metrics import matthews_corrcoef
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBRFClassifier


data_path = '/home/lai/shopee/challenge_8/dataset/'

def add_datepart(df, fldname, drop=True):
    fld = df[fldname]
    if not np.issubdtype(fld.dtype, np.datetime64):
        df[fldname] = fld = pd.to_datetime(fld, infer_datetime_format=True)
    targ_pre = re.sub('[Dd]ate$', '', fldname)
    for n in ('Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear',
            'Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start', 'Is_year_end', 'Is_year_start'):
        df[targ_pre+n] = getattr(fld.dt,n.lower())
    if drop: df.drop(fldname, axis=1, inplace=True)

def remove_datecols(df):
    fld = ['grass_Year','grass_Is_quarter_end','grass_Is_quarter_start','grass_Is_year_start','grass_Is_year_end']
    df.drop(fld, axis=1, inplace=True)

def get_xy(df, target_col='open_flag', **kwargs):
    feature_cols = [ col for col in df.columns if col != target_col ]
    if target_col in df:
        X = df[feature_cols]
        y = df[target_col]
        X_train, X_valid, y_train, y_valid = train_test_split(X, y)
        return X_train, X_valid, y_train, y_valid
    else:
        X_test = df[feature_cols]
        return X_test

# Import
train_df = pd.read_csv(data_path + 'train.csv').set_index('row_id')
test_df = pd.read_csv(data_path + 'test.csv').set_index('row_id')
user_df = pd.read_csv(data_path + 'users.csv')

# Merge
train_df = train_df.merge(user_df, left_on = 'user_id', right_on = 'user_id')
test_df = test_df.merge(user_df, left_on = 'user_id', right_on = 'user_id')


# Revise Date
add_datepart(train_df, 'grass_date')
add_datepart(test_df, 'grass_date')
remove_datecols(train_df)
remove_datecols(test_df)

# Remove user_id
train_df.drop('user_id', axis = 1, inplace = True)
test_df.drop('user_id', axis = 1, inplace = True)


train_df = pd.concat([train_df.drop('country_code', axis=1), pd.get_dummies(train_df['country_code'])], axis=1)
train_df = pd.concat([train_df.drop('domain', axis=1), pd.get_dummies(train_df['domain'])], axis=1)
test_df = pd.concat([test_df.drop('country_code', axis=1), pd.get_dummies(test_df['country_code'])], axis=1)
test_df = pd.concat([test_df.drop('domain', axis=1), pd.get_dummies(test_df['domain'])], axis=1)

# Deal with Never
train_df.replace(["Never open", "Never login", "Never checkout"], np.nan, inplace = True)
test_df.replace(["Never open", "Never login", "Never checkout"], np.nan, inplace = True)
train_df[['last_open_day','last_login_day','last_checkout_day']] = train_df[['last_open_day','last_login_day','last_checkout_day']].apply(pd.to_numeric)
test_df[['last_open_day','last_login_day','last_checkout_day']] = test_df[['last_open_day','last_login_day','last_checkout_day']].apply(pd.to_numeric)

#Fill missing values
train_df.fillna({"last_open_day":train_df['last_open_day'].max(),
                 "last_login_day":train_df['last_login_day'].max(),
                 "last_checkout_day":train_df['last_checkout_day'].max(),
                 "attr_1": 2,
                 "attr_2": 2,
                 "attr_3": 2,
                 "age": train_df['age'].median()}, inplace = True)

test_df.fillna({"last_open_day":test_df['last_open_day'].max(),
                 "last_login_day":test_df['last_login_day'].max(),
                 "last_checkout_day":test_df['last_checkout_day'].max(),
                 "attr_1": 2,
                 "attr_2": 2,
                 "attr_3": 2,
                 "age": test_df['age'].median()}, inplace = True)

# Split
X_train, X_valid, y_train, y_valid = get_xy(train_df, test_size=0.2, random_state=1234)
X_test = get_xy(test_df)

# Train
model = RandomForestClassifier(min_samples_split=10, max_depth = 2000, n_estimators = 300, n_jobs = -1, bootstrap = True, random_state = 1234)
f = model.fit(X_train, y_train)

# Evaluate
y_pred = f.predict(X_valid)
score = matthews_corrcoef(y_valid,y_pred)
print(score)
# Predict
y_pred = model.predict(X_test)
submission = pd.DataFrame({'row_id':np.arange(len(test_df)), 'open_flag':y_pred})
submission.to_csv('submission.csv', index = False)