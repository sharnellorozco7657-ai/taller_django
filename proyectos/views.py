# LIBRERIAS
import json
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Proyecto


# VISTA
@method_decorator(csrf_exempt, name="dispatch")
class ProyectoView(View):

    # READ
    def get(self, request, pk=None):
        if pk:
            try:
                p = Proyecto.objects.get(pk=pk)
            except Proyecto.DoesNotExist:
                return JsonResponse({"error": "No encontrado"}, status=404)
            return JsonResponse({"id": p.id, "nombre": p.nombre, "descripcion": p.descripcion})

        proyectos = list(Proyecto.objects.values())
        return JsonResponse(proyectos, safe=False)

    # CREATE
    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

        p = Proyecto.objects.create(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", ""),
        )
        return JsonResponse({"id": p.id, "mensaje": "Creado"}, status=201)

    # UPDATE
    def put(self, request, pk):
        try:
            p = Proyecto.objects.get(pk=pk)
        except Proyecto.DoesNotExist:
            return JsonResponse({"error": "No encontrado"}, status=404)

        data = json.loads(request.body)
        p.nombre = data.get("nombre", p.nombre)
        p.descripcion = data.get("descripcion", p.descripcion)
        p.save()
        return JsonResponse({"mensaje": "Actualizado"})

    # DELETE
    def delete(self, request, pk):
        try:
            p = Proyecto.objects.get(pk=pk)
        except Proyecto.DoesNotExist:
            return JsonResponse({"error": "No encontrado"}, status=404)

        p.delete()
        return JsonResponse({"mensaje": "Eliminado"})