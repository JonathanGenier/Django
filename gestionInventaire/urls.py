from django.conf.urls import url
from .views import (indexView, loginView, logoutView, registerView, productView, salesView, addView, editView, deleteView)

urlpatterns = [
    url(r'^$', indexView, name='index'),
    url(r'^login$', loginView, name='login'),
    url(r'^logout$', logoutView, name='logout'),
    url(r'^register$', registerView, name='register'),
    url(r'^product/(?P<pk>\d+)$', productView, name='product'),
    url(r'^sales$', salesView, name='sales'),
    url(r'^add$', addView, name='add'),
    url(r'^edit/(?P<pk>\d+)$', editView, name='edit'),
    url(r'^delete/(?P<pk>\d+)$', deleteView, name='delete'),
]