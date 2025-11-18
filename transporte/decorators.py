from django.shortcuts import render
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

def jwt_required(view_func):
    def wrapper(request, *args, **kwargs):

        access = request.COOKIES.get("access")
        refresh = request.COOKIES.get("refresh")

        # Caso 1: no hay token → iniciar sesión
        if not access:
            return render(request, "transporte/require_login.html")

        try:
            # Intentar validar el access token
            AccessToken(access)

        except TokenError:
            # Access expirado o inválido → intentar renovar
            if refresh:
                try:
                    new_refresh = RefreshToken(refresh)
                    new_access = new_refresh.access_token

                    # Creamos respuesta para agregar nueva cookie
                    response = view_func(request, *args, **kwargs)
                    response.set_cookie(
                        "access", str(new_access),
                        httponly=True, secure=False, samesite="Lax"
                    )
                    return response

                except TokenError:
                    # Refresh inválido o expirado → sesión expirada
                    return render(request, "transporte/session_expired.html")

            # No hay refresh → iniciar sesión
            return render(request, "transporte/session_expired.html")

        # Access válido → entrar directamente
        return view_func(request, *args, **kwargs)

    return wrapper
