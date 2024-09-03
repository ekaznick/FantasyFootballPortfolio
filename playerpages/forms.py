from django import forms
from .models import Player

class FantasyTeamForm(forms.Form):
    player = forms.ModelMultipleChoiceField(
        queryset=Player.objects.all(), 
        widget=forms.CheckboxSelectMultiple, 
        required=True
    )