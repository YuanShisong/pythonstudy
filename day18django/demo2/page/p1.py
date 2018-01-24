
from django.shortcuts import HttpResponse, render

def index(request):
    print('1111111')
    context = {'test': 'test for context'}
    return render(request, 'html/html1.html', context)
    # return HttpResponse('page1 ok')