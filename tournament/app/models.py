from django.db import models
from django.contrib.auth.models import User

class Tournament(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название турнира")
    description = models.TextField(verbose_name="Описание и правила")
    date = models.DateTimeField(verbose_name="Дата проведения")

    def __str__(self):
        return self.title


class Application(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="applications", verbose_name="Турнир")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Игрок")
    phone = models.CharField(max_length=20, verbose_name="Телефон для связи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подачи")

    class Meta:
        # Защита: один игрок может подать только одну заявку на конкретный турнир
        unique_together = ('tournament', 'user')

    def __str__(self):
        return f"Заявка от {self.user.username} на {self.tournament.title}"
