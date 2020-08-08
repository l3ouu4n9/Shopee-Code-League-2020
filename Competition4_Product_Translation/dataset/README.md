# Data Description
In Shopee Product Title Translation competition, there are two large scale product title data in traditional Chinese and English. They are from popular product categories, e.g., women's fashion, electronics, etc. The two dataset are not in labelled pair format and contain a lot of noises.

### File descriptions
- train_tcn.csv: training dataset for traditional Chinese product titles (500k)
- train_en.csv: training dataset for English product titles (500k)
- dev_tcn.csv: dev (validation) set for traditional Chinese product titles (1k)
- dev_en.csv: dev (validation) set for English product titles (1k)
- test_tcn.csv: test dataset for traditional Chinese product titles (10k)

Note:
train_tcn.csv and train_en.csv are not parallel data
dev_tcn.csv and dev_en.csv are parallel data which you can check your model's sacrebleu score with lowercase parameter (https://github.com/mjpost/sacrebleu).

Submission file should follow the dev_en.csv format with a header of "translation_output" and all translations followed in each row.

### Columns of data fields
- product_title: product title (str).
- category: product category (str).