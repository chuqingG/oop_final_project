from django.conf.urls import url
from django.urls import path
from WebServer import views

urlpatterns = [
    url(r'^home$', views.home),
    path('admin/', views.admin, name='admin'),
    path('reader/', views.reader, name='reader'),
    url(r'^import_book$', views.import_book, name='import_book'),
    url(r'^add_book$', views.add_book, name='add_book'),
    url(r'^del_book$', views.del_book, name='del_book'),
    url(r'^mod_book$', views.mod_book, name='mod_book'),
    url(r'^search_book$', views.search_book, name='search_book'),
    url(r'^inc_book$', views.inc_book, name='inc_book'),
    url(r'^dec_book$', views.dec_book, name='dec_book'),
    url(r'^import_user$', views.import_user, name='import_user'),
    url(r'^add_user$', views.add_user, name='add_user'),
    url(r'^del_user$', views.del_user, name='del_user'),
    url(r'^mod_user$', views.mod_user, name='mod_user'),
    url(r'^search_user$', views.search_user, name='search_user'),
    url(r'^search_his$', views.search_his, name='search_his'),
    url(r'^user_confirm$', views.user_confirm, name='user_comfirm'),
    url(r'^borrow_book$', views.borrow_book, name='borrow_book'),
    url(r'^return_book$', views.return_book, name='return_book'),
    
]
