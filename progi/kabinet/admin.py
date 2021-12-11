#  kabinet/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import User, Status, Adres, UserProfile

class MyUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'zametka']


admin.site.register(User, MyUserAdmin)


class StatusAdmin(admin.ModelAdmin):
    model = Status
    list_display = ['title', 'is_activ']


admin.site.register(Status, StatusAdmin)


class AdresAdmin(admin.ModelAdmin):
    model = Adres
    exclude = []
    readonly_fields = ["slug"]
    list_display = ['raion', 'gorod', 'slug']
    save_on_top = True  # В админке появляется сверху блок из трех кнопок дублирует нижний блок с кнопкой сохранить

admin.site.register(Adres, AdresAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ['name', 'get_img', 'avatar']

    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" width="50">')


admin.site.register(UserProfile, UserProfileAdmin)

