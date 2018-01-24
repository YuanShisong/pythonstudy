from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse, render, redirect


def view1(request):
    return HttpResponse('This is view1.')


def login(request):
    # # 1/ 直接打开文件然后将login.html文件流写如到前台
    # f = open('html/login.html', 'r', encoding='utf-8')
    # data = f.read()
    # f.close()
    # return HttpResponse(data)

    # # 2/ 通过render直接渲染login.html
    # return render(request, 'login.html')

    # 3/ 用户名 密码 认证
    # 如果是GET请求，跳转到login.html页面
    # 如果时POST请求，验证用户名密码 正确则跳转到百度 错误给出提示
    err_msg = ''
    if request.method == 'POST':
        name = request.POST.get('username', None)  # 如果username为空则name为None
        pwd = request.POST.get('password', None)
        # print(name, pwd)
        if name == 'root' and pwd == 'root':
            # return redirect('http://www.baidu.com')
            return redirect('/home')
        else:
            err_msg = '用户名或密码错误'
    return render(request, 'login.html', {'err_msg': err_msg})


USER_LIST = [
    {'name': 'joshua', 'age': 30, 'gender': 'male'},
    {'name': 'monica', 'age': 20, 'gender': 'female'},
    {'name': 'ross', 'age': 30, 'gender': 'male'},
]


def home(request):
    if request.method == 'POST':
        n = request.POST.get('name', None)
        a = request.POST.get('age', None)
        g = request.POST.get('gender', None)
        print(n, a, g)
        tmp = {'name': n, 'age': a, 'gender': g}
        USER_LIST.append(tmp)

    return render(request, 'home.html', {'user_list': USER_LIST})