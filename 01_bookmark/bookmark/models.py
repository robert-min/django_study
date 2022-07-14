from django.db import models

# Create your models here.
class Bookmark(models.Model):
    # 필드의 종류가 결정
    ## 1. 데이터베이스 컬럼 종류
    ## 2. 제약 사항
    ## 3. Form의 종류, Form에서 제약사항 결정
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    # 모델을 생성 => 데이터베이스에 어떤 데이터를 넣을지 결정
    # makemigrations => 모델의 변경사항을 추적해서 기록
    # 마이그레이션 => 데이터베이스에 모델의 내용을 반영

    # 목록에 이름 추가
    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url

