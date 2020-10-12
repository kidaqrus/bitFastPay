from django.shortcuts import render
from django.utils import timezone
from .models import Post
import mimetypes
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def home(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'Bitcoin/home.html', {'posts': posts})



def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'CERTIFICATE.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf,content_type='application/pdf')
            response['Content-Disposition']= 'inline; filename="CERTIFICATE.pdf"'
            return response

    else:
        return HttpResponseNotFound('the requested pdf was not found')



