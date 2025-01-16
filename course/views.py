from django.shortcuts import render
from django.views import View
# Create your views here.
import csv
from .models import *
from django.http import JsonResponse
import re
from django.core.paginator import Paginator

class courseRegistration(View):
    def get (self, request):
        return render(request , 'html/course/courseRegistration.html' , {})

    def post (self, request, *args, **kwargs):
        if 'csvFile' in request.FILES:
            uploaded_file = request.FILES['csvFile']

            # خواندن فایل CSV
            decoded_file = uploaded_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            # پردازش فایل CSV و ذخیره داده‌ها در مدل
            for row in reader:
                code = row['كد درس'].strip()  # نام دقیق ستون را با دقت وارد کنید
                name = row['نام درس'].strip()
                practical_units = float(row['تعداد واحد عملي'].strip() or 0)
                theoretical_units = float(row['تعداد واحد نظري'].strip() or 0)
                print(code)
                # بررسی وجود درس بر اساس کد درس
                if not Course.objects.filter(code=code).exists():
                    # ایجاد و ذخیره درس جدید
                    Course.objects.create(
                        code=code,
                        name=name,
                        practical_units=practical_units,
                        theoretical_units=theoretical_units
                    )
                    print(f"درس {name} با کد {code} ذخیره شد.")
                else:
                    print(f"درس با کد {code} قبلاً در پایگاه داده وجود دارد.")
        return render(request , 'html/course/courseRegistration.html' , {})
class professorsRegistration(View):

    def post (self, request, *args, **kwargs):
        if 'csvFile' in request.FILES:
            uploaded_file = request.FILES['csvFile']

            # خواندن فایل CSV
            decoded_file = uploaded_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            # پردازش فایل CSV و ذخیره اساتید در مدل
            for row in reader:
                name = row['استاد'].strip()

                # بررسی وجود استاد بر اساس اسم و نام خانوادگی
                if not Professor.objects.filter(name=name).exists():
                    # ایجاد و ذخیره استاد جدید
                    Professor.objects.create(
                        name=name,
                        # سایر فیلدها را بر اساس نیاز خود اضافه کنید
                    )
                    print(f"استاد {name} ذخیره شد.")
                else:
                    print(f"استاد {name} قبلاً در پایگاه داده وجود دارد.")

        return render(request , 'html/course/courseRegistration.html' , {})
class classRegistration(View):
    def post (self, request, *args, **kwargs):
        if 'csvFile' in request.FILES:
            uploaded_file = request.FILES['csvFile']

            # خواندن فایل CSV
            decoded_file = uploaded_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            # پردازش فایل CSV و ذخیره داده‌ها در مدل Class
            for row in reader:
                class_code = row['كد ارائه کلاس درس'].strip()
                class_name = row['نام كلاس درس'].strip()

                # بررسی وجود کلاس بر اساس کد کلاس
                if not Class.objects.filter(code=class_code).exists():
                    # ایجاد و ذخیره کلاس جدید
                    Class.objects.create(
                        code=class_code,
                        name=class_name
                    )
                    print(f"کلاس {class_name} با کد {class_code} ذخیره شد.")
                else:
                    print(f"کلاس با کد {class_code} قبلاً در پایگاه داده وجود دارد.")

        return render(request , 'html/course/courseRegistration.html' , {})

