# app/urls.py

from django.urls import path
from .views import profile_view, job_list_view, job_detail_view, scrape_jobs_view, get_recommendations

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('jobs/', job_list_view, name='job_list'),
    path('jobs/<int:job_id>/', job_detail_view, name='job_detail'),
    path('scrape-jobs/', scrape_jobs_view, name='scrape_jobs'),
    path('api/recommendations/<int:user_id>/', get_recommendations, name='get_recommendations'),
]
