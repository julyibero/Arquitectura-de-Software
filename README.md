# Actividad utilizando estructura Cliente-Servidor
# Proyecto de webapp de Almacenamiento en la Nube

## Descripción del Proyecto
Este proyecto implementa un servicio básico de almacenamiento en la nube utilizando Flask, un microframework de Python. La aplicación permite a los usuarios subir, descargar y eliminar archivos a través de una interfaz web simple y atractiva, utilizando la arquitectura Cliente-Servidor haciendo uso de peticiones HTTP.


## Estructura Cliente-Servidor

Este proyecto es un ejemplo claro de la arquitectura Cliente-Servidor, un modelo de diseño fundamental en el desarrollo de aplicaciones web y distribuidas. Aquí se detalla cómo se implementa esta estructura en nuestro proyecto:

## Framework a utilizar
Los frameworks pueden facilitar enormemente el desarrollo de aplicaciones cliente-servidor al proporcionar estructuras y herramientas predefinidas. Flask es un microframework de Python que es ligero, flexible y excelente para aprendices.
Elegimos Flask por varias razones:
  1. Es de código abierto y totalmente gratuito.
  2. Tiene una curva de aprendizaje suave, perfecto para estudiantes.
  3. Es muy flexible, permitiéndo añadir solo las funcionalidades que necesitemos.
  4. Tiene una gran comunidad y documentación extensa.
  5. Se integra bien con otras bibliotecas de Python.

Vamos a adaptar nuestro ejemplo anterior para usar Flask. Esto nos permitirá crear una API web para nuestro servicio de almacenamiento en la nube.
### Lado del Servidor (Flask Application)
- **Componente**: `app.py`
- **Funcionalidad**:
  1. Maneja las solicitudes HTTP entrantes.
  2. Procesa la lógica de negocio (subir, listar, descargar y eliminar archivos):
  4. Interactúa con el sistema de archivos para almacenar y recuperar datos.
  5. Genera respuestas dinámicas (HTML renderizado o archivos para descargar).
  6. Implementa las rutas y la lógica para cada operación.

### Lado del Cliente (Navegador Web)
- **Componente**: Interfaz web (HTML/CSS renderizado por el navegador) index.html
- **Funcionalidad**:
  1. Envía solicitudes al servidor (GET para cargar la página y descargar archivos, POST para subir y eliminar archivos).
  2. Renderiza la interfaz de usuario basada en el HTML/CSS proporcionado por el servidor.
  3. Maneja la interacción del usuario (selección de archivos, clics en botones).
  4. Muestra los resultados de las operaciones (lista actualizada de archivos, mensajes de éxito/error).

### Flujo de Comunicación Cliente-Servidor
1. El cliente (navegador) envía una solicitud HTTP al servidor (aplicación Flask).
2. El servidor procesa la solicitud:
   - Para solicitudes GET: Genera la página HTML con la lista de archivos.
   - Para solicitudes POST (subir/eliminar): Realiza la operación en el sistema de archivos y responde.
3. El servidor envía la respuesta HTTP al cliente.
4. El cliente (navegador) renderiza la respuesta (muestra la página o descarga el archivo).

### Ventajas de esta Arquitectura en el Proyecto
1. **Separación de Responsabilidades**: El servidor maneja la lógica y el almacenamiento, mientras que el cliente se encarga de la presentación.
2. **Escalabilidad**: Permite que múltiples clientes se conecten a un solo servidor.
3. **Mantenibilidad**: Cambios en la lógica del servidor no afectan directamente al cliente, y viceversa.
4. **Seguridad**: El servidor puede implementar medidas de seguridad centralizadas.
5. **Eficiencia**: El servidor puede manejar operaciones pesadas, mientras que el cliente se mantiene ligero.

## Montaje y Herramientas Utilizadas

### Estructura del Proyecto:
```
proyecto_cloud_storage/
├── app.py
├── cloud_storage/
└── templates/
    └── index.html
```

### Herramientas y Tecnologías:
1. **Python**: Lenguaje de programación principal.
2. **Flask**: Microframework web para Python. 
3. **HTML/CSS**: Para la interfaz de usuario.
4. **GitHub**: Para control de versiones y alojamiento del código.

### Pasos de Montaje:
1. Clonar el repositorio de GitHub.
2. Instalar las dependencias: `pip install flask`
3. Ejecutar la aplicación: `python app.py`
4. Acceder a `http://127.0.0.1:5000/` en un navegador web.

## Aplicación y Objetivo del Ejercicio

### Aplicación Práctica:
Este proyecto simula un servicio de almacenamiento en la nube básico, similar en concepto a servicios como Dropbox o Google Drive, pero a una escala muy simplificada. Puede ser utilizado como:
- Un sistema de almacenamiento personal para pequeños proyectos.
- Una herramienta educativa para enseñar conceptos de desarrollo web y manejo de archivos.
- Base para proyectos más complejos de gestión de archivos o aplicaciones web.

### Objetivos del Ejercicio:
1. **Implementar y Comprender la Arquitectura Cliente-Servidor**: Este proyecto demuestra claramente cómo se divide la funcionalidad entre el cliente (navegador web) y el servidor (aplicación Flask), ilustrando los principios fundamentales de esta arquitectura ampliamente utilizada en el desarrollo web y de aplicaciones distribuidas.
2. **Aplicar Conceptos de Desarrollo Web**: Utilizar HTML, CSS y Python en un contexto práctico.
3. **Manejar Operaciones de Archivos**: Implementar subida, descarga y eliminación de archivos en un entorno web.
4. **Crear una Interfaz de Usuario**: Diseñar una UI simple pero funcional con HTML y CSS.
5. **Practicar el Uso de Frameworks**: Familiarizarse con Flask y su integración con Python para desarrollo web.
6. **Implementar CRUD Básico**: Crear (subir), Leer (listar/descargar), Actualizar (no implementado en este ejemplo básico) y Eliminar archivos.
7. **Gestión de Proyectos**: Utilizar GitHub para el control de versiones y documentación del proyecto.
