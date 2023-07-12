from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Selection, Comment
from .forms import PostCreateForm, CommentForm
from django.core.paginator import Paginator
from django.http import JsonResponse


@login_required(login_url='/accounts/login/')
def post_create_form_view(request,selection_count=2):
    if request.method=='GET':
        form = PostCreateForm()
        context = {'form':form}
        return render(request,'posts/post-create-form-view.html',context)
    if request.method=='POST':
        title = request.POST.get('post_title')
        content = request.POST.get('post_content')
        writer = request.user
        category = request.POST.get('post_category')
            
        post = Post.objects.create(
            title = title,
            content = content,
            writer = writer,
            category = category,
        )
        post.save()
                
        image1 = request.FILES.get('selection_image1')
        content1 = request.POST.get('selection_content1') 
        image2 = request.FILES.get('selection_image2')
        content2 = request.POST.get('selection_content2')
        
        Selection.objects.create(
            image = image1,
            content = content1,
            post=post,
        )
        Selection.objects.create(
            image = image2,
            content = content2,
            post=post,
        )
    else:
        return render(request, 'posts/post-create-complete.html')
    return render(request, 'posts/post-create-complete.html')
                
                
                
                #post = Post.objects.create(
                #    title = form.cleaned_data['title'],
                #    content=form.cleaned_data['content'],
                #    writer=request.user,
                #    category = form.cleaned_data['category'],
                #)
                #post.save()
                #Selection.objects.create(
                #    image = form.cleaned_data['image1'],
                #    content = form.cleaned_data['selection_content1'],
                #    post=post
                #)
                #Selection.objects.create(
                #    image = form.cleaned_data['image2'],
                #    content = form.cleaned_data['selection_content2'],
                #    post=post
                #)
            #else:
                # return redirect('/admin')
            #    return render(request, 'posts/post-create-complete.html')
            #return render(request, 'posts/post-create-complete.html')
            # return redirect('/admin')

@login_required
def post_list_view(request):
    if request.method == 'GET':
        selected_category = request.GET.get('category') 
        post_list = Post.objects.all() # Post 전체 데이터 조회
        
        if selected_category is None: # 처음에 버튼 선택 안할시, queryset 데이터에 아무것도 없음.
            selected_category = '대인관계'  # 그래서 디폴트 값은 대인관계로 설정
            
        print(selected_category)
        filter_list = Post.objects.filter(category=selected_category).order_by('-created_at') # 사용자가 선택한 카테고리와 같은것만 필터링
        selection_list = Selection.objects.all()
        
        paginator = Paginator(filter_list, 8)  # 한 페이지에 8개의 게시글 표시
        page_number = request.GET.get('page')  # 현재 페이지 번호 가져오기
        page_obj = paginator.get_page(page_number)  # 현재 페이지의 게시글 객체 가져오기
        
        context = {
            'post_list': post_list,
            'selection_list': selection_list,
            'filter_list': page_obj,  # 페이지 객체를 전달
            'selected_category': selected_category,
        }
        return render(request, 'posts/post-list-all.html', context)
    
