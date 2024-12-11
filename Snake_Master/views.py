from django.shortcuts import render


def play(request):
    context = {

    }
    return render(request, "Snake_Master.html", context)


def death(request):
    context = {

    }
    return render(request, "pages/maze/death.html", context)

def keep(request):
    context = {

    }
    return render(request, "pages/maze/keep.html", context)

def limitless(request):
    context = {

    }
    return render(request, "pages/maze/limitless.html", context)

def sneak(request):
    context = {

    }
    return render(request, "pages/maze/sneak.html", context)

def watch(request):
    context = {

    }
    return render(request, "pages/maze/watch.html", context)

def difficulty(request):
    context = {

    }
    return render(request, "pages/difficulty.html", context)

def difficultyDefault(request):
    context = {

    }
    return render(request, "pages/difficultyDefault.html", context)

def instruction(request):
    context = {

    }
    return render(request, "pages/instruction.html", context)