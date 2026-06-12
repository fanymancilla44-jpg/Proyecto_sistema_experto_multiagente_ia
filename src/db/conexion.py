import sqlite3
from pathlib import Path


RUTA_BASE_DATOS = (
    Path(__file__).resolve().parents[2]
    / "database"
    / "animefull.db"
)


def conectar():
    RUTA_BASE_DATOS.parent.mkdir(parents=True, exist_ok=True)

    conexion = sqlite3.connect(RUTA_BASE_DATOS)

    return conexion