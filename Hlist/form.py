from django import forms
from .models import memo
from django.contrib.auth.hashers import check_password
from django import forms
# 모델클래스 GuessNumbers로 부터 데이터를 입력 받을 폼을 작성한다.

class postmemo(forms.ModelForm): #forms의 ModelForm 클래스를 상속 받는다.
    class Meta:
        model = memo #GuessNumbers와 연결
        fields = ('memotitle', 'memotext') # 그 중에 입력 받을 것
        
class LoginForm(forms.Form):
    username = forms.CharField(error_messages={
        'required':'아이디를 입력하세요!'
    },max_length=100, label="사용자이름")
    password = forms.CharField(error_messages={
        'required':'비밀번호를 입력하세요!'
    },widget=forms.PasswordInput, max_length=100, label="비밀번호")
    # 처음 값이 들어왔다 는 검증 진행

