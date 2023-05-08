

# Create your views here.

from datetime import datetime


from django.http import HttpResponse
from django.shortcuts import render 


# Create your views here.

def About(request):
    #gives time
    #cur_time= datetime.now().strftime("%d/%m/%Y , %H:%M:%S")
    #html = "<html><body>It is now %s</body></html>" %cur_time
    #return HttpResponse(html)

    #context for render
    #context = {
   #     'cur_time': cur_time
   # } 
    return render(request,'Blog/detail.html')#,context)
#,cur_time


def Experience(request):
    return render(request,'Blog/Experience.html') 

def Education(request):
    return render(request,'Blog/Education.html') 

def Skills(request):
    return render(request,'Blog/Skills.html') 

def Projects(request):
    return render(request,'Blog/Projects.html') 

def Interests(request):
    return render(request,'Blog/Interests.html') 