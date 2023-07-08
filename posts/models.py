from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
CHOICES = (
        ('1','대인관계'),
        ('2','연애'),
        ('3','교육'),
        ('4','생활'),
        ('5','건강'),
        ('6','반려동물'),
        ('7','여행'),
        ('8','쇼핑'),
        ('9','기타'),
)

class Post(models.Model):
    title = models.TextField(verbose_name='질문제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일',auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수',blank=True, default = 0)
    heart_count = models.IntegerField(verbose_name='공감수',blank=True, default = 0)
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=20, choices=CHOICES,default='기타' )


class Comment(models.Model):
    image = models.ImageField(verbose_name = '이미지',null=True,blank = True)
    content= models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일',auto_now_add=True)
    post=models.ForeignKey(to='Post',on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
    
class Selection(models.Model):
    image=models.ImageField(verbose_name = '이미지',null=True,blank = True)
    content = models.CharField(verbose_name='내용',max_length=100)
    post = models.ForeignKey(to='Post',on_delete=models.CASCADE,null=True,blank=True)

class Vote(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    post = models.ForeignKey(to='Post',on_delete=models.CASCADE)
    selection = models.ForeignKey(Selection,on_delete=models.CASCADE)
    