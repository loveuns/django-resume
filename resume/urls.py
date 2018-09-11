from django.urls import path
from .views import *

app_name = 'resume'
urlpatterns = [
    path('', resume, name='resume'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/<tag>/', TagPortfolioView.as_view(), name='portfolio_tag'),
]
