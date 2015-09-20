from orator import DatabaseManager, Model
import psycopg2
import psycopg2.extras

config = {
    'postgresql': {
        'driver': 'postgres',
        'database': 'politips_development'
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)
print(db)

class Candidate(Model):

    @property
    def scorings(self):
        return self.has_many(Scoring)

class Scoring(Model):
    __fillable__ = ['score', 'candidate_id', 'category_id']

class Category(Model):

    @property
    def keywords(self):
        return self.has_many(Keyword)

class Keyword(Model):
    pass
