from django.urls import path, include

from Bitcoin import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pdf/', views.pdf_view, name='pdf_view'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', views.registration, name="registration")

    
    
    



]