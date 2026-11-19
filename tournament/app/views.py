from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tournament, Application


# 1. Отображение списка турниров (вместо функции tournament_list)
class TournamentListView(ListView):
    model = Tournament
    template_name = 'tournaments/list.html'
    context_object_name = 'tournaments'  # Переменная, которая полетит в HTML-шаблон


# 2. Создание нового турнира (вместо функции create_tournament)
class TournamentCreateView(LoginRequiredMixin, CreateView):
    model = Tournament
    template_name = 'tournaments/create.html'
    fields = ['title', 'description', 'date']  # Поля модели, которые будут в форме
    success_url = reverse_lazy('tournament_list')  # Куда перенаправить после успешного создания


# 3. Регистрация на турнир (вместо функции register_for_tournament)
class RegisterForTournamentView(LoginRequiredMixin, View):
    def post(self, request, tournament_id):
        tournament = get_object_or_404(Tournament, id=tournament_id)

        # Создаем заявку, если её еще нет
        Application.objects.get_or_create(
            tournament=tournament,
            user=request.user,
            defaults={'phone': "+380000000000"}
        )
        return redirect('tournament_list')
