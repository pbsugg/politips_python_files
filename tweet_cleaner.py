import csv
import testbed
from testbed import *
import nltk
from nltk.corpus import stopwords

container = []
with open("trump_cleaned_tweets.csv", "rU") as csvfile:
    tweetreader = csv.reader(csvfile, delimiter= ' ')
    for row in tweetreader:
        words_lowered = [word.lower() for word in row]
        unicoded = [unicode(word, "utf-8", errors='replace') for word in words_lowered ]
        filtered_words = [word for word in unicoded if word not in stopwords.words('english')]
        ascii_encoded = [word.encode('ascii','ignore') for word in filtered_words]
        container.append(ascii_encoded)
# print(container)


all_tweets = []
for tweet in container:
    sentiment = tweet[-1][-1]
    tweet[-1] = tweet[-1][:-1]
    new = [tweet, sentiment]
    tupled = tuple(new)
    all_tweets.append(tupled)

# print(all_tweets[0][-1])

#
tweet_features = get_word_features(get_words_in_tweets(all_tweets))
# print(tweet_features)

def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in tweet_features:
        features['Contains({tweet_word})'.format(tweet_word=word)] = (word in tweet_words)
    return features


training_set = nltk.classify.apply_features(extract_features, all_tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)
# print(classifier.show_most_informative_features(10))
# print(tweet_features)
print("trump")
#
#
tweet = "So happy about my daughter @IvankaTrump announcement that she will be having a baby this spring. Congratulations!"
tweet = tweet.lower()
print(classifier.classify(extract_features(tweet.split())))
