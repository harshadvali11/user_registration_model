from django.shortcuts import render
from app.forms import *
# Create your views here.
def registration(request):
    uf=UserForm()
    pf=ProfileForm()
    d={'uf':uf,'pf':pf}
    return render(request,'registration.html',d)