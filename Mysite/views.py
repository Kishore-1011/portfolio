from django.shortcuts import render
from .forms import ContactForm
from .models import skill
from .models import Project
from .models import education
from .models import achivement

# Create your views here.
def home(request):
    skills = skill.objects
    projects = Project.objects
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data if needed
            return render(request, 'port/thankyou.html')
    else:
        form = ContactForm()
        return render(request,'port/homepage.html',{'skills':skills, 'projects':projects,'form': form})

def more_info(request):
    educations = education.objects
    achivements = achivement.objects
    return render(request,'port/more_info.html',{'educations':educations, 'achivements':achivements}) 

