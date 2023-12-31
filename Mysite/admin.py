from django.contrib import admin
from .models import skill
from .models import Project
from .models import education
from .models import achivement

# Register your models here.
admin.site.register(skill)
admin.site.register(Project)
admin.site.register(education)
admin.site.register(achivement)
