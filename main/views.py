from django.shortcuts import render


# Create your views here.
def send_email(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'index.html')
