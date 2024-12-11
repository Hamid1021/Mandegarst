from django.shortcuts import render, get_object_or_404
from application.models import Game, Banner
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Game


def home(request):
    highest_rate = Game.objects.get_highest_rate()
    latest_game = Game.objects.get_latest_games()
    top_banner = Banner.objects.get_first_top_banner()
    context = {
        "highest_rate":highest_rate,
        "latest_game":latest_game,
        "top_banner":top_banner,
    }
    return render(request, "index.html", context)


def single_game(request, game_id, game_name):
    game = get_object_or_404(Game, pk=game_id, game_name=game_name)
    context = {
        'object': game
    }
    return render(request, 'download.html', context)


def all_games(request):
    result_per_page = 6
    games_list = Game.objects.all()
    paginator = Paginator(games_list, result_per_page)  # Show 10 games per page
    top_banner = Banner.objects.get_first_top_banner()
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        "top_banner":top_banner,
    }
    return render(request, 'all_games.html', context)


def online_game_all(request):
    context = {

    }
    return render(request, "online_game.html", context)


def online_game_one(request):
    context = {

    }
    return render(request, "05-Guess-My-Number/index.html", context)


def online_game_tow(request):
    context = {

    }
    return render(request, "07-Pig-Game/index.html", context)


def online_game_three(request):
    context = {

    }
    return render(request, "snake-master/index.html", context)
