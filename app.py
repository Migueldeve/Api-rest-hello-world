from flask import Flask, jsonify

"""En este caso, se crea una instancia de Flask y se define 
una ruta /home que devuelve un mensaje de cualquier cosa en formato JSON 
utilizando la función jsonify(). Además, se utiliza if __name__ == '__main__': 
para asegurarse de que el servidor solo se ejecute si se ejecuta 
el archivo app.py directamente."""

app = Flask(__name__)

@app.route('/home')
def home():
    return jsonify(
        {
        'name': 'software developer tutorial guide'
        },
        {
        'description': 'esta web se trata de mostrarte como se forma un developer junior y senior con guias de apredizajes, imagenes, mapas conceptuales, estructuras etc.'
        },
        {
        'background image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTldgLWUzn9NroelDsWPR6fPNo06MeCGAFRYQ&usqp=CAU'
        })

@app.route('/what-is-a-developer')
def what_is_a_developer():
    return jsonify(
        {
        'name': '¿que es un developer?'
        },
        {
        'description': 'Un programador es aquella persona que elabora programas de computadora, los profesionales que crean el software se denominan programadores y utilizan lenguajes de programación, dichos lenguajes son similares a idiomas que permitan entenderse con el ordenador y escribir instrucciones que generan nuevos programas.Es decir escribe, depura y mantiene el código fuente de un programa informático, que ejecuta el hardware de una computadora, para realizar una tarea determinada.Los programadores también son denominados desarrolladores de software, aunque estrictamente forman parte de un equipo de personas de distintas especialidades (mayormente informáticas), y siendo que el equipo es propiamente el desarrollador.La programación es una de las principales disciplinas dentro de la informática.'
        },
        {
        'background image': 'https://talently.tech/blog/wp-content/uploads/2021/11/%C2%BFCuanto-gana-un-programador-full-stack_-1200x900.png'
        })

@app.route('/types-of-developers')
def types_of_developers():
    return jsonify(
        {
        'name': 'tipos de developers'
        },
        {
        'background image': 'https://linube.com/blog/wp-content/uploads/desarrollo-web-min.jpg'
        })

@app.route('/programming-concepts')
def programming_concepts():
    return jsonify(
        {
        'name': 'conceptos de programación'
        },
        {
        'background image': 'https://static.vecteezy.com/system/resources/previews/002/178/149/original/developer-working-on-code-free-vector.jpg'
        },
        {
        'description': 'La programación es el proceso de diseñar, codificar, depurar y mantener el código fuente de un software para la computadora.'
        },
        {
        'conceptos-basicos': 'conceptos basicos'
        },
        {
        'concepto1': '1.Variables: una variable es un contenedor que almacena un valor que puede cambiar durante la ejecución del programa.'
        },
        {
        'concepto2': '2.Tipos de datos: los tipos de datos definen qué tipo de valores se pueden almacenar en una variable. Algunos ejemplos de tipos de datos son: entero (int), flotante (float), cadena de texto (string), booleano (bool), entre otros.'
        },
        {
        'concepto3': '3.Operadores: los operadores son símbolos que se utilizan para realizar operaciones en los valores de las variables. Algunos ejemplos de operadores son: + (suma), - (resta), * (multiplicación), / (división), % (módulo), entre otros.'
        },
        {
        'concepto4': '4.Estructuras de control: las estructuras de control se utilizan para controlar el flujo de ejecución del programa. Algunas de las estructuras de control más comunes son: if-else (si-entonces-sino), while (mientras), for (para), switch (seleccionar), entre otras.'
        },
        {
        'concepto5': '5.Funciones: una función es un bloque de código que realiza una tarea específica y puede ser llamado desde cualquier parte del programa.'
        },
        {
        'concepto6': '6.Arreglos: un arreglo es una colección de variables del mismo tipo que se almacenan juntas en la memoria. Cada elemento del arreglo se puede acceder a través de un índice.'
        },
        {
        'concepto7': '7.Clases y objetos: las clases son plantillas para crear objetos. Los objetos son instancias de una clase y pueden tener propiedades (variables) y métodos (funciones).'
        })

@app.route('/guides')
def guides():
    return jsonify(
        {
        'name': 'guias'
        },
        {
        'background image': 'https://thumbs.dreamstime.com/b/trabajo-de-programadores-programaci%C3%B3n-o-web-developer-coding-en-equipo-pantalla-con-script-c%C3%B3digo-y-ventanas-abiertas-208530984.jpg'
        },
        {
        'guide-1': 'lo basico'
        },
        {
        'link-pdf-1': 'https://publuu.com/flip-book/91038/252069'
        })


#manejo de errores

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Página no encontrada'}), 404

@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({'error': 'Método No Permitido'}), 405

if __name__ == '__main__':
    app.run(debug=True)