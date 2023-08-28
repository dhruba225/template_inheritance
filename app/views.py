from django.shortcuts import render

# Create your views here.
def parents(request):
    return render(request,'parents.html')

def child(request):
    return render(request,'child.html')
