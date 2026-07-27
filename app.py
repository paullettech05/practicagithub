from flask import Flask
from basedatos import mysql

from rutas.acceso import acceso
from rutas.admin import admin
from rutas.cliente import cliente

app = Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_User"]="root"
app.config["MYSQL_PASWORD"]=""
app.config["MYSQL_BD"]="renta_vehiculos"

mysql.init_app(app)

app.register_blueprint(acceso)
app.register_blueprint(admin)
app.register_blueprint(cliente)

if __name__ == "__main__":
 app.run(debug=True)
