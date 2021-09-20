# How To: JPG, PNG to WEBP

Para usar este `script` tenemos que hacer lo siguiente:
1. Clonar el repositorio dentro de la raiz del proyecto wordpress
1. Asegurarnos de tener `python3` y `virtualenv` instalados
1. Ejecutar el siguiente comando dentro del proyecto
    ```
    virtualenv .env && source .env/bin/activate && pip install -r requirements.txt
    ```
1. Correr el script (dentro del virtualenv). El script va a buscar todas las imagenes jpg o png dentro de la carpeta wp-content/uploads y las convertira a webp.
    ```
    python3 main.py
    ```
1. Podemos salir del `virtualenv` con el comando `deactivate` o simplemente cerrando la consola