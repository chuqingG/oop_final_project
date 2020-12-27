import math
import random
import re
import numpy as np
import pandas as pd
from string import *
from pandas import Series,DataFrame

def importUser(path):
    if not path:
        path = "data/user.csv"
    userdf = pd.read_csv(path)
    userdf2 = pd.read_csv("data/user.csv")
    userdf = pd.merge(userdf2, userdf, how='outer')
    userdf.to_csv("data/user.csv",index=False,sep=',')
    userlist = []
    for index, row in userdf.iterrows():
        userlist.append(dict(row))
    return userlist

def addUser(username,uid,usertype,phone):
    userdf = pd.read_csv("data/user.csv")
    newuser = pd.DataFrame({'UserID':uid,'Name':username,'Type':usertype,'PhoneNumber':phone,'CurrentBorrow':"None",'History':"None"},index=[0])
    userdf = userdf.append(newuser,ignore_index=True)
    userdf.to_csv("data/user.csv",index=False,sep=',')
    userlist = []
    for index, row in userdf.iterrows():
        userlist.append(dict(row))
    return userlist 

def delUser(username,uid,usertype,phone):
    userdf = pd.read_csv("data/user.csv")
    userdf2 = userdf
    userlist = []
    if uid:
        userdf = userdf[userdf.UserID == int(uid)]
    if usertype:
        userdf = userdf[userdf.Type == usertype]
    if username:
        userdf = userdf[userdf.Name == username]
    if phone:
        userdf = userdf[userdf.PhoneNumber == int(phone)]
    if(userdf.shape[0]!=1):
        for index, row in userdf.iterrows():
            userlist.append(dict(row))
        return userlist,False
    userdf2  = userdf2.drop(userdf2[userdf2.UserID == userdf.loc[userdf.index[0],'UserID']].index[0])
    userdf2.to_csv("data/user.csv",index=False,sep=',')
    for index, row in userdf2.iterrows():
        userlist.append(dict(row))
    return userdf.loc[userdf.index[0],'Name'],userlist,True

def modUser(username,uid,usertype,phone):
    userdf = pd.read_csv("data/user.csv")
    userdf2 = userdf
    userlist = []
    if uid:
        index = userdf[userdf.UserID == int(uid)].index[0]
    else:
        for index, row in userdf.iterrows():
            userlist.append(dict(row))
        return userlist,False
    if usertype:
        userdf2.loc[index,'Type'] =  usertype
    if username:
        userdf2.loc[index,'Name'] =  username
    if phone:
        userdf2.loc[index,'PhoneNumber'] = int(phone)
    userdf = userdf2[userdf2.UserID == int(uid)]
    userdf2.to_csv("data/user.csv",index=False,sep=',')
    for index, row in userdf.iterrows():
        userlist.append(dict(row))
    return userlist,True

def searchUser(username,uid,usertype,phone):
    userdf = pd.read_csv("data/user.csv")
    userlist = []
    hislist = []
    curlist = []
    if uid:
        userdf = userdf[userdf.UserID == int(uid)]
    if usertype:
        userdf = userdf[userdf.Type == usertype]
    if username:
        userdf = userdf[userdf.Name == username]
    if phone:
        userdf = userdf[userdf.PhoneNumber == int(phone)]
    for index, row in userdf.iterrows():
        userlist.append(dict(row))
    if(userdf.shape[0]!=1):
        flag = False
    else:
        flag = True
        hislist = re.findall(r"@@(.+?)%%",userlist[0]['History'])
        curlist = re.findall(r"@@(.+?)%%",userlist[0]['CurrentBorrow'])
    if not hislist:
        hislist.append('None')
    if not curlist:
        curlist.append('None')
    return userlist,flag,hislist,curlist

def confirmUser(username,uid):
    userdf = pd.read_csv("data/user.csv")
    userlist = []
    hislist = []
    curlist = []
    if uid:
        userdf = userdf[userdf.UserID == int(uid)]
    if username:
        userdf = userdf[userdf.Name == username]
    for index, row in userdf.iterrows():
        userlist.append(dict(row))
    if(userdf.shape[0]==0):
        flag = False
    else:
        flag = True
        userdf.to_csv("data/curuser.csv",index=False,sep=',')
        hislist = re.findall(r"@@(.+?)%%",userlist[0]['History'])
        curlist = re.findall(r"@@(.+?)%%",userlist[0]['CurrentBorrow'])
    if not hislist:
        hislist.append('None')
    if not curlist:
        curlist.append('None')
    return userlist,flag,hislist,curlist

