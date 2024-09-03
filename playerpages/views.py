from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Player
from .forms import FantasyTeamForm

# Create your views here.
def indexPageView(request) : 

    qbs = Player.objects.filter(POSITION='QB')[:5]
    for qb in qbs: 
        qb.PASS_YDS = round(qb.PASS_YDS)
        qb.PASS_TD = round(qb.PASS_TD, 1)
        qb.RUSH_YDS = round(qb.RUSH_YDS)
        qb.FPTS_G = round(qb.FPTS_G, 1)

    rbs = Player.objects.filter(POSITION='RB')[:5]
    for rb in rbs: 
        rb.RUSH_YDS = round(rb.RUSH_YDS)
        rb.RUSH_TD = round(rb.RUSH_TD, 1)
        rb.REC_YDS = round(rb.REC_YDS)
        rb.PPR_G = round(rb.PPR_G, 1)

    wrs = Player.objects.filter(POSITION='WR')[:5]
    for wr in wrs: 
        wr.REC = round(wr.REC)
        wr.REC_YDS = round(wr.REC_YDS)
        wr.REC_TD = round(wr.REC_TD, 1)
        wr.PPR_G = round(wr.PPR_G, 1)

    tes = Player.objects.filter(POSITION='TE')[:5]
    for te in tes: 
        te.REC = round(te.REC)
        te.REC_YDS = round(te.REC_YDS)
        te.REC_TD = round(te.REC_TD, 1)
        te.PPR_G = round(te.PPR_G, 1)
        

    personal_opinion = {
        "Patrick Mahomes II": "Just right", 
        "Lamar Jackson": "Just right", 
        "Dak Prescott": "Just right", 
        "Josh Allen": "<span style='color:red;'>Slightly high</span>", 
        "Jalen Hurts": "<span style='color:green;'>Slightly low</span>", 
        "Christian McCaffrey": "Just right", 
        "Breece Hall": "Just right", 
        "Bijan Robinson": "Just right", 
        "Saquon Barkley": "Just right", 
        "Jahmyr Gibbs": "Just right", 
        "CeeDee Lamb": "Just right", 
        "Tyreek Hill": "Just right", 
        "Amon-Ra St. Brown": "<span style='color:red;'>Slightly high</span>", 
        "Justin Jefferson": "<span style='color:green;'>Slightly low</span>", 
        "JaMarr Chase": "Just right", 
        "Sam LaPorta": "Just right", 
        "Travis Kelce": "<span style='color:red;'>Slightly high</span>", 
        "Trey McBride": "<span style='color:red;'>Slightly high</span>", 
        "Mark Andrews": "<span style='color:green;'>Slightly low</span>", 
        "Dalton Kincaid": "<span style='color:green;'>Slightly low</span>"
    }

    for player in qbs: 
        player.personal_opinion = personal_opinion.get(player.NAME, "No opinion")

    for player in rbs: 
        player.personal_opinion = personal_opinion.get(player.NAME, "No opinion")

    for player in wrs: 
        player.personal_opinion = personal_opinion.get(player.NAME, "No opinion")

    for player in tes: 
        player.personal_opinion = personal_opinion.get(player.NAME, "No opinion")

    context = {
        'qbs': qbs, 
        'rbs': rbs, 
        'wrs': wrs, 
        'tes': tes,
    }

    return render(request, 'playerpages/index.html', context)

def aboutPageView(request) : 
    return render(request, 'playerpages/about.html')

def playersPageView(request): 
    position = request.GET.get('position', 'QB')
    players = Player.objects.filter(POSITION=position)

    context = {
        'position': position, 
        'players': players,
    }
    return render(request, 'playerpages/players.html', context)

def methodologyPageView(request):
    return render(request, 'playerpages/methodology.html')

def fantasy_team_view(request):
    if request.method ==  'POST':
        form = FantasyTeamForm(request.POST)
        if form.is_valid():
            #Get the selected players
            selected_players = form.cleaned_data['players']
            context = {
                'players': selected_players,
            }
            return render(request, 'playerpages/myteam.html', context)
    else:
        form = FantasyTeamForm()

    return render(request, 'playerpages/fantasy_team_form.html', {'form': form})