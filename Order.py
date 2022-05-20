from sqlite3 import Date

from numpy import void
from OrderDetails import OrderDetails

class Order:
    Orderld: str
    date: Date
    CustomerName: str
    Customerld: str


def __init__(self,Orderdetail:OrderDetails):
    pass

def placeOrder():
    return void