from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django import forms
from django.core.files.storage import FileSystemStorage
import os

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Upload an Image')

class ImageProcessingView(View):
    template_name = 'index.html'

    def get(self, request):
        form = ImageUploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():

            uploaded_image = form.cleaned_data['image']

        
            fs = FileSystemStorage()
            filename = fs.save(uploaded_image.name, uploaded_image)
            uploaded_file_url = fs.url(filename)

            response = {
                'kategori': 'T-shirt',  
                'aciklama': 'Basic cotton T-shirt with a classic design.',  
                'image_url': uploaded_file_url  
            }

            return JsonResponse(response)

        return render(request, self.template_name, {'form': form, 'error': 'Invalid form submission'})


class StatisticsView(View):
    def get(self, request):
        # İstatistik verileri burada gösterilecek
        return render(request, 'statistics.html')