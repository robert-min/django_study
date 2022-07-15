from django.shortcuts import render

# Create your views here.
# CRUD : CREATE, READ, UPDATE, DELETE

# List page(Read)
# 클래스형 뷰, 함수형 뷰
# 웹 페이지 접속 -> 페이지 본다.(URL 입력 -> 웹서버가 뷰를 찾아서 동작 -> 응답)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = "_create"

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = "_update"

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')