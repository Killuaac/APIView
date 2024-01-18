from django.urls import path
from .views import (CreateStudentView, CreateSubjectView, CreateClassView,
                    DeleteOrUpdateClassView, DeleteOrUpdateStudentView,
                    DeleteOrUpdateSubjectView, Registration, Login, logout)

urlpatterns = [
    path('students/', CreateStudentView.as_view()),
    path('subjects/', CreateSubjectView.as_view()),
    path('classes/', CreateClassView.as_view()),
    path('studentsdelete/<int:pk>', DeleteOrUpdateStudentView.as_view()),
    path('subjectsdelete/<int:pk>', DeleteOrUpdateSubjectView.as_view()),
    path('classdelete/<int:pk>', DeleteOrUpdateClassView.as_view()),
    path('register/', Registration.as_view()),
    path('login/', Login.as_view()),
    path('logout/', logout)
]
