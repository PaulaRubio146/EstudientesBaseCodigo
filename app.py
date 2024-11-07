from flask import Flask, render_template, request
from estudiante_dao import EstudianteDAO
from estudiante_dto import EstudianteDTO

app = Flask(__name__)

@app.route('/registrar_estudiante', methods=['GET', 'POST'])
def registrar_estudiante():
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        direccion_residencia = request.form['direccion_residencia']
        lat_residencia = float(request.form['lat_residencia'])
        lon_residencia = float(request.form['lon_residencia'])
        direccion_trabajo = request.form['direccion_trabajo']
        lat_trabajo = float(request.form['lat_trabajo'])
        lon_trabajo = float(request.form['lon_trabajo'])

        estudiante = EstudianteDTO(cedula, nombres, apellidos, direccion_residencia, (lat_residencia, lon_residencia), direccion_trabajo, (lat_trabajo, lon_trabajo))
        
        estudiante_dao = EstudianteDAO()
        estudiante_dao.insertar_estudiante(estudiante)

        return "Estudiante registrado correctamente!"
    return render_template('registro.html')

@app.route('/consulta')
def consulta():
    estudiante_dao = EstudianteDAO()
    estudiantes = estudiante_dao.obtener_estudiantes_con_distancia()
    return render_template('consulta.html', estudiantes=estudiantes)

if __name__ == "__main__":
    app.run(debug=False)

