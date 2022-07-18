from django.shortcuts import render

# Create your views here.
from .models import Photo

def photo_list(request):
    # 보여줄 데이터(사진)
    photos = Photo.objects.all()
    # "object list"가 관례적 이름 -> "photos" 바꿀 수 있음.
    return render(request, 'photo/list.html', {"photos": photos})