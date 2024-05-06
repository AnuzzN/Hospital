from django.shortcuts import render

# Create your views here.
from patient.models import  patients




# Create your views here.
def patient1(request):
    if request.method=='POST':
        obj=patients()
        obj.fname=request.POST.get('Name')
        obj.disease=request.POST.get('Disease')
        obj.visitingdoctor=request.POST.get('visitingdoctor')
        obj.save()
    return render(request,'pat.html')
def patient2(request):
    obj=patients.objects.all()
    return render(request,'viewpatient.html',{'data':obj})
def patdelete(request,varb):
    obj= patients.objects.get(id=varb) 
    obj.delete()
    return patient2(request)