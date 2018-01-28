from django.shortcuts import render

# Create your views here.
def compound_boxes(request):
    return render(request, 'sky_boxes/index.html')