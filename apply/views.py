from django.shortcuts import render
from .models import ApplyModel
# Create your views here.

def home_apply(request):
    email_error = ''
    if request.method == 'POST':
    
        email = request.POST['email']
    
        if ApplyModel.objects.filter(email=email).exists():
            email_error = 'Email already exsists !!'
        else:
            name = request.POST['name']
            profession = request.POST.get('toggle')
            create_apply_object = ApplyModel.objects.create(name=name,email=email,profession=profession)
            create_apply_object.save()
        
    template_name = 'index.html'
    context = {'error': email_error }
    return render(request,template_name,context)




