from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('journals/', views.JournalList.as_view(), name='journal_list'),
    path('journals/<int:pk>', views.JournalDetail.as_view(), name='journal_detail'),
    path('entries/', views.EntryList.as_view(), name='entry_list'),
    path('entries/<int:pk>', views.EntryDetail.as_view(), name='entry_detail'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
]