from flask import Flask, render_template, request

app = Flask(__name__)

citas_registradas = [
    {"cliente": "Carlos Mendoza", "telefono": "3154445566", "direccion": "Carrera 43 # 72-10", "barbero": "Angel 'Loko'", "servicio": "Combo Loko (Corte + Barba)", "fecha": "2026-05-28T14:30"}
]

servicios = [
    {"id": 1, "nombre": "Corte de Cabello Clásico", "precio": "$15.000", "descripcion": "Corte personalizado a tijera o máquina, lavado y acabado con pomada de lujo."},
    {"id": 2, "nombre": "Perfilado de Barba Ritual", "precio": "$12.000", "descripcion": "Diseño detallado de barba, afeitado con navaja tradicional y toalla caliente."},
    {"id": 3, "nombre": "Combo Loko (Corte + Barba)", "precio": "$25.000", "descripcion": "El tratamiento insignia de la casa con exfoliación facial y masaje de cortesía."}
]

barberos = ["Angel 'Loko'", "Carlos Ortiz"]

@app.route('/')
def home():
    horarios = [
        {"dias": "Lunes a Viernes", "horas": "9:00 AM - 8:00 PM"},
        {"dias": "Sábados", "horas": "8:00 AM - 9:00 PM"},
        {"dias": "Domingos", "horas": "Cerrado"}
    ]
    return render_template('index.html', servicios=servicios, barberos=barberos, horarios=horarios)

@app.route('/guardar_reserva', methods=['POST'])
def guardar_reserva():
    nombre = request.form.get('nombre')
    telefono = request.form.get('telefono')
    direccion = request.form.get('direccion')
    barbero = request.form.get('barbero')
    servicio = request.form.get('servicio')
    fechahora = request.form.get('fechahora')
    
    for cita in citas_registradas:
        if cita['barbero'] == barbero and cita['fecha'] == fechahora:
            return render_template('ocupado.html', barbero=barbero, fecha=fechahora.replace('T', ' a las '))
            
    citas_registradas.append({
        "cliente": nombre, "telefono": telefono, "direccion": direccion,
        "barbero": barbero, "servicio": servicio, "fecha": fechahora
    })
    
    return render_template('exito.html', cliente=nombre)

@app.route('/panel_loko')
def panel_control():
    return render_template('panel.html', citas=citas_registradas)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
