from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tournament, Application

def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'tournaments/list.html', {'tournaments': tournaments})

@login_required
def register_for_tournament(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    if request.method == 'POST':
        # Создаем заявку, если её еще нет (телефон можно взять дефолтный или пустой)
        Application.objects.get_or_create(tournament=tournament, user=request.user, phone="+380000000000")
    return redirect('tournament_list')
