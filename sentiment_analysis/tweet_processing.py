import csv
import nltk
from nltk.corpus import stopwords

container = []
with open("fiorina_cleaned_tweets.csv", "rU") as csvfile:
    tweetreader = csv.reader(csvfile, delimiter= ' ')
    for row in tweetreader:
        words_lowered = [word.lower() for word in row]
        unicoded = [unicode(word, "utf-8", errors='replace') for word in words_lowered ]
        filtered_words = [word for word in unicoded if word not in stopwords.words('english')]
        ascii_encoded = [word.encode('ascii','ignore') for word in filtered_words]
        container.append(ascii_encoded)
print(container)
