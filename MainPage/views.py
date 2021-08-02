from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import  Disease

import pandas as pd

#from sklearn.externals import joblib
import joblib
reloadModel=joblib.load('./models/model.pkl')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Prevention(request):
    return render(request,'Prevention.html')

def Symptoms(request):
    return render(request,'Symptoms.html')

def Treatment(request):
    return render(request,'Treatment.html')

def Causes(request):
    return render(request,'Causes.html')    
    
def predictHD(request):
    if request.method=='POST':
        temp={}
        name1=request.POST.get('name')
        temp['age']=float(request.POST.get('age'))
        temp['trestbps']=float(request.POST.get('trestbps'))
        temp['chol']=float(request.POST.get('chol'))
        temp['thalach']=float(request.POST.get('thalach'))
        temp['oldpeak']=float(request.POST.get('oldpeak'))

        sex=request.POST.get('sex')
        if sex=='m' or sex=='M' or sex=='male' or sex=='Male':
            temp['sex_0']=0
            temp['sex_1']=1
        elif sex=='f' or sex=='F' or sex=='female' or sex=='Female':
            temp['sex_0']=1
            temp['sex_1']=0
        else:
            temp['sex_0']=1
            temp['sex_1']=1
     
        cp=int(request.POST.get('cp'))
        if cp==0:
            temp['cp_0']=1
            temp['cp_1']=0
            temp['cp_2']=0
            temp['cp_3']=0
        elif cp==1:
            temp['cp_0']=0
            temp['cp_1']=1
            temp['cp_2']=0
            temp['cp_3']=0
        elif cp==2:
            temp['cp_0']=0
            temp['cp_1']=0
            temp['cp_2']=1
            temp['cp_3']=0
        else:
            temp['cp_0']=0
            temp['cp_1']=0
            temp['cp_2']=0
            temp['cp_3']=1



        temp['fbs_0']=int(request.POST.get('fbs_0'))

        restecg=int(request.POST.get('restecg'))
        if restecg==0:
            temp['restecg_0']=1
            temp['restecg_1']=0
            temp['restecg_2']=0
            
        elif restecg==1:
            temp['restecg_0']=0
            temp['restecg_1']=1
            temp['restecg_2']=0
           
        else:
            temp['restecg_0']=0
            temp['restecg_1']=0
            temp['restecg_2']=1

        exang=int(request.POST.get('exang'))
        if exang==0:
            temp['exang_0']=1
            temp['exang_1']=0
           
        else:
            temp['exang_0']=0
            temp['exang_1']=1

        slope=int(request.POST.get('slope'))
        if slope==0:
            temp['slope_0']=1
            temp['slope_1']=0
            temp['slope_2']=0
            
        elif slope==1:
            temp['slope_0']=0
            temp['slope_1']=1
            temp['slope_2']=0
           
        else:
            temp['slope_0']=0
            temp['slope_1']=0
            temp['slope_2']=1
   
        ca=int(request.POST.get('ca'))
        if ca==0:
            temp['ca_0']=1
            temp['ca_1']=0
            temp['ca_2']=0
            
        elif ca==1:
            temp['ca_0']=0
            temp['ca_1']=1
            temp['ca_2']=0
           
        else:
            temp['ca_0']=0
            temp['ca_1']=0
            temp['ca_2']=1

        thal=int(request.POST.get('thal'))
        if thal==1:
            temp['thal_1']=1
            temp['thal_2']=0
            temp['thal_3']=0
            
        elif thal==2:
            temp['thal_1']=0
            temp['thal_2']=1
            temp['thal_3']=0
           
        else:
            temp['thal_1']=0
            temp['thal_2']=0
            temp['thal_3']=1
        
    testDtaa=pd.DataFrame({'x':temp}).transpose()
    val=reloadModel.predict(testDtaa)[0]
    d1= Disease()
    d1.name=name1
    d1.val=val
    if d1.val==1:
        d1.msg="you have a some heart disease...Please consult to your doctor."
    else:
        d1.msg="your heart is healthy:)"
    return render(request,'index.html',{"d1":d1})
    

def Type(request):
    return render(request,'Types.html')