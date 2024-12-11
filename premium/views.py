from django.shortcuts import render
from premium.models import PremiumCode

def premium(request):
    p_code = PremiumCode.objects.filter(is_active=True).first()
    context = {
        "p_code": p_code,
    }
    return render(request, "premium.html", context)