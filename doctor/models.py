from django.db import models

# Create your models here.
class doctors(models.Model):
    fname=models.CharField(max_length=30,verbose_name='Name')
    Specialisation=models.CharField(max_length=30)
    visitingtime=models.CharField(max_length=30)
class place(models.Model):
    placename=models.CharField(max_length=50)
    
    def __str__(self) ->str:
        return self.placename
    
    class meta:
        verbose_name_plural='Place'
class district(models.Model):
    Place=models.ForeignKey(place,on_delete=models.CASCADE)
    Name=models.CharField(max_length=50,verbose_name='District')
    
    def __str__(self):
        return self.Name
    
    
    
    
    
    

    