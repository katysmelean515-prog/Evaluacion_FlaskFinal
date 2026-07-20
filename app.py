from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal con los dos botones
@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1: Cálculo de compras de pintura
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        
        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario
        
        # Lógica de descuentos según la edad
        if edad >= 18 and edad <= 30:
            porcentaje_descuento = 0.15
        elif edad > 30:
            porcentaje_descuento = 0.25
        else:
            porcentaje_descuento = 0.0
            
        descuento = total_sin_descuento * porcentaje_descuento
        total_pagar = total_sin_descuento - descuento
        
        return render_template('ejercicio1.html', 
                               nombre=nombre, 
                               total_sin_descuento=total_sin_descuento, 
                               descuento=descuento, 
                               total_pagar=total_pagar,
                               calculado=True)
                               
    return render_template('ejercicio1.html', calculado=False)

# Ejercicio 2: Inicio de sesión
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        
        # Validación de usuarios
        if usuario == 'juan' and password == 'admin':
            mensaje = f"Bienvenido administrador {usuario}"
        elif usuario == 'pepe' and password == 'user':
            mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"
            
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)