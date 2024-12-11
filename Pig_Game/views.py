from django.shortcuts import render


def play(request):
    context = {

    }
    return render(request, "Pig_Game.html", context)
