from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.

User = get_user_model()
CHOICES = (
        ('전체','전체'),
        ('대인관계','대인관계'),
        ('연애','연애'),
        ('교육','교육'),
        ('생활','생활'),
        ('건강','건강'),
        ('반려동물','반려동물'),
        ('여행','여행'),
        ('쇼핑','쇼핑'),
        ('기타','기타'),
)

class Post(models.Model):
    title = models.TextField(verbose_name='질문제목')
    image = models.ImageField(verbose_name='이미지',null=True, blank=True)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일',default=timezone.now)
    view_count = models.IntegerField(verbose_name='조회수',blank=True, default = 0)
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
    all_voted_count = models.IntegerField(verbose_name = '투표 참여 수', default = 0)
    category = models.CharField(max_length=20, choices=CHOICES,default='기타' )
    like = models.ManyToManyField(User,related_name='likes',blank=True)
    
    
    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False

class Comment(models.Model):
    image = models.ImageField(verbose_name = '이미지',null=True,blank = True)
    content= models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일',default=timezone.now)
    post=models.ForeignKey(to='Post',on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
    
    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False
        
    
class Selection(models.Model):
    image=models.ImageField(verbose_name = '이미지',null=True,blank = True)
    content = models.CharField(verbose_name='내용',max_length=100)
    vote = models.CharField(verbose_name = '투표율', default = "0%", max_length = 10)
    each_voted_count = models.IntegerField(verbose_name = '선택지 투표 참여 수', default = 0)
    post = models.ForeignKey(to='Post',on_delete=models.CASCADE,null=True,blank=True)