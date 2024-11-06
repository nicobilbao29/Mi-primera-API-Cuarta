# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer  # Importa el serializador
from django.http import HttpResponse


@api_view(['GET'])
def get_users(request):
    # Obtén todos los usuarios
    users = User.objects.all()  # Cambié 'object' a 'objects'
    serializer = UserSerializer(users, many=True)  # Serializa múltiples objetos
    return Response(serializer.data)  # Retorna los datos serializado

   #return Response(UserSerializer({'name':"pedro","age":23}).data)
   
    

   
@api_view(['POST'])
def create_user(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# cuando quierea trabajar  actualizar o eliminar, necesito acceder a un usuario especifico atravez del id  
# primero debo buscarlo a travz de la PK
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
        
    
    
    
    
    
    
#@api_view(['GET'])
#def api_home(request):
 #   return Response({
  #      "message": "Bienvenido a la API de ventas",
   #     "endpoints": {
    #        "/users/": "Obtener lista de usuarios",
     #       "/users/<id>/": "Obtener, actualizar o eliminar un usuario específico",
      #      "/users/create/": "Crear un nuevo usuario",
       # }
    #})
    
    

# api/views.py
from django.http import HttpResponse



def api_home(request):
    html_content = """
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    margin: 0;
                    padding: 0;
                }
                h1 {
                    color: #2C3E50;
                    font-size: 36px;
                    text-align: center;
                    margin-top: 50px;
                }
                p {
                    color: #34495E;
                    font-size: 18px;
                    text-align: center;
                }
                ul {
                    list-style-type: none;
                    padding: 0;
                    text-align: center;
                }
                li {
                    background-color: #2980B9;
                    color: white;
                    padding: 10px;
                    margin: 10px 0;
                    font-size: 18px;
                    border-radius: 5px;
                    width: 300px;
                    margin-left: auto;
                    margin-right: auto;
                    transition: background-color 0.3s ease;
                }
                li:hover {
                    background-color: #3498DB;
                }
                strong {
                    color: #E74C3C;
                }
                .example {
                    font-weight: bold;
                    color: #E67E22;
                }
            </style>
        </head>
        <body>
            <h1>Bienvenido a la Primerta  API de Nicolás</h1>
            <p>Accede a los endpoints colocando <strong>api/</strong> antes de cada ruta.</p>
            <p class="example">Ejemplo: <strong>/api/users/</strong></p>
            <p>Endpoints disponibles:</p>
            <ul>
                <li><strong>/api/users/</strong>: Obtener lista de usuarios</li>
                <li><strong>/api/users/&lt;id&gt;/</strong>: Obtener, actualizar o eliminar un usuario específico</li>
                <li><strong>/api/users/create/</strong>: Crear un nuevo usuario</li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(html_content)
