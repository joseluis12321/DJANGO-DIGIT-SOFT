from django.shortcuts import render

# Vista para Equipo.html
def vista_equipo(request):
    return render(request, 'mi_app/Equipo.html')

# Vista para ServicioTecno.html
def vista_servicio_tecnico(request):
    return render(request, 'mi_app/serviciotecnico.html')


# Vista para Tecnicos.html
def vista_tecnicos(request):
    return render(request, 'mi_app/Tecnicos.html')