def borrowBook(bookname,isbn,author,booktag,publisher):
    bookdf = pd.read_csv("data/book.csv")
    bookdf2 = bookdf
    userdf = pd.read_csv("data/user.csv")
    curdf = pd.read_csv("data/curuser.csv")
    booklist = []
    hislist = []
    curlist = []
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
    if(curdf.shape[0]==0):
        return booklist,2,hislist,curlist
    if(bookdf.shape[0]==1):
        if(bookdf.loc[bookdf.index[0],'Stock']==0):
            return booklist,3,hislist,curlist
        curlist = re.findall(r"@@(.+?)%%",curdf['CurrentBorrow'][0])
        if((len(curlist)==4 and curdf['Type'][0]=='normal') or (len(curlist)==8 and curdf['Type'][0]=='vip')):
            return booklist,4,hislist,curlist
        bookdf2.loc[bookdf2[bookdf2.ISBN == bookdf.loc[bookdf.index[0],'ISBN']].index[0],'Stock'] = bookdf.loc[bookdf.index[0],'Stock'] - 1
        bookdf2.to_csv("data/book.csv",index=False,sep=',')
        userdf.loc[userdf[userdf.UserID == curdf['UserID'][0]].index[0],'CurrentBorrow'] = "@@" + bookdf.loc[bookdf.index[0],'Name'] + "%%" + curdf['CurrentBorrow'][0]
        userdf.loc[userdf[userdf.UserID == curdf['UserID'][0]].index[0],'History'] = "@@" + bookdf.loc[bookdf.index[0],'Name'] + "%%" + curdf['History'][0]
        curdf.loc[0,'CurrentBorrow'] = "@@" + bookdf.loc[bookdf.index[0],'Name'] + "%%" + curdf['CurrentBorrow'][0]
        curdf.loc[0,'History'] = "@@" + bookdf.loc[bookdf.index[0],'Name'] + "%%" + curdf['History'][0]
        curdf.to_csv("data/curuser.csv",index=False,sep=',')
        userdf.to_csv("data/user.csv",index=False,sep=',')
        hislist = re.findall(r"@@(.+?)%%",curdf.loc[0,'History'])
        curlist = re.findall(r"@@(.+?)%%",curdf.loc[0,'CurrentBorrow'])
        booklist[0]['Stock'] -= 1
        return booklist,0,hislist,curlist
    else:
        return booklist,1,hislist,curlist

def returnBook(bookname,isbn,author,booktag,publisher):
    bookdf = pd.read_csv("data/book.csv")
    bookdf2 = bookdf
    userdf = pd.read_csv("data/user.csv")
    curdf = pd.read_csv("data/curuser.csv")
    booklist = []
    hislist = []
    curlist = []
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
    if(curdf.shape[0]==0):
        return booklist,2,hislist,curlist
    if(bookdf.shape[0]==1):
        curlist = re.findall(r"@@(.+?)%%",curdf.loc[0,'CurrentBorrow'])
        if not bookdf.loc[bookdf.index[0],'Name'] in curlist:
            return booklist,3,hislist,curlist
        bookdf2.loc[bookdf2[bookdf2.ISBN == bookdf.loc[bookdf.index[0],'ISBN']].index[0],'Stock'] = bookdf.loc[bookdf.index[0],'Stock'] + 1
        bookdf2.to_csv("data/book.csv",index=False,sep=',')
        userdf.loc[userdf[userdf.UserID == curdf['UserID'][0]].index[0],'CurrentBorrow'] = userdf.loc[userdf[userdf.UserID == curdf['UserID'][0]].index[0],'CurrentBorrow'].replace("@@" + bookdf.loc[bookdf.index[0],'Name'] + "%%","",1)
        curdf.loc[0,'CurrentBorrow'] = curdf.loc[0,'CurrentBorrow'].replace("@@" + bookdf.loc[bookdf.index[0],'Name'] + "%%","",1)
        curdf.to_csv("data/curuser.csv",index=False,sep=',')
        userdf.to_csv("data/user.csv",index=False,sep=',')
        hislist = re.findall(r"@@(.+?)%%",curdf.loc[0,'History'])
        curlist = re.findall(r"@@(.+?)%%",curdf.loc[0,'CurrentBorrow'])
        booklist[0]['Stock'] += 1
        return booklist,0,hislist,curlist
    else:
        return booklist,1,hislist,curlist