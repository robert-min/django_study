from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.
# CRUD
# CREATE Update -> 입력받을 폼 html form tag

def register(request):
    if request.method == "POST":
        # 회원가입 데이터 입력 완료
        user_form = RegisterForm(request.POST)  # 사용자가 입력한 값0
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(request, "registration/register_done.html", {"new_user": new_user})
    else:
        # 회원 가입 내용을 입력하는 상황
        user_form = RegisterForm()
    return render(request, "registration/register.html", {"form": user_form})