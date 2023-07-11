#accounts/forms
from django.contrib.auth import get_user_model
from django.forms import TextInput, PasswordInput,FileInput
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# 완성

class UserBaseForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields='__all__'

#회원가입 폼
class signupForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        initial='',
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': '아이디를 입력하세요.'
        })
    )
    password1 = forms.CharField(
        label='비밀번호',
        initial='',
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '비밀번호를 입력하세요.'
        })
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        initial='',
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '비밀번호를 다시 입력하세요.'
        })
    )
    image = forms.ImageField(
        label='이미지',
        required=False,
        widget=FileInput(attrs={
            'class':'form-image',
            'placeholder':'프로필 사진을 업로드'
        }),
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['image','username', 'password1', 'password2']
        
# 로그인 폼
class CustomAuthenticationForm(AuthenticationForm):
    
    username = forms.CharField(
        label='',
        initial='',
        widget=TextInput(attrs={
            'class': 'login-form-username',
            'placeholder': '아이디를 입력하세요.'
        })
    )
    password = forms.CharField(
        label='',
        initial='',
        widget=PasswordInput(attrs={
            'class': 'login-form-password',
            'placeholder': '비밀번호를 입력하세요.'
        })
    )