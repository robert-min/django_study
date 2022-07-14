from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    html = "<html><body>hello</body></html>"
    return HttpResponse(html)

def welcome(request):
    html = "<html><body>Welcome to django</body></html>"
    return HttpResponse(html)

def template_test(request):
    # 기본 템플릿 폴더
    # 1.admin, 2. 각 앱의 폴더에 있는 templates 폴더, 3. 설정한 폴더
    return render(request, 'test.html')