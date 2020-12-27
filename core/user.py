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
    userdf2  = userdf2.drop(userdf2[userdf2.UserID == userdf['UserID'][0]].index[0])
    userdf2.to_csv("data/user.csv",index=False,sep=',')
    for index, row in userdf.iterrows():
        userlist.append(dict(row))
    return userlist,True

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