from django.db import models

# Create your models here

# for csv file upload
class csvfile(models.Model):
    csv_file = models.FileField() 
    activated=models.BooleanField(default=False)

    def __str__(self):
        return f"File id:{self.id}"

class csvmodel(models.Model):
    EmployeeName=models.CharField(max_length=50)
    JobTitle=models.CharField(max_length=50)
    BasePay=models.FloatField()
    OvertimePay=models.FloatField()
    Agency=models.CharField(max_length=100)

    def __str__(self):
        return self.EmployeeName
    
    

     