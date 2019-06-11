from django.shortcuts import render
from testapp import forms
# Create your views here.
def studentview(request):
    form=forms.studentform()
    return render(request,'testapp/studentregister.html',{'form':form})
