from flask import Flask, render_template  # Importa la clase Flask y la función render_template desde el paquete flask

app = Flask(__name__)  # Crea la aplicación Flask; __name__ ayuda a localizar recursos y plantillas

# Datos de ejemplo para las películas:
# Diccionario donde cada clave es una categoría y su valor es una lista de diccionarios (películas)
peliculas = {
    'suspenso': [
        {'titulo': 'la ventana secreta',
         'sinopsis': 'Tras seis meses, el protagonista se ha separado de su mujer y aparece sumido en una depresión y '
         'dejadez continua. Johnny Depp interpreta un personaje pacífico, tímido, depresivo e introvertido.'},
        {'titulo': 'Perdida',
         'sinopsis': 'Un hombre se convierte en el principal sospechoso cuando su esposa desaparece.'},
    ],
    'terror': [
        {'titulo': 'el resplandor',
         'sinopsis': 'La película relata la historia de Jack Torrance, un escritor que acepta un puesto '
         'como vigilante de invierno en un solitario hotel de alta montaña para ocuparse del mantenimiento. '},
        {'titulo': 'Hereditary',
         'sinopsis': 'Una familia es atormentada tras la muerte de su matriarca.'},
    ],
    'romance': [
        {'titulo': 'Diario de una pasión',
         'sinopsis': 'Noa le lee el diario a Allie en una sala de hospital. Allie tiene un momento de lucidez'
         ' recuerda su vida juntos y mueren pacíficamente tomados de la mano, seguidos por una bandada de pájaros'
         ' volando sobre el lago.'},
        {'titulo': 'La La Land',
         'sinopsis': 'Un pianista de jazz y una aspirante a actriz persiguen sus sueños en Los Ángeles.'},
    ],
    'infantil': [
        {'titulo': 'shrek',
         'sinopsis': 'La trama de Shrek gira en torno a un ogro solitario que ve interrumpida '
         'su paz cuando criaturas de cuentos de hadas son exiliadas a su pantano por el malvado Lord Farquaad.'},
        {'titulo': 'Mi Vecino Totoro',
         'sinopsis': 'Dos hermanas se mudan al campo y se hacen amigas de un espíritu del bosque.'},
    ],
}


@app.route('/')  # Define la ruta raíz (http://localhost:5000/)
def index():
    return render_template('index.html')  # Renderiza la plantilla templates/index.html para la página principal


@app.route('/suspenso')  # Define la ruta /suspenso
def suspenso():
    # Pasa la lista de películas de la categoría 'suspenso' a la plantilla suspenso.html
    return render_template('suspenso.html', peliculas=peliculas['suspenso'])


@app.route('/terror')  # Define la ruta /terror
def terror():
    # Pasa la lista de películas de la categoría 'terror' a la plantilla terror.html
    return render_template('terror.html', peliculas=peliculas['terror'])


@app.route('/romance')  # Define la ruta /romance
def romance():
    # Pasa la lista de películas de la categoría 'romance' a la plantilla romance.html
    return render_template('romance.html', peliculas=peliculas['romance'])


@app.route('/infantil')  # Define la ruta /infantil
def infantil():
    # Pasa la lista de películas de la categoría 'infantil' a la plantilla infantil.html
    return render_template('infantil.html', peliculas=peliculas['infantil'])


if __name__ == '__main__':  # Comprueba si se ejecuta este archivo directamente (no importado)
    app.run(debug=True)  # Inicia el servidor de desarrollo con recarga automática y modo debug activado