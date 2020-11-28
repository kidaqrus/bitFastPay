from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm

# Create your views here.


def home(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'Bitcoin/home.html', {'posts': posts})



        



def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'pdf/CERTIFICATE.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf,content_type='application/pdf')
            response['Content-Disposition']= 'attachment; filename="pdf/CERTIFICATE.pdf"'
            return response

    else:
        return HttpResponseNotFound('the requested pdf was not found')



def registration(request):
    if request.method == "GET":
        return render(request, "registration/register.html", {"form": CustomUserCreationForm}
        )
            
            
        
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))