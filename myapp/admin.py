from django.contrib import admin
from .models import * 
# Register your models here.

class teachers(admin.ModelAdmin):
    list_display=['Name','Image','ContactNo','Emailid','Expierence','teachingsubject']
admin.site.register(teachersrModel)

class coursesAdmin(admin.ModelAdmin):
    list_display=['courseimage','coursename','courseduration','coursedetails','coursefee']
admin.site.register(courses,coursesAdmin)


class teachers(admin.ModelAdmin):
    list_display=['Name','Image','ParentNo','Branch','Section','Subjects']
admin.site.register(studentsrModel)