class offeredCoursesRegistration(View):
    def post (self, request, *args, **kwargs):
        if 'csvFile' in request.FILES:
            uploaded_file = request.FILES['csvFile']

            # خواندن فایل CSV
            decoded_file = uploaded_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            for row in reader:

                course_code = row.get('كد درس', '').strip()
                class_code = row.get('كد ارائه کلاس درس', '').strip()
                professor_name = row.get('استاد', '').strip()
                schedule = row.get('زمانبندي تشکيل کلاس', '').strip()
                exam_time = row.get('زمان امتحان', '').strip()
                max_capacity = int(row.get('حداکثر ظرفیت', '0').strip() or 0)
                registered_students = int(row.get('تعداد ثبت نامی تاکنون', '0').strip() or 0)
                location = row.get('محل برگزاری', '').strip()
                level = row.get('مقطع ارائه درس', '').strip()
                delivery_type = row.get('نوع ارائه', '').strip()
                is_active = row.get('وضعیت فعال', 'True') == 'True'  # به صورت پیشفرض فعال فرض می‌شود

                # رشته ورودی
                input_text = exam_time

                # الگوی استخراج تاریخ و زمان
                pattern = r"(?P<date>\d{4}/\d{2}/\d{2}) از (?P<start_time>\d{2}:\d{2}) تا (?P<end_time>\d{2}:\d{2})"

                match = re.match(pattern, input_text)

                if match:
                    exam_date = match.group("date")  # تاریخ
                    exam_start_time = match.group("start_time")  # زمان شروع
                    exam_end_time = match.group("end_time")  # زمان پایان
                else:
                    exam_date = ""  # تاریخ
                    exam_start_time = ""  # زمان شروع
                    exam_end_time = ""   # زمان پایان
                findOstad = Professor.objects.filter(name=professor_name).first()
                if not findOstad :
                    print('error in find ostad')
                findclass = Class.objects.filter(name=class_code).first()
                if not findOstad:
                    print('error in find class')
                findcourse = Course.objects.filter(code = course_code).first()
                if not findcourse:
                    print('error in find course')
                weekday_map = {
                    'شنبه': '0',
                    'یکشنبه': '1',
                    'دوشنبه': '2',
                    'سه‌شنبه': '3',
                    'چهارشنبه': '4',
                    'پنج‌شنبه': '5',
                    'جمعه': '6'
                }

                # الگوی regex برای استخراج زمان‌ها و روز
                pattern_schedul = r"(?P<weekday>[\u0600-\u06FF\s]+) از (?P<start_time>\d{2}:\d{2}) تا (?P<end_time>\d{2}:\d{2})"



                match_schedule = re.match(pattern_schedul, schedule)

                if match_schedule:
                    weekday = match_schedule.group("weekday")  # روز هفته
                    start_time = match_schedule.group("start_time")  # زمان شروع
                    end_time = match_schedule.group("end_time")  # زمان پایان

                    # تبدیل روز به عدد معادل آن در دیکشنری
                    weekday = weekday.strip()  # حذف فضای خالی اضافی
                    weekday_number = weekday_map.get(weekday, None)

                    if weekday_number is not None:
                        print(f"Day: {weekday} (mapped to {weekday_number})")
                    else:
                        print("Invalid weekday name")
                else:
                    weekday = ""
                    start_time = ""
                    end_time = ""
                print('data is created ')
                OfferedCourse.objects.create(
                    course=findcourse ,
                    professor=findOstad,
                    class_code =findclass ,
                    schedule = schedule ,
                    exam_time =exam_time,
                    max_capacity  = max_capacity ,
                    registered_students = registered_students ,
                    location = location,
                    level= level,
                    delivery_type = delivery_type ,
                    exam_date = exam_date ,
                    exam_start_time = exam_start_time ,
                    exam_end_time = exam_end_time ,
                    weekday = weekday ,
                    weekday_start_time = start_time ,
                    weekday_end_time=end_time,
                )

        return render(request , 'html/course/courseRegistration.html' , {})


class showAllCourse(View):
    def get (self, request, *args, **kwargs):
        return render(request , 'html/course/showAllCourse.html' , {})


class showAllOfferedCourse(View):
    def get (self, request, *args, **kwargs):
        return render(request , 'html/course/showAllOfferedCourse.html' , {})




# api

class getCoursesApiView(View):
    def get (self, request, *args, **kwargs):
        # دریافت فیلترها از query params
        course_name = request.GET.get('courseName', '')
        course_code = request.GET.get('courseCode', '')
        practical_units = request.GET.get('practicalUnits', '')
        theoretical_units = request.GET.get('theoreticalUnits', '')

        # فیلتر کردن دروس بر اساس پارامترها
        courses = Course.objects.all()

        # اعتبارسنجی مقادیر عددی برای practical_units و theoretical_units
        if practical_units and practical_units.isdigit():
            courses = courses.filter(practical_units=practical_units)
        if theoretical_units and theoretical_units.isdigit():
            courses = courses.filter(theoretical_units=theoretical_units)
        if course_name:
            courses = courses.filter(name__icontains=course_name)
        if course_code:
            courses = courses.filter(code__icontains=course_code)

        # بازگرداندن داده‌ها به صورت JSON
        courses_data = list(courses.values('code', 'name', 'practical_units', 'theoretical_units'))
        return JsonResponse({'courses': courses_data})

