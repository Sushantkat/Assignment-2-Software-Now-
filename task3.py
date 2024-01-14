import csv
from collections import Counter
import string

input_txt_file = 'allcsv.txt'
output_csv_file = 'topwordscount.csv'

# Reading the text from the file
with open(input_txt_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Removing punctuation and convert to lowercase
translator = str.maketrans("", "", string.punctuation)
text = text.translate(translator).lower()

# Tokenize the text into words
words = text.split()

# Counting occurrences of each word
word_counts = Counter(words)

# Getting the top 30 most common words
top_words = word_counts.most_common(30)

# Storing the top words and counts in a CSV file
with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Word', 'Count']) 

    for word, count in top_words:
        csv_writer.writerow([word, count])