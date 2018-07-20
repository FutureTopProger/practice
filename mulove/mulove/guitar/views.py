from django.shortcuts import render



def index(request):
    return render(request, 'guitar/homeGuitar.html')

def search(request):
    print("========", request.GET.get('qwerty'))
    return render(request, 'guitar/homeGuitar.html')
# Create your views here.1
