from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Selection, Comment
from .forms import PostBaseForm,PostCreateForm,SelectionAddForm2, SelectionAddForm3
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
            if selection_count == 3:
                form = SelectionAddForm2(request.POST,request.FILES)
            elif selection_count == 4:
                form = SelectionAddForm3(request.POST,request.FILES)
                
            if form.is_valid():
                post = Post.objects.create(
                    title = form.cleaned_data['title'],
                    content=form.cleaned_data['content'],
                    writer=request.user,
                )
                for selectionnum in range(selection_count):
                    imagename = 'image'+str(selectionnum+1)
                    contentname='selection_content'+str(selectionnum+1)
                    Selection.objects.create(
                        image = form.cleaned_data[imagename],
                        content = form.cleaned_data[contentname],
                        post=post
                    )
            else:
                return redirect('/admin')
            return redirect('/admin')
        elif 'selection' in request.POST:
            if selection_count == 2:
                selection_count =3
                form = SelectionAddForm2()
                context = {'form':form}
                return render(request,'posts/post-create-form-view.html',context)
            elif selection_count ==3 :
                selection_count =4
                form = SelectionAddForm3()
                return render(request,'posts/post-create-form-view.html',context)
    
@login_required
def post_list_view(request):
    post_list = Post.objects.all() # Post 전체 데이터 조회
    # comment_list = Comment.objects.all()
    comment_list = Comment.objects.all()
    # post_list = Post.objects.filter(writer = request.user) # Post.writer 가 현재 로그인인 것 조회
    context = {
        'post_list' : post_list,
        'comment_list' : comment_list,
    }
    return render(request, 'posts/post-list.html', context)