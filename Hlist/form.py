from django import forms
from .models import memo
# 모델클래스 GuessNumbers로 부터 데이터를 입력 받을 폼을 작성한다.

class postmemo(forms.ModelForm): #forms의 ModelForm 클래스를 상속 받는다.

    class Meta:
        model = memo #GuessNumbers와 연결
        fields = ('memotitle', 'memotext') # 그 중에 입력 받을 것