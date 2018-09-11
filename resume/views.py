from django.shortcuts import render, redirect
from .models import Portfolio
from tagging.views import TaggedObjectList


def resume(request):
    return render(request, 'resume/resume.html')


def portfolio(request):
    pfs = Portfolio.objects.all()
    return render(request, 'resume/portfolio.html', {'object_list': pfs})


class TagPortfolioView(TaggedObjectList):
    model = Portfolio
    template_name = 'resume/portfolio.html'
