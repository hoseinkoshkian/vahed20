

from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
    path('courseRegistration', courseRegistration.as_view(), name='courseRegistration'),
    path('professorsRegistration', professorsRegistration.as_view(), name='professorsRegistration'),
    path('showAllCourse', showAllCourse.as_view(), name='showAllCourse') ,
    path('classRegistration', classRegistration.as_view(), name='classRegistration'),
    path('offeredCoursesRegistration', offeredCoursesRegistration.as_view(), name='offeredCoursesRegistration'),
    path('showAllOfferdCourse', showAllOfferedCourse.as_view(), name='showAllOfferedCourse'),

#     api
    path('getCoursesApiView', getCoursesApiView.as_view(), name='getCoursesApiView'),
    path('api/getOfferedCoursesApiView', getOfferedCoursesApiView.as_view(), name='getOfferedCoursesApiView'),

]
