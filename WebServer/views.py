from django.http import JsonResponse
from django.shortcuts import render
from py2neo import *
from core import book, user
import os
import tkinter as tk
from tkinter import filedialog
from . import settings


def home(request):
    return render(request, 'home.html')

def admin(request):
    return render(request, 'admin.html')

def reader(request):
    return render(request, 'reader.html')

def return_gdbfs(request):
    return render(request, 'gdbfs.html')


def import_book(request):
    path = request.POST.get('path')
    bookdf = book.importBook(path)
    print("import book")
    return JsonResponse({'bookdf': bookdf})

def import_user(request):
    path = request.POST.get('path')
    userdf = user.importUser(path)
    print("import user")
    return JsonResponse({'userdf': userdf})

def add_book(request):
    bookname = request.POST.get('bookname')
    isbn = request.POST.get('isbn')
    author = request.POST.get('author')
    booktag = request.POST.get('booktag')
    publisher = request.POST.get('publisher')
    date = request.POST.get('date')
    bookid = request.POST.get('bookid')
    stock = request.POST.get('stock')
    bookdf = book.addBook(bookname,isbn,author,booktag,publisher,date,bookid,stock)
    return JsonResponse({'bookdf': bookdf})

def add_user(request):
    username = request.POST.get('username')
    uid = request.POST.get('uid')
    usertype = request.POST.get('usertype')
    phone = request.POST.get('phone')
    userdf = user.addUser(username,uid,usertype,phone)
    return JsonResponse({'userdf': userdf})

def del_book(request):
    bookname = request.POST.get('bookname')
    bookdf,flag = book.delBook(bookname)
    return JsonResponse({'bookdf': bookdf,'flag': flag})

def del_user(request):
    username = request.POST.get('username')
    uid = request.POST.get('uid')
    usertype = request.POST.get('usertype')
    phone = request.POST.get('phone')
    userdf,flag = user.delUser(username,uid,usertype,phone)
    return JsonResponse({'userdf': userdf,'flag':flag})

def mod_user(request):
    username = request.POST.get('username')
    uid = request.POST.get('uid')
    usertype = request.POST.get('usertype')
    phone = request.POST.get('phone')
    userdf,flag = user.modUser(username,uid,usertype,phone)
    print("views mod")
    return JsonResponse({'userdf': userdf,'flag':flag})

def search_user(request):
    username = request.POST.get('username')
    uid = request.POST.get('uid')
    usertype = request.POST.get('usertype')
    phone = request.POST.get('phone')
    userdf,flag,his,cur = user.searchUser(username,uid,usertype,phone)
    return JsonResponse({'userdf': userdf,'flag':flag})

def user_confirm(request):
    username = request.POST.get('username')
    uid = request.POST.get('uid')
    userdf,flag,his,cur = user.confirmUser(username,uid)
    return JsonResponse({'userdf': userdf,'flag':flag,'hislist':his,'curlist':cur})

def search_his(request):
    username = request.POST.get('username')
    print(username)
    uid = request.POST.get('uid')
    usertype = request.POST.get('usertype')
    phone = request.POST.get('phone')
    userdf,flag,his,cur = user.searchUser(username,uid,usertype,phone)
    return JsonResponse({'userdf': userdf,'flag':flag,'hislist':his,'curlist':cur})

def mod_book(request):
    bookname = request.POST.get('bookname')
    isbn = request.POST.get('isbn')
    author = request.POST.get('author')
    booktag = request.POST.get('booktag')
    publisher = request.POST.get('publisher')
    date = request.POST.get('date')
    bookid = request.POST.get('bookid')
    bookdf = book.modBook(bookname,isbn,author,booktag,publisher,date,bookid)
    return JsonResponse({'bookdf': bookdf})

def search_book(request):
    bookname = request.POST.get('bookname')
    isbn = request.POST.get('isbn')
    author = request.POST.get('author')
    booktag = request.POST.get('booktag')
    publisher = request.POST.get('publisher')
    bookdf = book.searchBook(bookname,isbn,author,booktag,publisher)
    return JsonResponse({'bookdf': bookdf})

def borrow_book(request):
    print("coming view")
    bookname = request.POST.get('bookname')
    isbn = request.POST.get('isbn')
    author = request.POST.get('author')
    booktag = request.POST.get('booktag')
    publisher = request.POST.get('publisher')
    bookdf,flag,his,cur = user.borrowBook(bookname,isbn,author,booktag,publisher)
    return JsonResponse({'bookdf': bookdf,'flag':flag,'hislist':his,'curlist':cur})

def return_book(request):
    bookname = request.POST.get('bookname')
    isbn = request.POST.get('isbn')
    author = request.POST.get('author')
    booktag = request.POST.get('booktag')
    publisher = request.POST.get('publisher')
    bookdf,flag,his,cur = user.returnBook(bookname,isbn,author,booktag,publisher)
    return JsonResponse({'bookdf': bookdf,'flag':flag,'hislist':his,'curlist':cur})

def inc_book(request):
    bookname = request.POST.get('bookname')
    isbn = request.POST.get('isbn')
    author = request.POST.get('author')
    booktag = request.POST.get('booktag')
    publisher = request.POST.get('publisher')
    stock = request.POST.get('stock')
    bookdf,flag = book.incBook(bookname,isbn,author,booktag,publisher,stock)
    return JsonResponse({'bookdf': bookdf,'flag': flag})

def dec_book(request):
    bookname = request.POST.get('bookname')
    isbn = request.POST.get('isbn')
    author = request.POST.get('author')
    booktag = request.POST.get('booktag')
    publisher = request.POST.get('publisher')
    stock = request.POST.get('stock')
    bookdf,flag = book.decBook(bookname,isbn,author,booktag,publisher,stock)
    return JsonResponse({'bookdf': bookdf,'flag': flag})


