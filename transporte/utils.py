from functools import wraps
from django.shortcuts import redirect
from rest_framework_simplejwt.tokens import AccessToken

def requiere_token(vista_original):
    @wraps(vista_original)
    def wrapper(request, *args, **kwargs):
        token = request.COOKIES.get("access")

        if not token:
            return redirect("restriccion_autenticacion")

        try:
            AccessToken(token)  # Valida el token
        except Exception:
            return redirect("restriccion_autenticacion")

        return vista_original(request, *args, **kwargs)

    return wrapper

def requiere_staff(vista_original):
    @wraps(vista_original)
    def wrapper(request, *args, **kwargs):
        token = request.COOKIES.get("access")

        if not token:
            return redirect("restriccion_autenticacion")

        try:
            datos = AccessToken(token)
        except Exception:
            return redirect("restriccion_autenticacion")

        # Verificar si el usuario es staff
        if not datos.get("is_staff", False):
            return redirect("restriccion_autenticacion")

        return vista_original(request, *args, **kwargs)

    return wrapper
