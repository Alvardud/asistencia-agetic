from distutils.debug import DEBUG
import os
from pickle import FALSE

# SECRET_KEY == os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
JSON_AS_ASCII = FALSE