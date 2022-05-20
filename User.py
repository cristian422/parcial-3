from sqlite3 import Date
from unicodedata import name

from numpy import void


class User:
    Usend:str
    Pasword:str
    Register:Date
    Name: str
    email: str

def login():
    return void