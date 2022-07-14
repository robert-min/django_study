from django.contrib import admin

# Register your models here.
from .models import Bookmark

# 모델에 등록하고 볼 수 있도록 함
admin.site.register(Bookmark)