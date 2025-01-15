function updatePageNumber(page) {
    const pageNumberElement = document.getElementById('page-number'); // عنصر شماره صفحه
    if (pageNumberElement) {
        pageNumberElement.textContent =  page;
    }
}


document.addEventListener('DOMContentLoaded', function () {
    let page = 1; // شماره صفحه فعلی
    updatePageNumber(page)
    const courseContent = document.getElementById('course-content');
    const nextPageButton = document.getElementById('next-page');
    const previousPageButton = document.getElementById('previous-page');

    // تابع برای واکشی داده‌ها از بک‌اند
    function fetchCourses(page) {
        const urlParams = new URLSearchParams(window.location.search);
        const course_code = urlParams.get('course_code');
        fetch(`api/getOfferedCoursesApiView?page=${page}&course_code=${course_code}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                // پاک کردن محتوای قبلی
                courseContent.innerHTML = '';

                // افزودن داده‌ها به صفحه
                if (data.length === 0) {
                    courseContent.innerHTML = '<div class="text-center text-gray-500">اطلاعاتی یافت نشد.</div>';
                } else {
                    data.forEach(course => {
                        const row = document.createElement('div');
                        row.classList.add('grid', 'grid-cols-7', 'text-center', 'text-sm', 'bg-gray-100');
                        row.innerHTML = `
                            <div>${course.course__name || ''}</div>
                            <div>${course.course__code || ''}</div>
                            <div>${course.professor__name || ''}</div>
                            <div>${course.weekday || ''}</div>
                            <div>${course.weekday_start_time || ''}</div>
                            <div>${course.weekday_end_time || ''}</div>
                            <div>${course.delivery_type || ''}</div>
                        `;
                        courseContent.appendChild(row);
                    });
                }
            })
            .catch(error => console.error('Error fetching course data:', error));
    }

    // واکشی داده‌های اولیه
    fetchCourses(page);

    // افزودن رویداد برای دکمه "بعدی"
    nextPageButton.addEventListener('click', () => {
        page++;
        fetchCourses(page);
    updatePageNumber(page)

    });

    // افزودن رویداد برای دکمه "قبلی"
    previousPageButton.addEventListener('click', () => {
        if (page > 1) {
            page--;
            fetchCourses(page);
    updatePageNumber(page)


        }
    });
});

function formatDateInput(input) {
    let value = input.value.replace(/[^0-9]/g, ''); // حذف کاراکترهای غیر عددی

    // افزودن '/' بعد از چهارمین و هفتمین کاراکتر
    if (value.length > 4) {
        value = value.slice(0, 4) + '/' + value.slice(4);
    }
    if (value.length > 7) {
        value = value.slice(0, 7) + '/' + value.slice(7);
    }

    // محدود کردن طول ورودی به 10 کاراکتر
    if (value.length > 10) {
        value = value.slice(0, 10);
    }

    input.value = value;
}



document.addEventListener('DOMContentLoaded', function () {
    const searchButton = document.getElementById('search-filter'); // دکمه جستجو
    const courseContent = document.getElementById('course-content'); // قسمت نمایش دوره‌ها
    const form = document.getElementById('search-form'); // فرم جستجو

    // تابع برای جمع‌آوری داده‌های ورودی و ارسال درخواست به API
    function fetchCourses() {
        // جمع‌آوری مقادیر از ورودی‌ها
        const professor = document.getElementById('professor').value;

        const weekday = document.getElementById('weekday').value;
        const examDate = document.getElementById('exam_date').value;
        const startTime = document.getElementById('start_time').value;
        const endTime = document.getElementById('end_time').value;
        const course = document.getElementById('course-name').value;


        // ساخت URL برای API
        let url = `/cours/api/getOfferedCoursesApiView?`;

        if (professor) url += `professor=${professor}&`;
        if (weekday && weekday != "انتخاب کنید ...") url += `weekday=${weekday}&`;
        if (examDate) url += `exam_date=${examDate}&`;
        if (startTime) url += `start_time=${startTime}&`;
        if (endTime) url += `end_time=${endTime}&`;
        if (course) url += `course_name=${course}&`;


        // حذف علامت & اضافی در انتهای URL
        url = url.slice(0, -1);

        // ارسال درخواست به API
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                // پاک کردن محتوای قبلی
                courseContent.innerHTML = '';

                // نمایش داده‌ها
                if (data.length === 0) {
                    courseContent.innerHTML = '<div class="text-center text-gray-500">اطلاعاتی یافت نشد.</div>';
                } else {
                    data.forEach(course => {
                        const row = document.createElement('div');
                        row.classList.add('grid', 'grid-cols-7', 'text-center', 'text-sm', 'bg-gray-100');
                        row.innerHTML = `
                            <div>${course.course__name || ''}</div>
                            <div>${course.course__code || ''}</div>
                            <div>${course.professor__name || ''}</div>
                            <div>${course.weekday || ''}</div>
                            <div>${course.weekday_start_time || ''}</div>
                            <div>${course.weekday_end_time || ''}</div>
                            <div>${course.delivery_type || ''}</div>
                        `;
                        courseContent.appendChild(row);
                    });
                }
            })
            .catch(error => {
                console.error('Error fetching course data:', error);
                courseContent.innerHTML = '<div class="text-center text-red-500">خطا در دریافت اطلاعات.</div>';
            });
    }

    // اضافه کردن رویداد برای دکمه "جست و جو"
    searchButton.addEventListener('click', function () {
        fetchCourses();
    });
});
