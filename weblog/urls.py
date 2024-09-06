from django.urls import path 
from .import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('abut/',views.AbutView.as_view(),name='abut'),
    path('details/<int:blog_id>/',views.DetailBlogView.as_view(),name='detail_blog'),
]
