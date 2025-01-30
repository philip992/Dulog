from django.urls import path
from django.contrib import admin
from django.urls import include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .views import (HomePageView, AnimalPageView, ReportStrayPageView, ReportStrayListView, 
                    ReportStrayDetailView, ReportStrayCreateView, ReportStrayUpdateView, ReportStrayDeleteView,
                    StrayAnimalDetailView)  # Import StrayAnimalDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('animal/', AnimalPageView.as_view(), name='animal'),
    path('report-stray/', ReportStrayPageView.as_view(), name='report_stray'),
    path('stray-list/', ReportStrayListView.as_view(), name='stray_list'),
    path('stray-detail/<int:pk>/', ReportStrayDetailView.as_view(), name='stray_detail'),
    path('stray-create/', ReportStrayCreateView.as_view(), name='stray_create'),
    path('stray-update/<int:pk>/edit', ReportStrayUpdateView.as_view(), name='stray_update'),
    path('stray-delete/<int:pk>/delete', ReportStrayDeleteView.as_view(), name='stray_delete'),
    path('animal-detail/<int:pk>/', StrayAnimalDetailView.as_view(), name='animal_detail'), 
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
