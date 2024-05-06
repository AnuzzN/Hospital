from django.db import models

# Create your models here.
class patients(models.Model):
    fname=models.CharField(max_length=30,verbose_name='Name')
    disease=models.CharField(max_length=30)
    visitingdoctor=models.CharField(max_length=30)
class state(models.Model):
    statename=models.CharField(max_length=50)
    def __str__(self) ->str:
        return self.statename
    
    
    class meta:
        verbose_name_plural='state'
        
class district(models.Model):
    State=models.ForeignKey(state,on_delete=models.CASCADE)
    Name=models.CharField(max_length=30,verbose_name='District')
    def __str__(self) ->str:
        return self.Name
    
    
        