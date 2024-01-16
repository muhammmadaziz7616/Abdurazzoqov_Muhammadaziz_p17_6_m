from django.contrib.auth.views import LogoutView
from django.urls import path
from apps.views import SimpleView, delete_page, update_page, index, CustomLoginView, RegisterFormView

urlpatterns = [
    path('', SimpleView.as_view(), name='Simpley'),
    path('update_page/<int:pk>/', index, name='index'),
    path('delete/<int:pk>/', delete_page, name='delete_page'),
    path('update_simpley/<int:pk>/', update_page, name='update_page'),
    path('login', CustomLoginView.as_view(), name='login_page'),
    path('register', RegisterFormView.as_view(), name='register_page'),
]
