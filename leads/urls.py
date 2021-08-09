from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path('', views.lead_list, name='lead-list'),
    path('<int:pk>/', views.lead_detail, name='lead-detail'),
    path('create/', views.lead_create, name='lead-create'),
    path('<int:pk>/update/', views.lead_update, name='lead-update'),
    path('<int:pk>/delete/', views.lead_delete, name='lead-delete'),
]
