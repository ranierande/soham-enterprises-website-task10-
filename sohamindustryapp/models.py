from django.db import models 
  
# declare a new model with a name "companyform" 
class companyform2(models.Model):
    name = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=50)  
    comment = models.CharField(max_length=1000)
    def __str__(self): 
        return self.name 

# form class has to define in forms.py file 
# not in models.py        