# 상세 목록 보기
@login_required
def post_detail_view(request, id):
    post = Post.objects.get(id=id)
    
    # 요청이 GET인 경우
    if request.method == 'GET':
        # 로그인이 안된 상태라면
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        # 로그인이 된 상태라면
        else:
            param = request.GET.get('param')
            selections = Selection.objects.filter(post=post)
            
            if param == "1" or param == "2":
                post.all_voted_count += 1
                post.save()
                first_selection = selections.first()
                second_selection = selections[1]
                
                if param == "1":
                    if first_selection and param == "1":
                        first_selection.each_voted_count += 1
                        first_selection.save()

                    total_voted_count = post.all_voted_count
                    first_selection_voted_count = first_selection.each_voted_count if first_selection else 0
                    second_selection_voted_count = selections[1].each_voted_count if len(selections) > 1 else 0
                    
                    # Calculate vote percentages
                    first_selection_vote_percentage = int((first_selection_voted_count / total_voted_count) * 100) if total_voted_count != 0 else 0
                    second_selection_vote_percentage = int((second_selection_voted_count / total_voted_count) * 100) if total_voted_count != 0 else 0
                    
                    if first_selection:
                        first_selection.vote = f'{first_selection_vote_percentage}%'
                        second_selection.vote = f'{second_selection_vote_percentage}%'
                        first_selection.save()
                        second_selection.save()
                
                elif param == "2":
                    if second_selection and param == "2":
                        second_selection.each_voted_count += 1
                        second_selection.save()

                    total_voted_count = post.all_voted_count
                    first_selection_voted_count = first_selection.each_voted_count if first_selection else 0
                    second_selection_voted_count = selections[1].each_voted_count if len(selections) > 1 else 0
                    
                    # Calculate vote percentages
                    first_selection_vote_percentage = int((first_selection_voted_count / total_voted_count) * 100) if total_voted_count != 0 else 0
                    second_selection_vote_percentage = int((second_selection_voted_count / total_voted_count) * 100) if total_voted_count != 0 else 0
                    
                    if second_selection:
                        first_selection.vote = f'{first_selection_vote_percentage}%'
                        second_selection.vote = f'{second_selection_vote_percentage}%'
                        first_selection.save()
                        second_selection.save()
                        
            context = {
            'post' : post,
            'comment_form' : CommentForm(),
        }
        return render(request, 'posts/post-detail-view.html', context)
    # 요청이 POST인 경우
    if request.method == 'POST':
        # 댓글 작성
        # 로그인이 안된 상태라면
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        # 로그인이 된 상태라면
        else:
            post = Post.objects.get(id=id)
            image = request.FILES.get('file_field_name')  # 파일 필드에 대한 값 가져오기
            content = request.POST.get('text_field_name')  # 텍스트 필드에 대한 값 가져오기
            #댓글 이미지와 내용이 전부 존재할 경우, 
            if image and content:
                comment = Comment.objects.create(
                    image=image,
                    content=content,
                    post=post,
                    writer=request.user,
                )
            # 댓글 내용만 존재할 경우,
            elif content:
                comment = Comment.objects.create(
                    content = content,
                    post=post,
                    writer=request.user,
                )
            else: # 댓글 이미지와, 내용이 없을 경우,
                return render(request, 'posts/post-detail-view.html')
            context = {
                    'post': post,
            }
            return render(request, 'posts/post-detail-view.html', context)            
    return render(request, 'posts/post-detail-view.html')   

@login_required
def post_create_complete(request):
    return redirect('posts:post-create-complete')

# 곰곰이의 고민 상세 보기
@login_required
def post_gomgom_detail_view(request, id):
    post = Post.objects.get(id=id)
    
    # 요청이 GET인 경우
    if request.method == 'GET':
        # 로그인이 안된 상태라면
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        # 로그인이 된 상태라면
        else:
            context = {
            'post' : post,
            'comment_form' : CommentForm(),
        }
        return render(request, 'posts/post-detail-today-question.html', context)
    
    # 요청이 POST인 경우
    if request.method == 'POST':
        # 댓글 작성
        # 로그인이 안된 상태라면
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        # 로그인이 된 상태라면
        else:
            post = Post.objects.get(id=id)
            image = request.FILES.get('file_field_name')  # 파일 필드에 대한 값 가져오기
            content = request.POST.get('text_field_name')  # 텍스트 필드에 대한 값 가져오기
            #댓글 이미지와 내용이 전부 존재할 경우, 
            if image and content:
                comment = Comment.objects.create(
                    image=image,
                    content=content,
                    post=post,
                    writer=request.user,
                )
            # 댓글 내용만 존재할 경우,
            elif content:
                comment = Comment.objects.create(
                    content = content,
                    post=post,
                    writer=request.user,
                )
            else: # 댓글 이미지와, 내용이 없을 경우,
                return render(request, 'posts/post-detail-today-question.html')
            context = {
                    'post': post,
            }
            return render(request, 'posts/post-detail-today-question.html', context)            
    return render(request, 'posts/post-detail-today-question.html')