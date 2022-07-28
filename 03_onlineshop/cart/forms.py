from django import forms

# 사용자 클라이언트 화면에 입력폼을 만들어줄 때,
# 클라이언트에 입력한 데이터에 대한 전처리

class AddProductForm(forms.Form):
    quantity = forms.IntegerField()
    # boolfield는 required flase로
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

