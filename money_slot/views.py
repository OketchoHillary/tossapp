from django.shortcuts import render

# Create your views here.
def money_slot(request):
    return render(request, 'money_slot/index.html')