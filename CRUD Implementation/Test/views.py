from django.shortcuts import render
from django.http import HttpResponse
from .forms import DatabaseForm
from Test.models import Details
import json

def user(request):
    return render(request,'form.html')


def user_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']

        p = Details.objects.create(name=name,email=email,gender=gender,)

        queryset = Details.objects.all()
##        queryset = serializers.serialize('json',q)
        data = [{'name':database.name,'email':database.email,'gender':database.gender} for database in queryset]
        return HttpResponse(json.dumps(data),content_type="application/json")
    
