from django import forms
from .models import UploadFileModel, EtcUploadFileModel
from django.contrib.auth.hashers import check_password
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class LoginForm(forms.Form):
    username = forms.CharField(error_messages={
        'required':'아이디를 입력하세요!'
    },max_length=100, label="사용자이름")
    password = forms.CharField(error_messages={
        'required':'비밀번호를 입력하세요!'
    },widget=forms.PasswordInput, max_length=100, label="비밀번호")
    # 처음 값이 들어왔다 는 검증 진행
    
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ['file','Ubody','title']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'Ubody': forms.CharField(widget=CKEditorUploadingWidget()),
        }
    
class EtcUploadFileForm(forms.ModelForm):
    class Meta:
        model = EtcUploadFileModel
        fields = ['file','Ubody','title']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'Ubody': forms.CharField(widget=CKEditorUploadingWidget()),
        }
    