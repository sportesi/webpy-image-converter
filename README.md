# How to Build Webpy

Para compilar este `script` tenemos que hacer lo siguiente:
1. Clonar el repositorio
1. Asegurarnos de tener `docker` instalado
1. Compilar la imagen usando el comando
    ```
    docker build -t webpy:latest .
    ```
1. Correr un container mapeando el codigo fuente al mismo
    ```
    cd webpy-image-converter
    docker run -it -v $PWD:/root/app webpy:latest sh
    ```
1. Dentro del container crear el entorno virtual e instalar las dependencias
    ```
    cd /root/app
    virtualenv .env && source .env/bin/activate && pip install -r requirements.txt
    ```
1. Compilar el ejecutable con `pyinstaller`
    ```
    pyinstaller main.py --onefile
    ```

<br />

---

<br />

# How to Run Webpy
1. Copiarse el archivo `dist/main` en la raiz del proyecto **Wordpress** que necesitemos convertir.
1. Correr el script. El script va a buscar todas las imagenes jpg o png dentro de la carpeta wp-content/uploads y las convertira a webp.
    ```
    ./main
    ```