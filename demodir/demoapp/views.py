
from django.shortcuts import render
from . models import place
from . models import review
  
  
def demo(request):
    obj=place.objects.all()
    obj1=review.objects.all()
    return render(request,"index.html",{'result':obj,'rev':obj1})
