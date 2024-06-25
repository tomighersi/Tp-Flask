from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Creo la primer ruta basica, que renderiza la plantilla de index
@app.route('/')
def home():
    return render_template('index.html')

#Lista de Productos
productos = [
    {"id": 1, "nombre": "Iphone 14", "categoria": "Celulares"},
    {"id": 2, "nombre": "LG SMART 42 Pulgadas", "categoria": "Televisores"}
]

#Ruta que renderiza la lista de productos
@app.route("/productos")
def lista_productos():
    return render_template("productos.html", productos=productos) #Aca digamos que paso la lista de productos para que se pueda usar en plantilla

#Ruta de agregar productos
@app.route("/agregar_producto", methods=["GET", "POST"])
def agregar_producto():
    if request.method == 'GET':
        print('es un Get')

    if request.method == "POST":
        nuevo_producto = {
            "id": len(productos) + 1,
            "nombre": request.form["nombre"],
            "categoria": request.form["categoria"]
        }
        productos.append(nuevo_producto)
        return redirect(url_for("lista_productos")) #Al agregar un producto, te redirecciona a la lista de productos actualizada con el que se agrego
    return render_template("agregar_producto.html")

#Depurador para ver si hay errores y en donde se encuentran

if __name__ == '__main__':
    app.run(debug=True) 
