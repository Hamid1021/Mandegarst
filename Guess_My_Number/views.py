from django.shortcuts import render

def play(request):
    context = {

    }
    return render(request, "Guess_My_Number.html", context)
