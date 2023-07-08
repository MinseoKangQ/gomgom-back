from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Selection, Comment
from .forms import PostBaseForm,PostCreateForm
from django import forms

# Create your views here.


@login_required(login_url='/accounts/login/')
def post_create_form_view(request,selection_count=2):
    if request.method=='GET':
        selection_count+=1
        form = PostCreateForm()
        context = {'form':form}
        return render(request,'posts/post-create-form-view.html',context)
    if request.method=='POST':
        if 'post' in request.POST:
            form = PostCreateForm(request.POST,request.FILES)
            if form.is_valid():
                post = Post.objects.create(
                    title = form.cleaned_data['title'],
                    content=form.cleaned_data['content'],
                    writer=request.user,
                    category = form.cleaned_data['category'],
                )
                Selection.objects.create(
                    image = form.cleaned_data['image1'],
                    content = form.cleaned_data['selection_content1'],
                    post=post
                )
                Selection.objects.create(
                    image = form.cleaned_data['image2'],
                    content = form.cleaned_data['selection_content2'],
                    post=post
                )
            else:
                return redirect('/admin')
            return redirect('/admin')

@login_required
def post_list_view(request):
    post_list = Post.objects.all() # Post 전체 데이터 조회
    # comment_list = Comment.objects.all()
    comment_list = Comment.objects.all()
    # post_list = Post.objects.filter(writer = request.user) # Post.writer 가 현재 로그인인 것 조회
    selection_list=Selection.objects.all()
    context = {
        'post_list' : post_list,
        'comment_list' : comment_list,
        'selection_list': selection_list,
    }
    return render(request, 'posts/post-list-all.html', context)

# 상세 목록 보기
@login_required
def post_detail_view(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'GET':
        # 로그인이 안된 상태라면
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        # 로그인이 된 상태라면
        else:
            context = {
            'post' : post,
        }
        
        return render(request, 'posts/post-detail.html', context)