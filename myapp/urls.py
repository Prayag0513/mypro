from django.urls import path
from .import views
app_name='myapp'
urlpatterns = [
    path('teacherreg/',views.teacherregister,name='teacherr'),
    path('teacherlog/',views.teacherlogin,name='teacherl'),
    path('home/',views.home,name='home'),
    path('teachers/',views.teachers,name='teachersr'),
    path('course/',views.course,name='course'),
    path('teacherdata/',views.teacherdata,name='teacherdata'),
    path('payments/',views.payment,name='payment'),
    path('logout/',views.logout_view,name='logout'),
    path('students/',views.students,name='studentsr'),
    path('studentdata/',views.studentdata,name='studentdata'),
    path('enquiry/',views.enquiryview,name='enquiry')
    
]
