from django import forms

from .models import Sistema, Juego, Reserva

class ReservaSearchForm(forms.Form):
    jugador = forms.CharField(max_length=50, required=True, label="Ingresar nombre de jugador")

class ReservaCreateForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            "jugador",
            "juego",
            "raza",
            "clase",
            "experiencia",
            "descripcion",
        ]
        labels = {
            "jugador": "Nombre del jugador",
            "juego": "Partida a la que te quieres unir",
            "raza": "Raza de tu personaje",
            "clase": "Clase de tu personaje",
            "experiencia": "Experiencia en el sistema de juego",
            "descripcion": "Descripción de tu personaje",
        }


class JuegoCreateForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = [
            "nombre", 
            "disponible",
            "numero_de_jugadores",
            "sistema_de_juego",
            "descripcion",
            "fecha",
            "hora_inicio",
            "hora_fin",
        ]    
        labels = {
            "nombre": "Elegir nombre del juego",
            "disponible": "Disponible",
            "capacidad": "Número de jugadores",
            "descripcion": "Descripción de la partida",
            "sistema_de_juego": "Sistema de juego",
            "fecha": "Fecha",
            "hora_inicio": "Hora de inicio",
            "hora_fin": "Hora de final"
        }

class SistemaCreateForm(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = [
            "nombre",
            "dado",
            "base",
            "descripcion",
        ]
        labels = {
            "nombre": "Nombre del sistema de juego",
            "dado": "Tipo de dado que utiliza el sistema",
            "base": "Base del sistema",
            "descripcion": "Descripción del sistema de juego"
        }