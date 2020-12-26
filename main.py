import math
import random
import numpy
import pandas
'''
	概述：
实现一个简单的图书管理系统。图书基本信息包括：图书ID，书名，ISBN，出版社，出版年月，作者，标签（可选做）。读者基本信息包括：读者ID，读者姓名，读者类型，读者联系电话。

	功能需求描述：
（1）图书信息维护。导入书目、增加书目、删除书目、修改书目。图书购置入库（库存增加）、图书处理出库（库存减少）。
（2）读者信息维护。导入读者、增加读者、删除读者、修改读者信息。
（3）图书信息查询。根据书名、作者、标签（可选做）、出版社和ISBN查询图书。显示库存数量，根据图书库存数量显示是否可借。
（4）读者信息查询。根据读者姓名、联系方式查询显示读者信息。查询显示读者在借图书信息。查询显示读者借阅历史。
（5）图书借出。
（6）图书归还。
（7）系统关闭。保存数据之后关闭系统。这些数据在系统启动的时候自动读入系统。

	使用方法描述：
（1）该系统由图书管理员操作，以上所有操作都不是由读者操作完成的。
（2）同一个ID的图书可能有多本，库存量随着入库、出库、借出、归还而改变。
（3）读者有两个类型：会员和非会员。主要区别是借阅的数量上限。会员上限8本，非会员上限4本。当未还图书数量达到上限时，无法借阅。
（4）只有在图书库存数量为0时，才可以删除书目。

	用户界面：
可以使用命令行界面或者图形用户界面，若使用图形用户界面评分时适当加分。

	菜单结构和导航设计：
不作强制要求。但有一些建议供考虑：
（1）读者在借图书和借阅历史这两个功能（按钮或菜单），建议安排在读者信息显示界面。
（2）图书借出功能，建议安排在图书显示界面。
（3）图书归还功能，建议安排在读者在借图书界面。
（4）图书入库和出库功能，建议安排在图书显示界面。
（5）在每个子菜单下面需要考虑用户可能会继续操作，也可能希望返回主菜单。

	上机实验验收和报告提交：
第5次上机实验为验收最后期限。验收之后一周内，需要提交一份简单的实验报告，包括系统架构和实现思路，代码文件作为附件提交给助教。

'''

class Book:
    '''
    - 图书信息维护。导入书目、增加书目、删除书目、修改书目。
      图书购置入库（库存增加）、图书处理出库（库存减少）。
    - 根据书名、作者、标签（可选做）、出版社和ISBN查询图书。
      显示库存数量，根据图书库存数量显示是否可借。
    - 图书基本信息包括：图书ID，书名，ISBN，出版社，出版年月，作者，标签（可选做）。
    - 图书借出。
    - 图书归还。
    '''
    def __init__(self,bookid,name,isbn,publisher,date,author,tag):
        self.bookid = bookid
        self.name = name
        self.isbn = isbn
        self.publisher = publisher
        self.date = date
        self.author = author
        self.tag = tag
    

class User:
    '''
    - 读者信息维护。导入读者、增加读者、删除读者、修改读者信息。
    - 读者信息查询。根据读者姓名、联系方式查询显示读者信息。
        查询显示读者在借图书信息。查询显示读者借阅历史。
    - 读者基本信息包括：读者ID，读者姓名，读者类型，读者联系电话。
    - 读者有两个类型：会员和非会员。主要区别是借阅的数量上限。
      会员上限8本，非会员上限4本。当未还图书数量达到上限时，无法借阅。
    '''
    def __init__(self,uid,name,viptype,phone):
        self.uid = uid
        self.name = name
        self.viptype = viptype
        self.phone = phone
#图书ID，书名，ISBN，出版社，出版年月，作者，标签（可选做）。
def bookDataGen():
    #f = open('../data/book.txt','r+',encoding='utf-8')
    namelist = ['编译原理','计算方法','算法基础','随机过程','计算机网络']
    authorlist = ['Amy','Bob','Cindy','David','Emily']
    publisherlist = ['科学出版社','科学出版社','科学出版社','科学出版社','机械工业出版社']
    taglist = ['cs','math','cs','cs','cs']
    stocklist = [2,3,4,5,6]
    with open("data/book.csv",'w+',encoding='utf-8') as f:
        f.write("BookID,Name,ISBN,Publisher,Date,Author,Tag,Stock\n")
        for i in range(len(namelist)):
            bookid = ""
            for ch in namelist[i]:
                bookid += str(ord(ch))
            #print(bookid,"\n")
            isbn = str(random.randint(1,10))
            for j in range(3):
                isbn += "-" + str(random.randint(1,100))
            date = str(random.randint(1900,2020)) + "-" + str(random.randint(1,13)) + "-" + str(random.randint(1,29)) 
            f.write("{},{},{},{},{},{},{},{}\n".format(bookid[-10:],namelist[i],isbn,publisherlist[i],date,authorlist[i],taglist[i],stocklist[i]))
    
#- 读者信息查询。根据读者姓名、联系方式查询显示读者信息。
#  查询显示读者在借图书信息。查询显示读者借阅历史。
#- 读者基本信息包括：读者ID，读者姓名，读者类型，读者联系电话。
def userDataGen():
    with open("data/user.csv",'w+',encoding='utf-8') as f:
        f.write("UserID,Name,Type,PhoneNumber,CurrentBorrow,History\n")
        namelist = ['张三','李四','王五','赵六']
        typelist = ['normal','vip','normal','vip']
        phonelist = ['18212341234','18312341234','18412341234','18512341234']
        for i in range(len(namelist)):
            uid = ""
            for ch in namelist[i]:
                uid += str(ord(ch))
            emptystr = ""
            f.write("{},{},{},{},{},{}\n".format(uid[-8:],namelist[i],typelist[i],phonelist[i],emptystr,emptystr))
#现在的想法是把借阅信息写入字符串然后对字符串进行处理
def Manager():
    print("----------选择需要进行的操作------------")
    print("1. 导入书目")
    print("2. 增加书目")
    print("3. 删除书目")
    print("4. 修改书目")
    print("5. 购置图书")
    print("6. 图书出库")
    print("7. 导入读者\n8. 增加读者\n9. 删除读者\n10. 修改读者信息\n11. 退出")
    case = int(input())

def User():
    print("------------选择需要进行的操作-----------")
    print("1. 查询书目")
    print("2. 借阅书籍")
    print("3. 归还书籍")
    case = int(input())

def Main():
    print("-------------选择身份--------------\n")
    print("1.管理员")
    print("2.用户")
    user = int(input())
    #无语了为什么python没有switch
    if(user == 1):
        Manager()
    else:
        User()

if __name__ == "__main__":
    #bookDataGen()
    #userDataGen()
    #Main()
