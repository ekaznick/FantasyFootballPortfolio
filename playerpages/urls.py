from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import playersPageView
from .views import methodologyPageView
from .views import fantasy_team_view

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("about", aboutPageView, name="about"), 
    path("players", playersPageView, name="players"),
    path("methodology", methodologyPageView, name="methodology"),
    path("fantasy-team", fantasy_team_view, name="fantasy_team"),
]

