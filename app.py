from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mi_llave_secreta_para_el_examen'

@app.route('/')
def formulario():
    
    return render_template('formulario.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    edad = int(request.form['edad'])
    genero = request.form['genero']
    nivel_actividad = request.form['nivel_actividad']

    tmb = 0
    if genero == 'hombre':
        tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
    elif genero == 'mujer':
        tmb = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

    factor = 1.0
    if nivel_actividad == 'sedentario':
        factor = 1.2
    elif nivel_actividad == 'ligero':
        factor = 1.375
    elif nivel_actividad == 'moderado':
        factor = 1.55
    elif nivel_actividad == 'alto':
        factor = 1.725
    
    get = tmb * factor

    session['tmb_resultado'] = tmb
    session['get_resultado'] = get

    return redirect(url_for('mostrar_resultado'))


@app.route('/resultado')
def mostrar_resultado():
    tmb = session.get('tmb_resultado', 0)
    get = session.get('get_resultado', 0)

    return render_template('resultado.html', tmb=tmb, get=get)

if __name__ == '__main__':
    app.run(debug=True)