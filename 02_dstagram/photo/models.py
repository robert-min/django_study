from django.db import models

# Create your models here.

# 1. 모델 : 데이터베이스에 저장될 데이터가 있다면 해당 데이터를 묘사.
# 2. 뷰(기능) : 계산, 처리 - 실제 기능 or 화면
# 3. URL 맵핑 : 라우팅 테이블에 기록
# 4. 화면에 보여줄 것이 있는 경우 -> 템플릿 작성(html or json 등등)

# 장고의 기본 유저 모델
from django.contrib.auth.models import User
from django.urls import reverse

# ForeignKey : 외래키
# PrimaryKey : 주키
class Photo(models.Model):
    # default 값이 없으면 무조건 입력해야 하는 걸로 변경
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # makemigrations -> migrate : 데이터베이스 적용
    class meta:
        ordering = ['-updated']

    # 인스턴스를 프린트하거나 관리자 페이지에서 프린트할 때
    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])