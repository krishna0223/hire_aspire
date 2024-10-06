# app/views.py

from django.shortcuts import render
from .models import UserProfile, JobPosting
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ml import calculate_similarity
from .scraping import scrape_jobs
from django.contrib.auth.decorators import login_required

# API VIEW: Get Job Recommendations
@api_view(['GET'])
def get_recommendations(request, user_id):
    user_profile = UserProfile.objects.get(user_id=user_id)
    user_skills = ", ".join([skill.name for skill in user_profile.skills.all()])

    jobs = JobPosting.objects.all()
    recommended_jobs = []

    for job in jobs:
        job_description = job.description
        similarity = calculate_similarity(user_skills, job_description)

        if similarity > 0.75:
            recommended_jobs.append({
                'title': job.title,
                'company': job.company_name,
                'location': job.location,
                'description': job.description
            })

    return Response({'jobs': recommended_jobs})

# API VIEW: Scrape Jobs from External Websites
@api_view(['GET'])
def scrape_jobs_view(request):
    scrape_jobs()
    return Response({'status': 'success', 'message': 'Job scraping completed'})

# Profile View: Render Profile Page and Calculate Profile Completion
@login_required
def profile_view(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    # Logic to calculate profile completion percentage
    completed_fields = 0
    total_fields = 4  # Adjust this based on your requirements

    if user.first_name and user.last_name:
        completed_fields += 1
    if user.email:
        completed_fields += 1
    if user_profile.phone:
        completed_fields += 1
    if user_profile.resume:
        completed_fields += 1

    profile_completion = (completed_fields / total_fields) * 100

    return render(request, 'profile.html', {
        'user': user,
        'profile_completion': profile_completion,
        'user_profile': user_profile,
    })

# Job Listings View: Display a List of Job Postings
def job_list_view(request):
    jobs = JobPosting.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

# Job Detail View: Display Detailed Information About a Specific Job
def job_detail_view(request, job_id):
    job = JobPosting.objects.get(id=job_id)
    return render(request, 'job_detail.html', {'job': job})
