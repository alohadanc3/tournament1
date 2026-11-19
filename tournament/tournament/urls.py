from django.contrib import admin
from django.urls import path
from app import views  # Импортируем ваши вьюшки из папки app

urlpatterns = [
    path('admin/', admin.site.urls),

    # Заменяем вызовы на классы с методом .as_view()
    path('', views.TournamentListView.as_view(), name='tournament_list'),
    path('create/', views.TournamentCreateView.as_view(), name='create_tournament'),
    path('register/<int:tournament_id>/', views.RegisterForTournamentView.as_view(), name='register_for_tournament'),
]




