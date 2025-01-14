from django.contrib import admin
from .models import *

# تنظیمات برای نمایش مدل Course در ادمین
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'practical_units', 'theoretical_units')
    search_fields = ('code', 'name')
    list_filter = ('practical_units', 'theoretical_units')

# تنظیمات برای نمایش مدل Professor در ادمین
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'phone_number', 'created_at')
    search_fields = ('name', 'email', 'department')
    list_filter = ('department',)

# تنظیمات برای نمایش مدل OfferedCourse در ادمین
class OfferedCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'professor', 'schedule', 'exam_time', 'max_capacity', 'registered_students', 'location', 'level', 'delivery_type', 'is_active')
    search_fields = ('course__name', 'professor__first_name', 'professor__last_name', 'schedule')
    list_filter = ('course', 'professor', 'is_active', 'delivery_type')

# ثبت مدل‌ها برای نمایش در ادمین
admin.site.register(Course, CourseAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(OfferedCourse, OfferedCourseAdmin)
admin.site.register(Class)