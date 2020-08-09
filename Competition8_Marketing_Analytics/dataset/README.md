## Data Description

Given the recent history of a user's interactions with previous email campaigns, can you predict the success of the next one? This is a common business problem, but one that it is usually hard to find real, publicly accessible datasets for.

### Files

[train/test].csv

- country_code: An integer code for the country where the user lives.
- grass_date: The date when the email was sent.
- user_id: the unique identifier of each user
- subject_line_length: the number of characters in the subject of the email
- last_open_day: How many days ago was the last time the user opened an email
- last_login_day: How many days ago the user last logged in its Shopee account
- last_checkout_day: How many days ago the user last purchased on Shopee
- open_count_last_[10/30/60]_days: the total number of email opens in the last N days.
- login_count_last_[10/30/60]_days: the total number of user logins in the last N days.
- checkout_count_last_[10/30/60]_days: the total number of checkouts (=purchases) by the user in the last N days.
- open_flag: the target variable. Whether or not the email was opened.
- row_id:

users.csv 
[empty values are simply unknown]

- user_id: the unique identifier of each user
- attr_[1/2/3]: general user attributes. Attr_1 and attr_2 are boolean, attrib_3 is categorical (can be integer [0,1,2,3,4])
- age: The user's reported age.
- domain: The user's top-level email domain. Less common domains are bundled together under the label 'other'.

sample_submission_0_1.csv: A valid submission file.