from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('user/', views.userpage, name='UserPage'),
    path('profile/', views.profilesetting, name='Profile'),
    path('products/', views.products, name='Products'),
    path('customer/<str:pk_test>/', views.customer, name='Customer'),

    path('createOrder/<str:pk>/', views.createOrder, name='CreateOrder'),
    path('updateOrder/<str:pk>/', views.updateOrder, name='UpdateOrder'),
    path('deleteOrder/<str:pk>/', views.deleteOrder, name='DeleteOrder'),

    path('register/', views.register, name='Register'),
    path('login/', views.loginpage, name='Login'),
    path('logout/', views.logoutuser, name='Logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'), name='password_reset_complete'),
]

"""
    1 - Submit email form                       //PasswordResetView.as_view()
    2 - Email sent success message              //PasswordResetDoneView.as_view()
    3 - Link to password reset form in email    //PasswordResetConfirmView.as_view()
    4 - Password successfully changed message   //PasswordResetCompleteView.as_view()
"""