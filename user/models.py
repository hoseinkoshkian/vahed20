from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class User(AbstractUser):
    # فیلد شماره تلفن (ضروری)
    phone_regex = RegexValidator(
        regex=r'^09\d{9}$',
        message="شماره تلفن باید با 09 شروع شود و 11 رقم داشته باشد. مثال: 09139785339"
    )
    phone_number = models.CharField(
        max_length=11,
        validators=[phone_regex],
        unique=True,  # شماره تلفن باید منحصر به فرد باشد
        verbose_name="شماره تلفن"
    )

    # فیلد ایمیل (اختیاری)
    email = models.EmailField(
        blank=True,  # اختیاری
        null=True,   # اختیاری
        verbose_name="ایمیل"
    )

    # فیلد نام (اجباری)
    first_name = models.CharField(
        max_length=30,
        verbose_name="نام",
        blank=False,  # اجباری
        null=False    # اجباری
    )

    # فیلد نام خانوادگی (اجباری)
    last_name = models.CharField(
        max_length=30,
        verbose_name="نام خانوادگی",
        blank=False,  # اجباری
        null=False    # اجباری
    )

    # تنظیم فیلد USERNAME_FIELD برای لاگین با شماره تلفن
    USERNAME_FIELD = 'phone_number'

    # فیلدهای مورد نیاز برای ایجاد کاربر (به غیر از USERNAME_FIELD و password)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']  # ایمیل اختیاری است

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"