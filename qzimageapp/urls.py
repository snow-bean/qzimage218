from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index,name='index'),
    path('',views.user,name='user'),
    path('upload/',views.upload,name='upload'),#上传图片
    path('doupload/',views.doupload,name='doupload'),
    path('user/<str:uid>/del', views.delUsers, name="delusers"), #执行用户信息删除
    # path('user/<int:uid>/del', views.delUsers, name="delusers"), #执行用户信息删除
    path('user/<str:uid>/edit', views.editUsers, name="editusers"), #加载用户信息编辑表单
    path('user/update/', views.updateUsers, name="updateusers"), #执行用户信息编辑
]
