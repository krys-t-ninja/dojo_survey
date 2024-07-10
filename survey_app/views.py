from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def success(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'location': request.POST['location'],
            'language': request.POST['language'],
            'comment': request.POST['comment']
        }
        return render(request, 'success.html', context)