from django.contrib import admin

from .models import PayFor, PayItem

# Register your models here.


# class CustomUserAdmin(UserAdmin):
#     # 「ユーザー名とパスワードを登録してください。・・・」の文言を非表示にする#
#     add_form_template = None
#     # 表示項目から'username'を削除して 'email'に変更
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal info', {'fields': ('first_name','last_name')})),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('email', 'first_name', 'last_name', 'is_staff')
#     search_fields = ('first_name', 'last_name', 'email')
#     ordering = ('email',)
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
#

admin.site.register(PayFor)
admin.site.register(PayItem)