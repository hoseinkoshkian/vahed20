# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # فیلدهایی که در لیست کاربران نمایش داده می‌شوند
    list_display = ('phone_number', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')

    # فیلدهایی که می‌توان در آن‌ها جستجو کرد
    search_fields = ('phone_number', 'first_name', 'last_name', 'email')

    # ترتیب نمایش کاربران (بر اساس شماره تلفن)
    ordering = ('phone_number',)

    # تنظیمات فرم ویرایش کاربر
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'email')}),
        ('دسترسی‌ها', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('تاریخ‌های مهم', {'fields': ('last_login', 'date_joined')}),
    )

    # تنظیمات فرم افزودن کاربر
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )

    # فیلترهای سمت راست صفحه
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

# ثبت مدل کاربر با کلاس UserAdmin شخصی‌سازی شده
admin.site.register(User, CustomUserAdmin)