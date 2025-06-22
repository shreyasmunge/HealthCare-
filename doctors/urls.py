from django.urls import path
from .views import DoctorViewSet

doctor_list = DoctorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

doctor_detail = DoctorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', doctor_list, name='doctor-list'),
    path('<int:pk>/', doctor_detail, name='doctor-detail'),
]
