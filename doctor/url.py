
from django.urls import  path

from doctor import views

urlpatterns = [
    path('doc/',views.doctor1),
    path('doct/',views.doctor2,name='viewdoc'),
    path('up/<int:varb>',views.docupdate,name='update'),
    path('del/<int:varb>/',views.docdelete,name='delete'),
    path('',views.indexview)
    
]