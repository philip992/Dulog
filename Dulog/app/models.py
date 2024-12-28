from django.db import models
from django.utils import timezone
from django.urls import reverse





class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class StrayAnimal(models.Model):
    species = models.CharField(max_length=100)  
    breed = models.CharField(max_length=100, blank=True) 
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20, choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])
    found_date = models.DateField(default=timezone.now)
    health_status = models.CharField(max_length=50, blank=True) 
    image = models.ImageField(upload_to='animal_images/', blank=True, null=True)  
    description = models.TextField(blank=True)
    

    def __str__(self):
        return f'{self.species} - {self.color}'
    





class Report(models.Model):
    SPECIES_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
    ]
    
    
    species = models.CharField(max_length=100, choices=SPECIES_CHOICES)
    image = models.ImageField(upload_to='animal_images/', blank=True, null=True)  
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    reporter_name = models.CharField(max_length=100)
    reporter_contact = models.CharField(max_length=15)
    report_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20, 
        choices=[('pending', 'Pending'), ('resolved', 'Resolved'), ('in_progress', 'In Progress')],
        default='pending'
    )

    def __str__(self):
        return f'Report of {self.species} on {self.report_date}'
    
    def get_absolute_url(self):
        return reverse('report-detail', kwargs={'pk': self.pk})
    



