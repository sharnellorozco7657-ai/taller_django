# Taller: Endpoints en Django nativo

**Curso:** Desarrollo de aplicaciones Web I - 4E

## Verbos HTTP y CRUD

| Verbo | Operación CRUD | Caso de uso | Respuesta típica |
|---|---|---|---|
| GET | Read | Listar o consultar proyectos | 200 / 404 |
| POST | Create | Registrar un proyecto | 201 / 400 |
| PUT | Update | Actualizar un proyecto existente | 200 / 404 |
| DELETE | Delete | Eliminar un proyecto | 200 / 404 |

## Módulos, funciones y decoradores usados

| Elemento | Descripción |
|---|---|
| `django.views.View` | Clase base de las vistas basadas en clase; `dispatch()` llama al método según el verbo HTTP. |
| `as_view()` | Convierte la clase en una vista invocable para registrarla en las URLs. |
| `JsonResponse` | Respuesta HTTP que serializa datos a JSON. |
| `json.loads(request.body)` | Convierte el cuerpo JSON de la petición en un diccionario. |
| `csrf_exempt` | Desactiva la verificación CSRF para poder probar POST/PUT/DELETE desde clientes externos. |
| `method_decorator` | Aplica un decorador de función a una clase (`name='dispatch'`). |
| `path` / `include` | Definen las rutas y enlazan el `urls.py` de la app con el del proyecto. |
| `Model.objects` | ORM: `.values()`, `.get()`, `.create()`, `.save()`, `.delete()`. |
| `Model.DoesNotExist` | Excepción usada para responder 404. |

## Pruebas

Las peticiones están en `pruebas.http`.

![Pruebas CRUD](capturas/crud_final.png)

## Fuentes

- https://docs.djangoproject.com/en/stable/topics/class-based-views/intro/
- https://docs.djangoproject.com/en/stable/ref/class-based-views/base/
- https://docs.djangoproject.com/en/stable/ref/request-response/
- https://docs.djangoproject.com/en/stable/topics/http/urls/
- https://docs.djangoproject.com/en/stable/howto/csrf/
- https://developer.mozilla.org/es/docs/Web/HTTP/Methods