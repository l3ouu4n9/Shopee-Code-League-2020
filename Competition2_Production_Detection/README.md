# Background

At Shopee, we always strive to ensure the correct listing and categorization of products. For example due to the recent pandemic situation, face masks become extremely popular for both buyers and sellers, everyday we need to categorize and update a huge number of masks items. A robust product detection system will significantly improve the listing and categorization efficiency. But in the industrial field the data is always much more complicated and there exists mis-labelled images, complex background images and low resolution images, etc. The noisy and imbalanced data and multiple categories make this problem still challenging in the modern computer vision field.

# Task

In this competition, a multiple image classification model needs to be built. There are ~100k images within 42 different categories, including essential medical tools like masks, protective suits and thermometers, home & living products like air-conditioner and fashion products like T-shirts, rings, etc. For the data security purpose the category names will be desensitized. The evaluation metrics is top-1 accuracy.

# Submission File

Submission file format should be `csv` file only. And for each `filename` in the test dataset, you must predict only one proper category name. The `csv` file should contain a header and have the following format:

> filename, category<br>
2f096e5e8e8955d43632be16e35993b5.jpg, 0<br>
3d63a44c82c9d1299b5791bdd2c7a4e8.jpg, 1

# Final Score
0.67940
