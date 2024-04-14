from django.shortcuts import render

from .forms import ReservaCreateForm, ReservaSearchForm, JuegoCreateForm, SistemaCreateForm
from .models import Dado, Base, Sistema, Juego, Reserva

def join_game_form_view(request):
    if request.method == "GET":
        contexto = {"create_reserva_form": ReservaCreateForm()}
        return render(request, "partidas/join-game.html", contexto)
    elif request.method == "POST":
        form = ReservaCreateForm(request.POST)
        if form.is_valid():
            jugador = form.cleaned_data["jugador"]
            juego = form.cleaned_data["juego"]
            raza = form.cleaned_data["raza"]
            clase = form.cleaned_data["clase"]
            experiencia = form.cleaned_data["experiencia"]
            descripcion = form.cleaned_data["descripcion"]
            nueva_reserva = Reserva(
                jugador=jugador,
                juego=juego,
                raza=raza,
                clase=clase,
                experiencia=experiencia,
                descripcion=descripcion,
            )
            nueva_reserva.save()
            return detail_juego_view(request, juego.id)

def create_game_form_view(request):
    if request.method == "GET":
        contexto = {"create_form": JuegoCreateForm}
        return render(request, "partidas/form-create-juego.html", contexto)
    elif request.method == "POST":
        form = JuegoCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            disponible = form.cleaned_data["disponible"]
            numero_de_jugadores = form.cleaned_data["numero_de_jugadores"]
            sistema_de_juego = form.cleaned_data["sistema_de_juego"]
            descripcion = form.cleaned_data["descripcion"]
            fecha = form.cleaned_data["fecha"]
            hora_inicio = form.cleaned_data["hora_inicio"]
            hora_fin = form.cleaned_data["hora_fin"]
            nuevo_juego = Juego(
                nombre=nombre,
                disponible=disponible,
                numero_de_jugadores=numero_de_jugadores,
                sistema_de_juego=sistema_de_juego,
                descripcion=descripcion,
                fecha=fecha,
                hora_inicio=hora_inicio,
                hora_fin=hora_fin,
                )
            nuevo_juego.save()
            return detail_juego_view(request, nuevo_juego.id)

def create_sistema_form_view(request):
    if request.method == "GET":
        contexto = {"create_sistema_form": SistemaCreateForm}
        return render(request, "partidas/form-create-sistema.html", contexto)
    elif request.method == "POST":
        form = SistemaCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            dado = form.cleaned_data["dado"]
            base = form.cleaned_data["base"]
            descripcion = form.cleaned_data["descripcion"]
            nuevo_sistema = Sistema(
                nombre=nombre,
                dado=dado,
                base=base,
                descripcion=descripcion,
                )
            nuevo_sistema.save()
            return detail_sistema_view(request, nuevo_sistema.id)

def home_view(request):
    return render(request, "partidas/home.html")

def list_view(request):
    juegos = Juego.objects.all()
    contexto = {"todos_los_juegos": juegos}
    return render(request, "partidas/list.html", contexto)

def search_view(request, jugador):
    juegos_del_usuario = Juego.objects.filter(jugador=jugador)
    contexto = {"todos_los_juegos": juegos_del_usuario}
    return render(request, "partidas/list.html", contexto)

def search_with_form_view(request):
    if request.method == "GET":
        form = ReservaSearchForm()
        return render(request, "partidas/form-search.html", context={"search_form": form})
    elif request.method == "POST":
        form = ReservaSearchForm(request.POST)
        if form.is_valid():
            jugador = form.cleaned_data["jugador"]
        reservas_del_jugador = Reserva.objects.filter(jugador=jugador).all()
        contexto = {"todos_los_juegos": reservas_del_jugador}
        return render(request, "partidas/detail.html", contexto)

def detail_view(request, reservas_id):
    reserva = Reserva.objects.get(id=reservas_id)
    contexto = {"reserva": reserva}
    return render(request, "partidas/detail.html", contexto)

def detail_juego_view(request, juego_id):
    juego = Juego.objects.get(id=juego_id)
    contexto = {"juego": juego}
    return render(request, "partidas/detail-juego.html", contexto)

def detail_sistema_view(request, sistema_id):
    sistema = Sistema.objects.get(id=sistema_id)
    contexto = {"sistema": sistema}
    return render(request, "partidas/detail-sistema.html", contexto)