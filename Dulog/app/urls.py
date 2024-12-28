from django.urls import path
from .views import (HomePageView, AnimalPageView, ReportStrayPageView, ReportStrayListView, 
                    ReportStrayDetailView, ReportStrayCreateView, ReportStrayUpdateView, ReportStrayDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('animal/', AnimalPageView.as_view(), name='animal'),
    path('report-stray/', ReportStrayPageView.as_view(), name='report_stray'),
    path('stray-list/', ReportStrayListView.as_view(), name='stray_list'),
    path('stray-detail/<int:pk>', ReportStrayDetailView.as_view(), name='stray_detail'),
    path('stray-create/', ReportStrayCreateView.as_view(), name='stray_create'),
    path('stray-update/<int:pk>/edit', ReportStrayUpdateView.as_view(), name='stray_update'),
    path('stray-delete/<int:pk>/delete', ReportStrayDeleteView.as_view(), name='stray_delete'),
    


]
