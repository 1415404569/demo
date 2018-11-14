from django.core.serializers import json
from django.shortcuts import render, redirect
from Threat_Search import models
import re,os
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.

# def myview(_request):
#   response = HttpResponse(json.dumps({"key": "value", "key2": "value"}))
#   response["Access-Control-Allow-Origin"] = "*"
#   response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
#   response["Access-Control-Max-Age"] = "1000"
#   response["Access-Control-Allow-Headers"] = "*"
#   return response

def html_index2(request):
    API = 'adfs121d61f56s1df65as1f1dsa1adf3s213f21sda1f'
    print(API)
    if API == request.POST.get("msgs") or API == request.GET.get("msgs"):
        if request.method == 'GET':
            # 获取前台输入的数据
            search=request.GET.get('search-index')
            # 判断输入的哈希值是否符合规范
            if len(search) in (32,40,64):
                # 用前台数据进行查询
                try:
                    contact = models.hash_md5.objects.get(hash_id=search)
                    print(contact)
                    print("*************************************")
                    # 对杀毒软件和标签进行拆分，并生成数组
                    source_list=contact.software.split(",")
                    tag_list = contact.tag.split(",")
                    time_list = str(contact.time)
                    print(source_list)
                    print(tag_list)
                    print(time_list)
                    # 把杀毒软件和相应标签调到一个元组里 [[],[],[]]
                    list=[]
                    for i in range(0,len(source_list)):
                        list.append([source_list[i],tag_list[i],time_list])
                    print(list)

                    #服务端的传数据
                    # return render(request,'home/search_result.html',{"contact":contact,"source_list":source_list,"tag_list":tag_list,"list":list})


                    str_json = str({"contact": contact.hash_id,"source_list": source_list, "tag_list": tag_list, "list": list})
                    print(str_json)
                    print(list)
                    return HttpResponse(str_json)
                except Exception:
                    return HttpResponse("没有结果")
            else:
                print('输入错误')
                return render(request, 'home/index.html')
    else:
        return HttpResponse("error")
def html_index(request):
    return render(request,'home/index.html')

def serach_result(request):

    return render(request,'home/search_result.html',{"search":request.GET.get("parm")})
def vt_api(request):
    search_data = request.GET.get('search')

    if search_data:
        vt_url = 'https://www.virustotal.com/#/search/%s'%search_data
        # return render(request, 'vt_api/vt_search.html',{'vt_url':vt_url})
        return redirect(vt_url)
    return render(request, 'vt_api/vt_search.html')


'''
https://www.virustotal.com/#/ip-address/8.8.8.8
https://www.virustotal.com/#/url/92f3cb0d6d7b5fc290b08e73797cb58bccf4fcbbbf8ec66fad5b90af2c86edde/detection
https://www.virustotal.com/#/domain/topsec.com.cn
https://www.virustotal.com/#/file/b963223d3f39884ebed3e647390e55d8de86c7e3c5daaae6509379a6fc3ba97e/detection
https://www.virustotal.com/#/search/*******
'''
def test(request):
    return redirect('https://www.baidu.com')
def seek(request):
    # return redirect('')
    return render(request, "home/search_result.html")
def login(request):
    return render(request,"home/login.html")
def zhuce(request):
    return render(request,'home/login.html',{"msg":1})
def add(request):
    print("**************************")
    obj = request.FILES.get('file_name')
    print(obj.name)
    path = default_storage.save('static/home/img/'+obj.name,ContentFile(obj.read()))

    # tmp_file = os.path.join(settings.MEDIA_ROO   print(path)T,path)
    return HttpResponse('<script type="text/javascript">alert("上传成功");location.href="http://127.0.0.1:8000/"</script>')