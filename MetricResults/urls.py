"""MetricResults URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resultsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get-results/', views.get_resultsapi, name='get_api'),
    path('api/post-results/', views.post_resultsapi, name='post_api'),
    path('api/retrieve-results/<pk>/', views.retrieve_resultsapi, name='retrieve_api'),
    path('api/put-results/<pk>/', views.put_resultsapi, name='put_api'),
    path('api/delete-results/<pk>/', views.delete_resultsapi, name='delete_api'),
]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', views.ResultsApi.as_view(), name='api'),
#     path('api/post-data', views.ResultsApi.as_view(), name='post_data'),
#     path('api/<pk>/', views.GetResultsApi.as_view()),
#
# ]