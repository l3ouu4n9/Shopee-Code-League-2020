import csv
from googletrans import Translator


# input csv
input_file = open('/home/lai/shopee/challenge_4/dataset/test_tcn.csv', 'r')
rows = csv.reader(input_file)
next(rows)

# output csv
output_file = open('/home/lai/shopee/challenge_4/leo/submission.csv', 'w')
writer = csv.writer(output_file)
writer.writerow(['translation_output'])

# all
for row in rows:
	translator = Translator()
	translation = translator.translate(row[0], src='zh-tw', dest='en')
	text = translation.text
	writer.writerow([text])

input_file.close()
output_file.close()