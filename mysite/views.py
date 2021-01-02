from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
import os
from .forms import upload_form
from .models import upload
from throttle.decorators import throttle
#https://github.com/sobotklp/django-throttle-requests


class Home(TemplateView):
    template_name = 'home.html'


def upload_list(request):
    uploads = upload.objects.all()
    return render(request, 'document_list.html', {
        'uploads': uploads
    })

@throttle(zone='default')
def upload_document(request):
    if request.method == 'POST':
        form = upload_form(request.POST, request.FILES)
        filesize = os.path.getsize(request.FILES)
        if form.is_valid():
            form.save()
            context = {
                'filesize': filesize
            }
            return redirect('document_list', context)
    else:
        form = upload_form()
    return render(request, 'upload_document.html', {
        'form': form
    })

@throttle(zone='default')
def delete_document(request, pk):
    if request.method == 'POST':
        upload = upload.objects.get(pk=pk)
        upload.delete()
    return redirect('document_list')

