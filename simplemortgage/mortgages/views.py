from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Mortgage


@login_required
def show_offers(request):
    mortgages = Mortgage.objects.filter(user=request.user)
    return render(request, "mortgages/show_offers.html", {"mortgages": mortgages})
