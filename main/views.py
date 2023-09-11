from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Sekar Gandes Dianti',
        'class': 'PBP D'
    }
    return render(request, "main.html", context)