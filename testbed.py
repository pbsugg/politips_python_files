import nltk
import csv



# neg_tweets = [ ("Christians need support in our country (and around the world), their religious liberty is at stake! Obama has been horrible, I will be great", "negative"), ("If I would have challenged the man, the media would have accused me of interfering with that man's right of free speech. A no win situation!", "negative"),("If someone made a nasty or controversial statement about me to the president, do you really think he would come to my rescue? No chance!", "negative")]
#
# pos_tweets = [("Looking forward to meeting the students of Urbandale High School tomorrow- http://t.co/Urj3Tic2e3", "positive"), ("Wow, great post-debate poll: 'Trump Increases Lead' via Breitbart http://t.co/B3yJk2lJ8I", "positive"), ("Will be interviewed tonight by @seanhannity on @FoxNews at 10 PM. Enjoy!", "positive")]
#
#
# all_tweets = []
# for (tweet, sentiment) in pos_tweets + neg_tweets:
#     # eventually might want to stem and lemmatize these as well:
#     words = [e.lower() for e in tweet.split() if len(e) >= 3]
#     all_tweets.append((words, sentiment))

# Get frequency distribution

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiments) in tweets:
        all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


# tweet_features = get_word_features(get_words_in_tweets(all_tweets))
#
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in tweet_features:
        features['Contains({tweet_word})'.format(tweet_word=word)] = (word in tweet_words)
    return features

# features = extract_features(all_tweets[1][0]))
# training_set = nltk.classify.apply_features(extract_features, all_tweets)
# classifier = nltk.NaiveBayesClassifier.train(training_set)
# print(classifier.show_most_informative_features(5))
