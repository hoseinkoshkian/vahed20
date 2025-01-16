document.addEventListener('DOMContentLoaded', function () {
    let currentPage = 1;

    // دریافت اطلاعات اساتید
    function fetchProfessors(page = 1) {
        const url = `/cours/api/getAllProfessor?page=${page}`;

        fetch(url)
            .then((response) => response.json())
            .then((data) => {
                console.log('Professors Data received:', data);
                professors = data.professors
                // پاک کردن داده‌های قبلی
                const professorsData = document.getElementById('professors-data');
                professorsData.innerHTML = '';

                // افزودن داده‌های جدید به جدول
                professors.forEach((professor) => {
                    const row = document.createElement('div');
                    row.className = 'grid-cols-5 grid p-2 text-center bg-gray-200';
                    row.innerHTML = `
                        <div><a  href='/cours/showAllOfferdCourse?professor_id=${professor.id}'>${professor.name || 'ناموجود'}</a></div>
                        <div>${professor.phone_number || 'ناموجود'}</div>
                        <div>${professor.office_location || 'ناموجود'}</div>
                        <div>${professor.department || 'ناموجود'}</div>
                        <div>${professor.offered_courses_count || '0'}</div>
                    `;
                    professorsData.appendChild(row);
                });

                // تنظیم وضعیت دکمه‌ها
                totalPages = data.total_pages;
                console.log(page >= totalPages)
                document.getElementById('prev-btn').disabled = page === 1;
                document.getElementById('next-btn').disabled = page >= totalPages;

                currentPage = page;
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }

    // هندلر دکمه "قبلی"
    document.getElementById('prev-btn').addEventListener('click', function () {
        if (currentPage > 1) {
            fetchProfessors(currentPage - 1);
        }
    });

    // هندلر دکمه "بعدی"
    document.getElementById('next-btn').addEventListener('click', function () {
         if (currentPage < totalPages) {
            fetchProfessors(currentPage + 1);
        }
    });

    // فراخوانی اطلاعات صفحه اول هنگام بارگذاری
    fetchProfessors();
});
