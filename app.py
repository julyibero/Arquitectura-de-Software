from flask import Flask, request, send_file, jsonify, render_template, redirect, url_for
import os

# Inicializa la aplicación Flask
app = Flask(__name__)

# Define la carpeta donde se almacenarán los archivos
UPLOAD_FOLDER = 'cloud_storage'
# Crea la carpeta si no existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Ruta principal que muestra la página de inicio
@app.route('/')
def index():
    # Obtiene la lista de archivos en la carpeta de almacenamiento
    files = os.listdir(UPLOAD_FOLDER)
    # Renderiza la plantilla index.html pasando la lista de archivos
    return render_template('index.html', files=files)

# Ruta para subir archivos
@app.route('/upload', methods=['POST'])
def upload_file():
    # Verifica si se ha enviado un archivo
    if 'file' not in request.files:
        return jsonify({"error": "No se ha seleccionado ningún archivo"}), 400
    file = request.files['file']
    # Verifica si se ha seleccionado un archivo
    if file.filename == '':
        return jsonify({"error": "No se ha seleccionado ningún archivo"}), 400
    if file:
        # Guarda el archivo en la carpeta de almacenamiento
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)
        # Redirige a la página principal
        return redirect(url_for('index'))

# Ruta para descargar archivos
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    # Verifica si el archivo existe
    if os.path.exists(filepath):
        # Envía el archivo para su descarga
        return send_file(filepath, as_attachment=True)
    else:
        # Retorna un error si el archivo no se encuentra
        return jsonify({"error": "Archivo no encontrado"}), 404

# Ruta para eliminar archivos
@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    # Verifica si el archivo existe
    if os.path.exists(filepath):
        # Elimina el archivo
        os.remove(filepath)
        # Redirige a la página principal
        return redirect(url_for('index'))
    else:
        # Retorna un error si el archivo no se encuentra
        return jsonify({"error": "Archivo no encontrado"}), 404

# Ruta para listar archivos (API)
@app.route('/list', methods=['GET'])
def list_files():
    # Obtiene la lista de archivos y la retorna en formato JSON
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify({"files": files})

# Ejecuta la aplicación si este script es el punto de entrada
if __name__ == '__main__':
    app.run(debug=True)