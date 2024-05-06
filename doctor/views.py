from django.shortcuts import redirect, render

from doctor.models import doctors




# Create your views here.
def doctor1(request):
    if request.method=='POST':
        obj=doctors()
        obj.fname=request.POST.get('Name')
        obj.Specialisation=request.POST.get('Specialisation')
        obj.visitingtime=request.POST.get('visitingtime')
        obj.save()
    return render(request,'doc.html')
def doctor2(request):
    obj=doctors.objects.all()
    return render(request,'viewdoctor.html',{'data':obj})
def docupdate(request,varb):
    obj=doctors.objects.get(id=varb)
    if request.method=='POST':
        obj=doctors.objects.get(id=varb)
        obj.fname=request.POST.get('Name')
        obj.Specialisation=request.POST.get('Specialisation')
        obj.visitingtime=request.POST.get('visitingtime')
        obj.save()
        return redirect('viewdoc')
    return render(request,'update.html',{'data':obj})
def docdelete(request,varb):
    obj=doctors.objects.get(id=varb)
    obj.delete()
    return redirect('viewdoc')
def indexview(request):
    return render(request,'index.html')
    
    