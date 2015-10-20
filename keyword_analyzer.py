import codecs
import nltk
# from nltk.corpus import stopwords
import db_politips
from db_politips import *
import glob
import re


# TD: stem and lemmatize our search terms before bringing them in.
    # right now stemming does weird things--have to normalize docs as well
    # self.stem = nltk.stem.porter.PorterStemmer()
    # stemmed_doc = [self.stem.stem_word(w) for w in lowered_doc]
# TD: remove stopwords
    # stopwords = stopwords.words('english')

class CategoryCount:

    def __init__(self, doc, category_name):
        self.category = Category.where('name', category_name).first()
        self.category_count = 0
        self.doc = doc
    def count_keyword_frequencies(self):
        for keyword in self.category.keywords:
            count = self.doc.count(keyword.word)
            self.category_count += count
        return self.category_count


class CountAllCategories:
    def __init__(self, file, candidate_last_name):
        self.lemm = nltk.WordNetLemmatizer()
        self.doc = self.normalize(file)
        self.candidate = Candidate.where('last_name', candidate_last_name).first()
    def normalize(self, file):
        encoded_doc = codecs.open(file, encoding='utf-8', mode='rU')
        raw = encoded_doc.read()
        word_tokenized_doc = nltk.word_tokenize(raw)
        lowered_doc = [w.lower() for w in word_tokenized_doc]
        lemmatized_doc = [self.lemm.lemmatize(w) for w in lowered_doc]
        return lemmatized_doc
    def run(self):
        categories = Category.all()
        for category in categories:
            single_category = CategoryCount(self.doc, category.name)
            score_val = single_category.count_keyword_frequencies()
            print("{last_name}: {category_name}: {score}".format(last_name=self.candidate.last_name, category_name=category.name, score=score_val))
            entry = Scoring.create(score=score_val, category_id=category.id, candidate_id=self.candidate.id)
            print(entry)

def extract_candidate_name_from_filename(dir_string):
    # pattern is everything between the "speeches/" directory and underscore
    #  (should be just name, capitalized)
    candidate_name_search_pattern = re.compile("(?<=/raw-text/master-files/).+?(?=_)")
    result = candidate_name_search_pattern.search(dir_string)
    return result.group(0).title()

def gather_files_and_run_keyword_analysis():
    all_files_to_parse = glob.glob("../raw-text/master-files/*.txt")
    for individual_text in all_files_to_parse:
        candidate = extract_candidate_name_from_filename(individual_text)
        if Candidate.where('last_name', candidate).first():
            instance = CountAllCategories(individual_text, candidate)
            instance.run()
