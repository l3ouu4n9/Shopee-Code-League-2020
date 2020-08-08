import csv
import string

# input csv
input_file = open('/home/lai/shopee/challenge_4/leo/ans.csv', 'r')
rows = csv.reader(input_file)
next(rows)

# output csv
output_file = open('/home/lai/shopee/challenge_4/leo/ans_modified.csv', 'w')
writer = csv.writer(output_file)
writer.writerow(['translation_output'])
char_list = list(string.ascii_letters + string.digits + string.whitespace)
for row in rows:
	s = ''
	s_test = row[0]
	for char in s_test:
		if char in char_list:
			s += char
	writer.writerow([s])

input_file.close()
output_file.close()
