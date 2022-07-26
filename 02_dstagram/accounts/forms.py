from django.contrib.auth.models import User
from django import forms

# form : form tag -> html tag 프론트에서 사용자의 입력을 받는 인터페이스
# 장고 form : html form 역할, 데이터베이스에 저장할 내용을 형식, 제약조건 설정
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def clean_password2(self):  # 해당 필드에대한 validation을 어떻게 할건지(clean_필드명)
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Password not match!!")
        return cd["password2"]  #  해당 필드의 데이터를 리턴하는 것이 관례

