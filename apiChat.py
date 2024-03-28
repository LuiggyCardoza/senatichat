from fastapi import FastAPI, Request, Form 
import mysql.connector
from mensaje import mensaje  
from fastapi.templating import Jinja2Templates



objMensaje = mensaje()
app = FastAPI()
miConexion = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="", 
    db="chat")

templates = Jinja2Templates(directory="/Pagina") 


@app.get("/")
def read_item(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.get("/enviarMensaje")
def enviarMensaje (mensaje: str):
    cursor = miConexion.cursor()
    mensajeEncriptado = objMensaje.codificar(mensaje)
    cursor.execute("insert into mensajes (Mensaje, Usuario) values('"+mensajeEncriptado+"','Luiggy')")
    miConexion.commit()
    return "Luiggy :"+mensaje

@app.get("/listarMensajes")
def listarMensajes():
	cursor = miConexion.cursor()
	cursor.execute("select * from mensajes")
	result = cursor.fetchall()
	return result

@app.get("/listarMensajesDeUnUsuario")
def listarMensajesDeUnUsuario(user1: str, user2: str):
    cursor = miConexion.cursor()
    cursor.execute("select * from mensajes where Usuario in('"+user1+"','"+user2+"')")
    result = cursor.fetchall()
    return result
  