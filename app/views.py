from django.shortcuts import render

# Create your views here.
def datarender(request):
    data="This data is our assumption data"
    d={'sunanda':data}
    return render(request,'datarender.html',context=d)
def login(request):
    d={'username':'anusri','age':3}
    return render(request,'login.html',context=d)
