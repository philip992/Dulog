from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Report, StrayAnimal
from django.contrib.auth.views import LoginView
from django.views import View
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class AnimalPageView(TemplateView):
    template_name = 'app/animal.html'

class ReportStrayPageView(TemplateView):
    template_name = 'app/stray.html'

class ReportStrayListView(ListView):
    model = Report
    template_name = 'app/ReportStray_list.html'
    context_object_name = 'reports'

class ReportStrayDetailView(DetailView):
    model = Report
    template_name = 'app/ReportStray_detail.html'
    context_object_name = 'report'

class ReportStrayCreateView(CreateView):
    model = Report
    fields = ['species', 'image', 'location', 'description', 'reporter_name', 'reporter_contact', 'status']
    template_name = 'app/ReportStray_create.html'
    success_url = reverse_lazy('stray_list')
    def form_valid(self, form):
       
        return super().form_valid(form)

class ReportStrayUpdateView(UpdateView):
    model = Report
    fields = ['species', 'image', 'location', 'description', 'reporter_name', 'reporter_contact', 'status']
    template_name = 'app/ReportStray_update.html'

    def get_success_url(self):
        
        return reverse_lazy('stray_detail', kwargs={'pk': self.object.pk})
    
class ReportStrayDeleteView(DeleteView):
    model = Report
    template_name = 'app/ReportStray_delete.html'
    success_url = reverse_lazy('stray_list')
    
class CustomLoginView(LoginView):
    def form_valid(self, form):
        print("Login successful, redirecting...")
        return super().form_valid(form)
    
class StrayAnimalDetailView(DetailView):
    model = StrayAnimal
    template_name = 'app/animal_detail.html'
    context_object_name = 'animal'
    


def animal_page(request):
    animals = StrayAnimal.objects.all() 
    return render(request, 'app/animal.html', {'animals': animals})

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('home')  
        return render(request, 'registration/signup.html', {'form': form})