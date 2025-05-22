from flask import Flask, render_template, request, jsonify
import cotizar  # Importa tu módulo de cotización

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cotizar', methods=['POST'])
def cotizar_paquete():
    try:
        data = request.get_json()
        
        # Obtener datos del formulario
        paquete = data.get('paquete')
        personas = int(data.get('personas'))
        email = data.get('email')
        fecha = data.get('fecha')
        
        # Calcular cotización (usando tu módulo cotizar.py)
        precio = cotizar.calcular_precio(paquete, personas)
        
        # Puedes guardar esta cotización en una base de datos si lo deseas
        
        return jsonify({
            'status': 'success',
            'paquete': paquete,
            'personas': personas,
            'email': email,
            'fecha': fecha,
            'precio': precio
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)