from django.contrib import admin
# from core.models import User, Follow, Blog, Author, BlogNote

# class BlogNoteInline(admin.StackedInline):
#     model = BlogNote
#     fields = ("body", "description")
#     extra = 1

# class BlogAdmin(admin.ModelAdmin):
#     list_display = ["title"]
#     inlines = [BlogNoteInline]
#     #autocomplete_fields = ("authors",)

# class FollowersInline(admin.StackedInline):
#     model = Follow
#     fk_name = "followed_user"
#     fields = ("following_user",)
#     extra = 1

# class UserAdmin(admin.ModelAdmin):
#     fields = ("username", "email", "is_superuser", "is_staff", "is_active")
#     inlines = [FollowersInline]

# class AuthorAdmin(admin.ModelAdmin):
#     search_fields = ("name",)


# # Register your models here.
# admin.site.register(User, UserAdmin)
# admin.site.register(Blog, BlogAdmin)
# admin.site.register(Author, AuthorAdmin)