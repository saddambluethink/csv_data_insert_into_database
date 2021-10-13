from django.http import request
from django.shortcuts import redirect, render, HttpResponse

# for csv
from .models import csvmodel,csvfile
from .forms import csvform
# Create your views here
from django.contrib.auth import authenticate
import csv
import os

       # csv file data save in database or model
def uploadfile(request):
    form =csvform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        obj=csvfile.objects.filter(activated=False).first()
        print(obj.csv_file.url)
        print(obj.csv_file.path)
        with open(obj.csv_file.path, 'r') as f:
            reader=csv.reader(f)
            

            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    
                    print(row[1])  
                    print(row[2]) 
                    print(row[3]) 
                    print(row[4]) 
                    print(row[11]) 
                                       
                    print(type(row)) 
                    obj=csvmodel(EmployeeName=row[1],JobTitle=row[2],BasePay=row[3],OvertimePay=row[4],Agency=row[11])
                    # obj=activated=True
                    obj.save() 
                    if i==1:
                        break   
                             
            # return HttpResponse("file uploaded")
            return redirect('csvupload')
            
  
    return render(request,'csvupload.html',{'form':form})










           