import codecs
import nltk
# import json
from nltk.corpus import stopwords
import db_politips
from db_politips import *


# categories = {
#     {"immigration" :["immigrant","border","the","security"]},
#     "marriage" : ["people","the","children","values"]
#     }

# TD: stem and lemmatize our search terms before bringing them in.
# TD: remove stopwords
stopwords = stopwords.words('english')

# search_terms: array of terms to search through, taken from database
final_object = {"name": "Trump", "children":[]}

data = {"immigration": ["america","good","the","hello","bad","good"],
"another_category": ["people","the","children","values","why"],
"education": ["good","we","no","jersey","alright"],
"marriage equality" : ["marriage", "equality", "or"],
"foreign_policy" : ["countries", "iraq", "iran","aid","no" ]}
#


class CategoryCount:

    def __init__(self, file, category_name):
        self.category = Category.where('name', category_name)
        self.lemm = nltk.WordNetLemmatizer()
        self.doc = self.normalize(file)
        self.category_count = 0
        # self.stem = nltk.stem.porter.PorterStemmer()
    def normalize(self, file):
        encoded_doc = codecs.open(file, encoding='utf-8', mode='rU')
        raw = encoded_doc.read()
        word_tokenized_doc = nltk.word_tokenize(raw)
        lowered_doc = [w.lower() for w in word_tokenized_doc]
        # stemming does weird shit--taking out for now
        # stemmed_doc = [self.stem.stem_word(w) for w in lowered_doc]
        lemmatized_doc = [self.lemm.lemmatize(w) for w in lowered_doc]
        return lemmatized_doc
    def count_keyword_frequencies(self):
        for keyword in self.category.first().keywords:
            count = self.doc.count(keyword.word)
            self.category_count += count
        return self.category_count

# data["children"].append(category_data)

# from parser import *
# test = CategoryCount("test.txt", "Taxes")
# print(test.count_keyword_frequencies())

# print(test.file)
# print(test.category.first().keywords[0].keyword)

class CountAllCategories:
    def __init__(self, file, candidate):
        self.file = file
        self.candidate = candidate
    def run(self):
        categories = Category.all()
        for category in categories:
            instance = CategoryCount(self.file, category.name)
            print(instance.count_keyword_frequencies())
            # print(category.name)
            # category = CategoryCount(self.file)
            # result = category.get_category_count(data[i], i)
            # final_object["children"].append(result)
        # print(self.candidate)
    def what(self):
        print(Candidate.find(1).scorings[0].score)

test = CountAllCategories("test.txt", "Trump")
test.run()
