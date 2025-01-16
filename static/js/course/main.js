document.addEventListener('DOMContentLoaded', function() {
    // ارسال درخواست برای دریافت داده‌ها
    fetchCourses();
});

function fetchCourses(filterData = {}) {
    // اضافه کردن داده‌های فیلتر به URL به‌صورت query params
    let url = "/cours/getCoursesApiView";
    let query = new URLSearchParams(filterData).toString();
    if (query) {
        url += `?${query}`;
    }

    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log('Data received:', data);
            const courses = data.courses;

            // ساخت جدول
            let table = '<table  class="w-full border-collapse">';
            table += '<thead><tr><th>کد درس</th><th>نام درس</th><th>تعداد واحد عملی</th><th>تعداد واحد نظری</th></tr></thead>';
            table += '<tbody>';

            // اضافه کردن داده‌ها به جدول
            courses.forEach(course => {
                table += `
                    <tr class="">
                        <td><a href='/cours/showAllOfferdCourse?course_code=${course.code}'>${course.code}</a></td>
                        <td>${course.name}</td>
                        <td>${course.practical_units}</td>
                        <td>${course.theoretical_units}</td>
                    </tr>
                `;
            });

            table += '</tbody></table>';

            // اضافه کردن جدول به بخش HTML
            document.getElementById('course-table').innerHTML = table;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function filterCourses() {
    var practicalUnits = document.getElementById("practicalUnits").value;
    var theoreticalUnits = document.getElementById("theoreticalUnits").value;

    // بررسی اینکه آیا ورودی‌ها عددی هستند
    if (isNaN(practicalUnits) || isNaN(theoreticalUnits)) {
        alert("لطفاً تعداد واحدهای عملی و نظری را به صورت عدد وارد کنید.");
        return;  // جلوگیری از ارسال درخواست در صورت وارد کردن داده غیر عددی
    }

    var filterData = {
        courseName: document.getElementById("courseName").value,
        courseCode: document.getElementById("courseCode").value,
        practicalUnits: practicalUnits,
        theoreticalUnits: theoreticalUnits
    };

    // ارسال فیلترها و دریافت داده‌ها
    fetchCourses(filterData);
}
