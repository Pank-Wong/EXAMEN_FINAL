from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        if 18 <= edad <= 30:
            descuento_porcentaje = 15
        elif edad > 30:
            descuento_porcentaje = 25
        else:
            descuento_porcentaje = 0

        descuento = total_sin_descuento * (descuento_porcentaje / 100)
        total_con_descuento = total_sin_descuento - descuento

        return render_template('ejercicio1.html',
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               descuento=descuento,
                               total_con_descuento=total_con_descuento)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario == 'juan' and contrasena == 'admin':
            mensaje = 'Bienvenido Administrador juan'
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = 'Bienvenido Usuario pepe'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

        return render_template('ejercicio2.html', mensaje=mensaje)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)