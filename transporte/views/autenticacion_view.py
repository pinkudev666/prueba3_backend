from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
def restriccion_autenticacion(request): 
    return render(request, "transporte/restriccion_autenticacion.html")
def inicio_sesion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            # 🔹 Inicia sesión en Django
            login(request, user)

            # 🔹 Genera tokens JWT
            refresh = RefreshToken.for_user(user)

            response = redirect("inicio")

            # 🔹 Guarda tokens en cookies
            response.set_cookie(
                "access", str(refresh.access_token),
                httponly=True, secure=False, samesite="Lax"
            )
            response.set_cookie(
                "refresh", str(refresh),
                httponly=True, secure=False, samesite="Lax"
            )

            return response

        return render(request, "transporte/inicio_sesion.html", {
            "error": "Usuario o contraseña incorrectos"
        })

    return render(request, "transporte/inicio_sesion.html")


def cerrar_sesion(request):
    # 🔹 Cierra sesión Django
    logout(request)

    # 🔹 Limpia cookies
    response = redirect("inicio")
    response.delete_cookie("access")
    response.delete_cookie("refresh")
    return response
