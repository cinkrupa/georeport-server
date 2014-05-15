__author__ = 'Marcin'

import os

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
ORGANIZATION = 'AGH Katedra Informatyki'
JURISDICTION = 'ki.agh.edu.pl'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
