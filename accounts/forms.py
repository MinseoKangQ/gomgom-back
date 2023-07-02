#accounts/forms
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
class UserBaseForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields='__all__'

#회원가입 폼
class signupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username','image']