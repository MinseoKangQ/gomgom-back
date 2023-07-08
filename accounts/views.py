
from django.contrib.auth import logout,login
from django.shortcuts import redirect,render
from accounts.forms import signupForm
from django.contrib.auth.forms import AuthenticationForm
from posts.models import Post
from users.models import models
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required

# 완성

# signup - GET 요청
def signup_view(request):
    #GET 요청시, 회원 가입 HTML render
    if request.method=='GET':
        form = signupForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
    #POST 요청으로 정보 가져옴 & 회원 생성    
        form = signupForm(request.POST,request.FILES)
        if form.is_valid():
            #이미지가 존재한다면, 이미지 저장 필요
            image = form.cleaned_data['image']
            #유효성 처리 후 회원 생성
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                print("비밀번호 값이 다릅니다.!!")
                return redirect('accounts:gomgom')
            instance = form.save()
            #회원가입이 성공하면 로그인 페이지로 이동
            return redirect('accounts:login')
        else:
            #회원가입이 실패하면 다시 회원가입 페이지로 이동
            return redirect('accounts:signup')
    
    
#login - GET 요청
def login_view(request):
    if request.method=='GET':
        #GET 요청시 로그인 페이지 내보냄
        return render(request,'accounts/login.html',{'form':CustomAuthenticationForm()})
    else:
        #개인정보는 post 요청으로 받아옴 (CustomAuthenticationForm으로..)
        form = CustomAuthenticationForm(request,data=request.POST)
        #비지니스 로직
        if form.is_valid():
            login(request,form.user_cache)
            #로그인 성공시 홈 페이지로 이동      ** 추후에 설정 필요함! **
            return redirect('gomgom:home') #확인용으로 redirect 작성
        else: #비지니스 로직 실패 ( 로그인 실패 )
            return render(request,'accounts/login.html',{'form':CustomAuthenticationForm()})
        


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    #로그아웃 시, 그냥 홈페이지로 이동 redirect  ** 추후에 설정 필요함! **
    return redirect('gomgom:home')

@login_required
def mypage_view(request):
    if request.method == 'GET':
        post_list = Post.objects.filter(writer = request.user) # Post.writer 가 현재 로그인인 것 조회
        context = {
            'post_list' : post_list,
        }
        return render(request, 'accounts/mypage.html', context)