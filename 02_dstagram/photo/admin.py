from django.contrib import admin

# Register your models here.
from .models import Photo
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "created", "updated"]
    # Forien key 필드는 raw id fields 설정 권장
    raw_id_fields = ["author"]
    list_filter = ["created", "updated", "author"]
    # searchfield는 text로 볼 수 있는 거만 검색가능 author X -> author__username
    search_fields = ["text", "created", "author__username"]
    # 1. updated기준 내림차순 -> 2. 생성일 기준 내림차순
    ordering = ["-updated", "-created"]

admin.site.register(Photo, PhotoAdmin)