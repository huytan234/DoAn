from django.urls import path, re_path, include
from rest_framework import routers
from . import views

from .admin import admin_site

r = routers.DefaultRouter()
r.register('users', views.UserViewSet, 'users')
r.register('services', views.ServiceViewSet, 'services')
r.register('bills', views.BillViewSet, 'bills')
r.register('residentfamiles', views.ResidentFamilyViewSet, 'residentfamiles')
r.register('tudos', views.TuDoViewSet, 'tudos')
r.register('packages', views.PackageViewSet, 'packages')
r.register('feedbacks', views.FeedbackViewSet, 'feedbacks')
r.register('surveyforms', views.SurveyViewSet, 'surveyforms')
r.register('surveyresponses', views.SurveyAnswerViewSet, 'surveyresponses')

urlpatterns = [
    path('', include(r.urls)),
    path('admin/', admin_site.urls)
]