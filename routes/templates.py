from flask import Blueprint, render_template, request
import routes.fileProcess as fP
plantilla=Blueprint("plantilla", __name__)

@plantilla.route("/")
def retornaPlantilla():
    return render_template("cara1.html")

@plantilla.route("/rostro")
def cara2():
    return render_template("cara2.html")

@plantilla.route("/mano")
def manos():
    return render_template("manos.html")
@plantilla.route("/poses")
def poses():
    return render_template("cuerpos.html")

# templateFile=Blueprint("templateFile", __name__)
@plantilla.route("/pyexcel")
def index():
    data=fP.procesoDeExcel()
    return render_template("index.html", cabeza=data[0], cuerpo=data[1])
@plantilla.route("/process", methods=["POST"])
def process():
    
    data=fP.procesoExcelRender(
    request.form.get("numeroDeFilas"),
    request.form.get("numeroDeColumnas"),
    request.form.get("desdeLaFila"),
    request.form.get("hastaLaFila"),
    request.form.get("desdeLaColumna"),
    request.form.get("hastaLaColumna"),
    request.form.get("nPrimerasFilas"),
    request.form.get("nUltimasFilas"),
    request.form.get("soloLaFila"),
    request.form.get("soloLaColumna"),
    request.form.get("lasFilas"),
    request.form.get("lasColumnas")
    )
    return render_template("index.html" , cabeza=data[0], cuerpo=data[1])