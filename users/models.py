from django.db import models
from django.contrib.auth .models import AbstractUser,UserManager as DjangoUserManager

class UserManager(DjangoUserManager):
    def _create_user(self, username,  email=None, password=None, **extra_fields):
        if not password:
            raise ValueError('비밀번호는 필수 값입니다.')
        if not username:
            raise ValueError('아이디는 필수 값입니다.')
        
        user = self.model(username=username,email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username,image=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(username,email,password,**extra_fields)
    
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(username,email,password,**extra_fields)
    
class User(AbstractUser):
    image = models.ImageField(verbose_name = '이미지',null=True,blank = True)
    objects = UserManager()