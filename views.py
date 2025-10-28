from django.shortcuts import render
from .models import Laptops
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_user(req):
    names=req.POST.get("name")
    models=req.POST.get("model")
    costs=req.POST.get("cost")
    
    lap=Laptops.objects.create(name=names,model_name=models,cost=costs)
    lap.save()
    return HttpResponse("user_added Succesfully")


def get_user(req):

    data=Laptops.objects.all()
    return HttpResponse(data.values())

@csrf_exempt
def update_user(req):
    
    user_data=json.loads(req.body)
    lap_name=user_data["lap_name"]
    model_names=user_data["model"]
    cost_p=user_data["cost"]

    new_data=Laptops.objects.create(name=lap_name,model_name=model_names,cost=cost_p)
    return HttpResponse("user added succesfully")

@csrf_exempt
def edit_user(req,id):

    edit_user_=Laptops.objects.get(id=id)

    user_data=json.loads(req.body)

    name=user_data["name"]
    model=user_data["model"]
    cost=user_data["cost"]


    edit_user_.name=name
    edit_user_.model_name=model
    edit_user_.cost=cost
    edit_user_.save()
    return HttpResponse("user edited succesfully")

@csrf_exempt

def delete_user(req,id):
     if req.method=='DELETE':
        try:
            coder=Laptops.objects.get(id=id)

            coder.delete()
            
            return HttpResponse("user deleted succesfully")
        except:
            return HttpResponse("user not found")