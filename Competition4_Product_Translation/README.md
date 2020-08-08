# Background

At Shopee, we have customers and sellers across Southeast Asia and Taiwan. In order to provide a better shopping experience, we set up the cross border business to improve the variety of products for our customers. In order to help the local sellers to migrate the SKUs to different foreign markets, we hire a group of professional human translators with an e-commerce background to take care of the product translation. The product information translated includes product title, variation and description. However, as Shopee is growing tremendously in recent years, the amount of translation per day is beyond the human translators’ capacity. At the same time, with the development of AI technology, machine translation is now deployed in many industrial areas to assist the human translators and they can achieve a near-human level translation quality.

In Shopee, we have an in-house machine translation pipeline which can translate millions of SKUs per week in different languages. The languages include Traditional Chinese, Bahasa, English, Vietnames, Thai and Portuguese. The challenges in machine translation is usually the lack of labelled data. However, different ways of unsupervised machine translation have been explored and proven to be effective, with little or even no label data. Some techniques are cross-lingual word alignments or pretrained cross-lingual language models.

**Note: This page is for participants from open group! **

# Task

Given a product title in Traditional Chinese, the candidate is expected to translate the title into English.

Dataset: Candidates are provided with two monolingual product title data (in Traditional Chinese and English). Use of public data is encouraged.

Metrics: Bleu score of the whole test set is used to assess the translation quality.

# Evaluation

The file should contain a header and have the following format:

> translation_output # header<br>
translated title string one<br>
translated title string two<br>
...

# Final Score
40.38, 27th place in Open Category
