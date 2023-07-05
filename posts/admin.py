from django.contrib import admin


from .models import Post,Selection

@admin.register(Post)
class UserModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Selection)
class UserModelAdmin(admin.ModelAdmin):
    pass