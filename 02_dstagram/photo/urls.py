from django.urls import path

from .views import *
# 2차 URL 파일
app_name = "photo"

urlpatterns = [
    # class형은 as_view, 함수형은 바로 사용
    path('', photo_list, name="photo_list"),
    path('upload/', PhotoUploadView.as_view(), name="photo_upload"),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name="photo_delete"),
]