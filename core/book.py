import math
import random
import numpy as np
import pandas as pd
from string import *
from pandas import Series,DataFrame


def importBook(path):
    if not path:
        path = "data/book.csv"
    bookdf = pd.read_csv(path)
    booklist = []
    for index, row in bookdf.iterrows():
        booklist.append(dict(row))
    return booklist

def addBook(bookname,isbn,author,booktag,publisher,date,bookid,stock):
    bookdf = pd.read_csv("data/book.csv")
    if not booktag:
        booktag = "None"
    newbook = pd.DataFrame({'BookID':bookid,'Name':bookname,'Tag':booktag,'ISBN':isbn,'Publisher':publisher,'Date':date,'Author':author,'Stock':stock},index=[0])
    bookdf = bookdf.append(newbook,ignore_index=True)
    bookdf.to_csv("data/book.csv",index=False,sep=',')
    booklist = []
    for index, row in bookdf.iterrows():
        booklist.append(dict(row))
    return booklist 

def delBook(bookname):
    bookdf = pd.read_csv("data/book.csv")
    if bookdf.loc[bookdf[bookdf.Name == bookname].index[0],'Stock'] != 0:
        flag = False
    else:
        bookdf  = bookdf.drop(bookdf[bookdf.Name == bookname].index[0])
        bookdf.to_csv("data/book.csv",index=False,sep=',')
        flag = True
    booklist = []
    for index, row in bookdf.iterrows():
        booklist.append(dict(row))
    return booklist,flag

def modBook(bookname,isbn,author,booktag,publisher,date,bookid):
    bookdf = pd.read_csv("data/book.csv")
    if isbn:
        bookdf.loc[bookdf[bookdf.Name == bookname].index[0],'ISBN'] = isbn
    if author:
        bookdf.loc[bookdf[bookdf.Name == bookname].index[0],'Author'] = author
    if publisher:
        bookdf.loc[bookdf[bookdf.Name == bookname].index[0],'Publisher'] = publisher
    if booktag:
        bookdf.loc[bookdf[bookdf.Name == bookname].index[0],'Tag'] = booktag
    if date:
        bookdf.loc[bookdf[bookdf.Name == bookname].index[0],'Date'] = date
    if bookid:
        bookdf.loc[bookdf[bookdf.Name == bookname].index[0],'BookID'] = bookid
    bookdf.to_csv("data/book.csv",index=False,sep=',')
    booklist = []
    for index, row in bookdf.iterrows():
        booklist.append(dict(row))
    return booklist 

def searchBook(bookname,isbn,author,booktag,publisher):
    bookdf = pd.read_csv("data/book.csv")
    booklist = []
    if isbn:
        bookdf = bookdf[bookdf.ISBN == isbn]
    if author:
        bookdf = bookdf[bookdf.Author == author]
    if publisher:
        bookdf = bookdf[bookdf.Publisher == publisher]
    if booktag:
        bookdf = bookdf[bookdf.Tag == booktag]
    if bookname:
        bookdf = bookdf[bookdf.Name == bookname]
    
    for index, row in bookdf.iterrows():
        booklist.append(dict(row))
    return booklist 


def incBook(bookname,isbn,author,booktag,publisher,stock):
    bookdf = pd.read_csv("data/book.csv")
    bookdf2 = bookdf
    booklist = []
    if isbn:
        bookdf = bookdf[bookdf.ISBN == isbn]
    if author:
        bookdf = bookdf[bookdf.Author == author]
    if publisher:
        bookdf = bookdf[bookdf.Publisher == publisher]
    if booktag:
        bookdf = bookdf[bookdf.Tag == booktag]
    if bookname:
        bookdf = bookdf[bookdf.Name == bookname]
    if(bookdf.shape[0]==1):
        bookdf2.loc[bookdf2[bookdf2.ISBN == bookdf['ISBN'][0]].index[0],'Stock'] = int(stock) + bookdf['Stock'][0]
        bookdf2.to_csv("data/book.csv",index=False,sep=',')
        for index, row in bookdf.iterrows():
            booklist.append(dict(row))
        return booklist,True
    else:
        for index, row in bookdf.iterrows():
            booklist.append(dict(row))
        return booklist,False

def decBook(bookname,isbn,author,booktag,publisher,stock):
    bookdf = pd.read_csv("data/book.csv")
    bookdf2 = bookdf
    booklist = []
    if isbn:
        bookdf = bookdf[bookdf.ISBN == isbn]
    if author:
        bookdf = bookdf[bookdf.Author == author]
    if publisher:
        bookdf = bookdf[bookdf.Publisher == publisher]
    if booktag:
        bookdf = bookdf[bookdf.Tag == booktag]
    if bookname:
        bookdf = bookdf[bookdf.Name == bookname]
    for index, row in bookdf.iterrows():
        booklist.append(dict(row))
    if(bookdf.shape[0]==1):
        if(int(stock) > bookdf['Stock'][0]):
            return booklist,1
        bookdf2.loc[bookdf2[bookdf2.ISBN == bookdf['ISBN'][0]].index[0],'Stock'] = bookdf['Stock'][0] - int(stock)
        bookdf2.to_csv("data/book.csv",index=False,sep=',')
        return booklist,0
    else:
        return booklist,2

if __name__ == "__main__":
    #bookDataGen()
    #userDataGen()
    #Main()
    main()
    #importBook("../data/book.csv")
