from django import forms
from .models import Selection,Post        
class PostBaseForm(forms.ModelForm):
    #모델 폼 상속 시 클래스 더 적어주어야 됨
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateForm(PostBaseForm):
    CATEGORY_CHOICES=[
        ('1','대인관계'),
        ('2','연애'),
        ('3','교육'),
        ('4','생활'),
        ('5','건강'),
        ('6','반려동물'),
        ('7','여행'),
        ('8','쇼핑'),
        ('9','기타'),
    ]
    #선택지1
    image1=forms.ImageField(label = '이미지')
    selection_content1=forms.CharField(label = '선택지 내용',max_length=20)
    #선택지2
    image2=forms.ImageField(label = '이미지')
    selection_content2=forms.CharField(label = '선택지 내용',max_length=20)
    
    category = forms.ChoiceField(label='카테고리',choices= CATEGORY_CHOICES)
    class Meta(PostBaseForm.Meta):
        fields = ['title','content']
    