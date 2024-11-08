
# Mi-primera-API creada Django Rest_Framework


Esta API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los usuarios (User) en la base de datos. El serializador (UserSerializer) se encarga de transformar los datos entre el modelo User y un formato JSON para que puedan ser enviados y recibidos a través de la API.

Explicación de cada componente y su función:

## ¿Qué hace el serializador?

El archivo serializers.py define el serializador que cumple las siguientes funciones:

Transforma el modelo User a JSON para que pueda ser enviado como respuesta a las solicitudes HTTP.

Valida y convierte datos JSON a objetos de modelo al recibir datos de una solicitud HTTP. Esto permite crear o actualizar un usuario en la base de datos con datos enviados en JSON.

Especifica los campos (fields = '__all__') que queremos incluir en el JSON. En este caso, todos los campos (age y name) se incluirán en el JSON.
views.py

Este archivo define las vistas de la API, que son funciones para gestionar las solicitudes de los usuarios y crear, leer, actualizar y eliminar datos en la base de datos.

get_users: Permite obtener una lista de todos los usuarios en la base de datos.

Usa UserSerializer(users, many=True) para serializar la lista completa de usuarios en formato JSON.
Response(serializer.data) envía el JSON al cliente que hace la solicitud.
create_user: Permite crear un nuevo usuario.

Recibe datos JSON, valida la información con serializer.is_valid(), y guarda el nuevo usuario si la validación es correcta.
Devuelve el usuario creado en formato JSON o errores de validación si hay problemas.
user_detail: Permite ver, actualizar o eliminar un usuario específico.

# GET: 
Serializa y devuelve los datos de un usuario específico.

# PUT: 
Recibe datos JSON para actualizar el usuario y guarda los cambios después de validar los datos.

# DELETE: 
Borra el usuario y devuelve un código 204, indicando que no hay contenido en la respuesta.


# URLs de la API
La configuración de URLs define las rutas para acceder a cada una de las vistas de la API:

/users/: Llama a get_users para listar todos los usuarios.
/users/create/: Llama a create_user para crear un nuevo usuario.
/users/<int:pk>: Llama a user_detail, permitiendo obtener, actualizar o eliminar un usuario específico por su ID.


# Subir A GitHub 

git add README.md  # Si solo modificaste el README
git add .


git commit -m "Actualización del README con explicación de la API"
git push origin main 