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

def open_file(request):
    path = request.POST.get('path')
    path = neobase.convert_path(path,
                                settings.fuse_process.fuse_obj.root,
                                settings.fuse_process.fuse_obj.mount_point)
    ok = True
    if not os.access(path, os.F_OK):
        ok = False
    os.system("nohup xdg-open {}".format(path))
    return JsonResponse({'ok': ok})


def rm_file(request):
    path = request.POST.get('path')
    path = neobase.convert_path(path,
                                settings.fuse_process.fuse_obj.root,
                                settings.fuse_process.fuse_obj.mount_point)
    os.system("rm {}".format(path))
    return find_files(request)


def rm_node(request):
    path = request.POST.get('path')
    graph = Graph("bolt://localhost:7687")
    ok = True
    if not neobase.delete_file(graph, path):
        ok = False
    return JsonResponse({'ok': ok})


def choose_dir(request):
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    root.destroy()
    print(path)
    return JsonResponse({'path': path})


def add_files(request):
    root = tk.Tk()
    root.withdraw()
    paths = filedialog.askopenfilenames()
    root.destroy()
    for path in paths:
        full_path = os.path.realpath(settings.fuse_process.fuse_obj.mount_point + '/' + os.path.realpath(path))
        print('\n\n', full_path, '\n\n')
        os.makedirs(os.path.dirname(full_path))
        os.system('cp {} {}'.format(path, full_path))

    return JsonResponse({'paths': paths})


def umount(request):
    print(umount)
    try:
        if type(settings.fuse_process) == settings.FuseProcess:
            settings.fuse_process.terminate()
            os.system("umount {}".format(settings.fuse_process.mount_path))
    except AttributeError:
        pass
    return render(request, 'home.html')


def add_folder(request):
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    root.destroy()
    os.system('cp -r {} {}'.format(path, settings.fuse_process.fuse_obj.mount_point))
    return JsonResponse({'paths': path})
