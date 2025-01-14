from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True, verbose_name="کد درس")
    name = models.CharField(max_length=100, verbose_name="نام درس")
    practical_units = models.PositiveIntegerField(default=0, verbose_name="تعداد واحد عملی")
    theoretical_units = models.PositiveIntegerField(default=0, verbose_name="تعداد واحد نظری")

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name = "درس"
        verbose_name_plural = "دروس"


class Professor(models.Model):
    # اطلاعات استاد
    name = models.CharField(max_length=100, verbose_name="نام")
    email = models.EmailField(max_length=100, verbose_name="ایمیل")
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name="شماره تماس")
    office_location = models.CharField(max_length=200, null=True, blank=True, verbose_name="محل دفتر")

    # گروه آموزشی (مثلاً گروه ریاضی، گروه کامپیوتر)
    department = models.CharField(max_length=200, verbose_name="گروه آموزشی" , blank=True , null=True)

    # تاریخ ایجاد استاد
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f"{self.name} "

    class Meta:
        verbose_name = "استاد"
        verbose_name_plural = "اساتید"


class Class(models.Model):
    code = models.CharField(max_length=10, unique=True, verbose_name="کد کلاس")
    name = models.CharField(max_length=100, verbose_name="نام کلاس")

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name = "کلاس"
        verbose_name_plural = "کلاس‌ها"
class OfferedCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE ,blank=True, null=True, verbose_name="استاد")
    class_code = models.ForeignKey(Class, on_delete=models.CASCADE ,blank=True, null=True, verbose_name="کد کلاس ارائه شده")
    schedule = models.CharField(max_length=200, blank=True)
    weekday = models.CharField(max_length=20 , blank=True , null=True)
    weekday_start_time = models.CharField(max_length=20 , blank=True , null=True)
    weekday_end_time = models.CharField(max_length=20 , blank=True , null=True)
    exam_time = models.CharField(max_length=100, blank=True)
    max_capacity = models.IntegerField()
    registered_students = models.CharField(max_length=2)
    location = models.CharField(max_length=200, blank=True)
    level = models.CharField(max_length=100, blank=True)
    delivery_type = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    exam_date = models.CharField(max_length=100, blank=True , null=True)
    exam_start_time = models.CharField(max_length=100, blank=True , null=True)
    exam_end_time = models.CharField(max_length=100, blank=True , null=True)

    def __str__(self):
        return f"{self.course.name} - {self.class_code}"

