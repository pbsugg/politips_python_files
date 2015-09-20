import codecs
import nltk
import json
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
class CountAllCategories:
    def __init__(self, file, category_data):
        self.file = file
        self.category_data = category_data
    def run(self):
        for i in self.category_data:
            category = CategoryCount(self.file)
            result = category.get_category_count(data[i], i)
            final_object["children"].append(result)
        print(final_object)
    def what(self):
        print(Candidate.find(1).scorings[0].score)



class CategoryCount:

    def __init__(self, file):
        self.file = file
        # self.category = category
        self.category_count = 0
        # self.stem = nltk.stem.porter.PorterStemmer()
        self.lemm = nltk.WordNetLemmatizer()
    def normalize(self):
        encoded_doc = codecs.open(self.file, encoding='utf-8', mode='rU')
        raw = encoded_doc.read()
        word_tokenized_doc = nltk.word_tokenize(raw)
        lowered_doc = [w.lower() for w in word_tokenized_doc]
        # stemming does weird shit--taking out for now
        # stemmed_doc = [self.stem.stem_word(w) for w in lowered_doc]
        lemmatized_doc = [self.lemm.lemmatize(w) for w in lowered_doc]
        return lemmatized_doc
    def count_term_frequency(self, term):
        doc = self.normalize()
        count = doc.count(term)
        self.category_count += count
        return self.category_count
    def get_category_count(self, category, category_name):
        term = 0
        for i in category:
            self.count_term_frequency(i)
        category_data = { "category": category_name, "value": self.category_count }
        return category_data

# data["children"].append(category_data)

# from parser import *
test = CountAllCategories("test.txt", data)
test.what()
# test.run()
