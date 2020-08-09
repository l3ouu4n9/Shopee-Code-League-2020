# Background Information

The aim of this project is to build a model that can predict whether a user opens the emails sent by Shopee.

Sending emails is one of the marketing channels Shopee uses to reach out to our users. Being able to predict whether a user opens an email allows Shopee to forecast and evaluate the performance of future marketing campaigns before launch. This is because when a user opens an email, the probability of the user knowing the campaign increases and this in turn increases the probability of the user making a checkout during the campaign period. Therefore, with the predicted open rates, Shopee can better develop, strategize and implement future marketing campaigns.

# Task

We provide you with data related to marketing emails (Electronic Direct Mail) that were sent to Shopee users over a certain period. It contains information about

- User-specific information
- Email nature
- Users’ engagement on the platform
- User’s reaction to the email, including whether users opened the email

Based on the data provided, you must predict whether each user will open an email sent to him/her.

# Submission File

For each row in the test set, you must make a binary prediction for the target variable. The file should contain a header and have the following format:

>row_id,open_flag<br>
0,0<br>
1,1<br>
2,0<br>
etc.

Your submission should have 55,970 rows, each with 2 columns.

# Final Score
0.50070
