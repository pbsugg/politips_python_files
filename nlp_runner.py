import db_politips
from db_politips import *
import keyword_analyzer
from keyword_analyzer import *
import sys
import os

if sys.argv[1] == "development":
    config = {
    'postgresql': {
    'driver': 'postgres',
    'database': 'politips_development'
    }
    }

elif sys.argv[1] == "production":
    config = {
    'postgresql': {
    'driver': 'postgres',
    'host': 'ec2-54-243-149-147.compute-1.amazonaws.com',
    'database': 'dai8rr8jl2ljkn',
    'username': 'lqoappvkzjvdnh',
    'password': os.environ.get('PG_DBKEY'),
    'port': '5432'
    }
    }

def initialize_database(db_config):
    db = DatabaseManager(config)
    Model.set_connection_resolver(db)
    print(db)
 

initialize_database(config)
gather_files_and_run_keyword_analysis()
