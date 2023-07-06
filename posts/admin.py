from django.contrib import admin


from .models import Post, Selection, Comment

@admin.register(Post)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'writer')
    pass

@admin.register(Selection)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('post', 'content')
    pass

@admin.register(Comment)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('post', 'content', 'writer')
    pass