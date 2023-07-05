from django.contrib import admin


from .models import Post, Selection, Comment

@admin.register(Post)
class UserModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Selection)
class UserModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class UserModelAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Post)
# admin.site.register(Selection)
# admin.site.register(Comment)