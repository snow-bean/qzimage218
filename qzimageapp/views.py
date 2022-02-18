from django.shortcuts import render

# Create your views here.
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from qzimageapp.models import  QkAttr
# from qzimageapp.models import QkAttr as Photo#引入模型并命名为photo
# from PIL import Image
# import time


# Create your views here.
def index(request):
    return render(request,'qzapp/index.html')

#实例化对象
def user(request):
    list=QkAttr.objects.all()
    context={'photolist':list}
    return render(request,'qzapp/index.html',context)

#图片上传
def upload(request):
    return render(request,'qzapp/upload.html')

#处理上传文件
def doupload(request):
    i=1
    myfile_name=request.POST.get("name",None)
    myfile = request.FILES.get("img",None)
    if not myfile:
        return HttpResponse("没有上传的文件信息")
    Photo.objects.create(name=myfile_name,img_src=myfile)
    #生成上传后的文件名
    # filename = str(myfile.name.split('.')[0])+"."+myfile.name.split('.').pop()
    filename='LX'+str(i)+"."+myfile.name.split('.').pop()
    destination = open("./static/pics/"+filename,"wb+")
    for chunk in myfile.chunks(): #分块读取上传文件内容并写入目标文件
        destination.write(chunk)
    destination.close()
    # # 执行图片缩放
    # im = Image.open("./static/" + filename)
    # # 缩放到75*75(缩放后的宽高比例不变):
    # im.thumbnail((75, 75))
    # # 把缩放后的图像用jpeg格式保存:
    # im.save("./static/pics/s_" + filename, None)
    context = {'info': '图片上传成功！'}
    return render(request,"qzapp/info.html",context)
    # return HttpResponse(myfile.name+'上传成功！')

    i=i+1

#执行用户信息删除操作
def delUsers(request,uid):
    try:
        ob = Photo.objects.get(pk=uid) #获取要删除用户信息
        ob.delete() #执行删除
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"qzapp/info.html",context)

#加载修改表单，准备用户信息修改
def editUsers(request,uid):
    try:
        ob = Photo.objects.get(pk=uid) #获取要修改的用户信息
        context = {'photo':ob}
        return render(request,"qzapp/edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
        return render(request,"qzapp/info.html",context)

# 执行信息编辑操作
def updateUsers(request):
    try:
        ob = Photo.objects.get(id= request.POST['id'])
        ob.name = request.POST['name']
        ob.save()
        context = {'info':'修改成功！'}
        return render(request,"qzapp/info.html",context)
    except:
        context = {'info':'修改失败！'}
        return render(request,"qzapp/info.html",context)


