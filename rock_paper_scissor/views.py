from django.shortcuts import render

# Create your views here.
def rock_paper_scissor(request):
    return render(request, 'rock_paper_scissor/index.html')