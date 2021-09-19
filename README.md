# How To: JPG, PNG to WEBP

Para usar este `script` tenemos que hacer lo siguiente:
1. Clonar el repositorio
1. Asegurarnos de tener `python3` y `virtualenv` instalados
1. Ejecutar el siguiente comando dentro del proyecto
    ```
    virtualenv .env && source .env/bin/activate && pip install -r requirements.txt
    ```
1. Correr el script (dentro del virtualenv) y apuntar al path absoluto de, por ejemplo, los uploads de un sitio wordpress. El script va a buscar todas las imagenes jpg o png y las convertira a webp.
    ```
    python3 main.py /absolute/dir/to/uploads
    ```
1. El script va a generar un archivo `.zip` en el destino que hayamos elegido
    ```
    Zip file generated in ./uploads.zip
    ```
1. Podemos salir del `virtualenv` con el comando `deactivate` o simplemente cerrando la consola