from django.db.models import Count
class getOfferedCoursesApiView(View):
    def get(self, request, *args, **kwargs):
        page_number = request.GET.get('page', 1)
        items_per_page = 20

        # فیلترها از query params
        professor_name = request.GET.get('professor', None)
        course_code = request.GET.get('course_code', None)
        weekday = request.GET.get('weekday', None)
        exam_date = request.GET.get('exam_date', None)
        start_time = request.GET.get('start_time', None)
        end_time = request.GET.get('end_time', None)
        course_name = request.GET.get('course_name', None)
        professor_id = request.GET.get('professor_id', None)
        print(professor_id)
        courses = OfferedCourse.objects.filter(is_active=True).values(
            'course__name',
            'professor__name',
            'professor__id',
            'class_code__code',
            'weekday',
            'weekday_start_time',
            'weekday_end_time',
            'exam_date',
            'exam_start_time',
            'exam_end_time',
            'schedule',
            'max_capacity',
            'registered_students',
            'location',
            'delivery_type'
        )

        # اعمال فیلتر بر اساس استاد
        if professor_name:
            courses = courses.filter(professor__name__icontains=professor_name)
        if course_name:
            courses = courses.filter(course__name__icontains=course_name)
        if course_code:
            courses = courses.filter(course__code__icontains=course_code)
        if professor_id:
            courses = courses.filter(professor__id=professor_id)

        # اعمال فیلتر بر اساس روز هفته
        if weekday:
            # دیکشنری نگاشت روزهای هفته به معادل فارسی
            weekday_map = {
                '0': 'شنبه',
                '1': 'يكشنبه',
                '2': 'دوشنبه',
                '3': 'سه شنبه',
                '4': 'چهارشنبه',
                '5': 'پنج شنبه',
                '6': 'جمعه'
            }


            # چک کردن اینکه آیا روز وارد شده در دیکشنری هست یا نه
            if weekday in weekday_map:
                day_name = weekday_map[weekday]
                courses = courses.filter(weekday=day_name)
                print('is ok')
            else:
                print('Invalid weekday')
        # اعمال فیلتر بر اساس تاریخ امتحان
        if exam_date:
            courses = courses.filter(exam_date=exam_date)

        # اعمال فیلتر بر اساس ساعت شروع
        if start_time:
            courses = courses.filter(exam_start_time__gte=start_time)

        # اعمال فیلتر بر اساس ساعت پایان
        if end_time:
            courses = courses.filter(exam_end_time__lte=end_time)

        # پیکربندی صفحه‌بندی
        paginator = Paginator(courses, items_per_page)
        page_obj = paginator.get_page(page_number)

        # ارسال داده‌ها به فرانت‌اند
        data = list(page_obj)
        print(data)
        return JsonResponse(data, safe=False)
class getAllProfessor(View):
    def get(self, request, *args, **kwargs):
        page_number = request.GET.get('page', 1)
        items_per_page = 20
        professor_name = request.GET.get('professor', None)

        # فیلتر و شمارش تعداد دروس ارائه‌شده
        professors = Professor.objects.annotate(
            offered_courses_count=Count('offeredcourse')
        ).values(
            'id',
            'name',
            'phone_number',
            'office_location',
            'department',
            'offered_courses_count',  # تعداد دروس ارائه‌شده
        )

        # اعمال فیلتر بر اساس نام استاد
        if professor_name:
            professors = professors.filter(name=professor_name)

        # صفحه‌بندی
        paginator = Paginator(professors, items_per_page)
        page_obj = paginator.get_page(page_number)

        # آماده‌سازی داده‌ها برای ارسال
        data = {
            "professors": list(page_obj),
            "total_pages": paginator.num_pages,
        }
        return JsonResponse(data, safe=False)


class professorView(View):
    def get (self, request,id):
        professor = Professor.objects.filter(id=id)
        if not professor.exists():
            return JsonResponse('professor not found', safe=False)
        return render(request , 'html/course/professor.html' , {})
class professorsListView(View):
    def get (self, request):
        return render(request , 'html/course/professorsList.html' , {})
