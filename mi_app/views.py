from django.shortcuts import render
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        errores = []

        if '@' not in email or '.' not in email:
            errores.append("Por favor, ingrese un correo electrónico válido.")

        if len(password) < 8:
            errores.append("La contraseña debe tener al menos 8 caracteres.")

        if errores:
            for error in errores:
                messages.error(request, error)
        else:
            messages.success(request, f'Bienvenido {email} ({role.capitalize()})')

    return render(request, 'mi_app/login.html')
