from django.urls import path
from .views import HomePageView, AnimalPageView, ReportStrayPageView, DonationPageView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('animal/', AnimalPageView.as_view(), name='animal'),
    path('report-stray/', ReportStrayPageView.as_view(), name='report_stray'),
    path('donation/', DonationPageView.as_view(), name='donate'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),


]
