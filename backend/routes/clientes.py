from flask import Blueprint, jsonify
from config.conexion import conectar

clientes_bp = Blueprint("clientes", __name__)


@clientes_bp.route("/api/clientes", methods=["GET"])
def obtener_clientes():
    conexion = conectar()

    if conexion is None:
        return jsonify({
            "success": False,
            "message": "No se pudo conectar a la base de datos"
        }), 500

    cursor = None

    try:
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT * FROM cliente")
        clientes = cursor.fetchall()

        return jsonify({
            "success": True,
            "clientes": clientes
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

    finally:
        if cursor:
            cursor.close()

        conexion.close()