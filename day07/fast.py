#fast모듈
from random import choice as ch

food = ['McDonalds', 'KFC', 'Bugger King', 'Taco Bell', 'Wendys', 'Arbys', 'Pizza Hut']

def pick():
    """Return random fast food"""
    return ch(food)

if __name__ == '__main__':
    print("fast모듈")