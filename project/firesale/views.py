from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from .models import MyData

# Create your views here
def index(request):
    return render(request, 'base.html')

def upload_data(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            MyData.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                # Add more fields as per your model
            )
            return redirect('success')  # Redirect to a success page
    else:
        form = UploadForm()
    
    return render(request, 'upload.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def get_members(request):
    return render(request, 'members/index.html')