from django.urls import path
from .views import (MessageList, MessageDestroy, MessageUpdate, Registration,
                    Login, logout)

urlpatterns = [
    path('', MessageList.as_view(), name='home'),
    path('update/<int:pk>', MessageUpdate.as_view(), name='update'),
    path('delete/<int:pk>', MessageDestroy.as_view(), name="delete"),
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view()),
    path('logout', logout),
]
