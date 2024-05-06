from django.urls import  path

from patient import views

urlpatterns = [
    path('pat/',views.patient1),
    path('pa/',views.patient2),
    path('patdel/<int:varb>/',views.patdelete,name='delete')
    
]