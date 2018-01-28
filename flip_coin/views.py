from django.shortcuts import render

# Create your views here.
def flip_coin(request):
    return render(request, 'dashboard/index.html')