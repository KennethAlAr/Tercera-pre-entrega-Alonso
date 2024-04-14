from django.urls import path

from .views import(
    join_game_form_view,
    create_game_form_view,
    create_sistema_form_view,
    home_view,
    list_view,
    search_view,
    search_with_form_view,
    detail_juego_view,
    detail_view
)

urlpatterns = [
    path("", home_view),
    path("detail/<reservas_id>", detail_view),
    path("list/", list_view, name="partidas-list"),
    path("buscar/<jugador>", search_view),
    path("buscar-con-formulario/", search_with_form_view, name="buscar-jugador-con-form"),
    path("unirse-con-formulario/", join_game_form_view, name="unirse-juego-con-form"),
    path("crear-juego-con-formulario/", create_game_form_view, name="crear-juego-con-form"),
    path("crear-sistema-con-formulario/", create_sistema_form_view, name="crear-sistema-con-form"),
    path("detail-juego/<juego_id>", detail_juego_view, name="detalle-partida")
]