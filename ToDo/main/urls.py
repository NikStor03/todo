from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='baseview'),
    path('delete/<str:slug>', views.OnDeleteView.as_view(), name='delete'),
    path('add', views.OnAddView.as_view(), name='add_new'),
    path('info/<str:slug>', views.TodoInfoView.as_view(), name='info'),
]
