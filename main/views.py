from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Sekar Gandes Dianti',
        'class': 'PBP C'
    }
    return render(request, "main.html", context)