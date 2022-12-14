import tkinter
from tkinter import *

# Crea listas para guardar las peliculas y los clientes
movie_files = []
client_files = []

# Registra la pelicula
def register_movie(name, code, genre, price):#Recibe el nombre, el codigo, el genero y el precio de la pelicula
    film = Movie()#Crea un objeto "Movie"
    film.__int__(name, code, genre, price)#Escribe los datos dentro del objeto "Movie"

    return film #Retorna el objeto creado

def register_movie1(name, code, genre, price,rented):#Recibe el nombre, el codigo, el genero y el precio de la pelicula
    film = Movie()#Crea un objeto "Movie"
    film.__int1__(name, code, genre, price,rented)#Escribe los datos dentro del objeto "Movie"

    return film #Retorna el objeto creado

# Registra el cliente
def register_client(name, id):#Recibe el nombre y la cedula del cliente
    client = Client()#Crea un objeto "Client"
    client.__int__(name, id)#Escribe los datos dentro del objeto "Client"

    return client #Retorna el objeto creado

# Registra el cliente
def register_client1(name, id, list):#Recibe el nombre y la cedula del cliente
    client = Client()#Crea un objeto "Client"
    client.__int1__(name, id, list)#Escribe los datos dentro del objeto "Client"

    return client #Retorna el objeto creado

class Movie: #Clase "Movie"

    def __int__(self, name, code, genre, price): #Crea los datos de la clase
        self.Movie_name = name
        self.Movie_code = code
        self.Movie_genre = genre
        self.Movie_price = price
        self.Movie_is_rented = False

    def __int1__(self, name, code, genre, price, bol): #Crea los datos de la clase
        self.Movie_name = name
        self.Movie_code = code
        self.Movie_genre = genre
        self.Movie_price = price
        self.Movie_is_rented = bol
    def is_rented(self): #Cambia el estado de no alquilado a alquilado
        self.Movie_is_rented = True

    def not_rented(self): #Cambia el estado de alquilado a no alquilado
        self.Movie_is_rented = False


class Client: #Clase "Client"

    def __int__(self, name, id, ): #Crea los datos de la clase
        self.Client_name = name
        self.Client_id = id
        self.Client_movie_rented = []

    def __int1__(self, name, id, list): #Crea los datos de la clase
        self.Client_name = name
        self.Client_id = id
        self.Client_movie_rented = list

    def rent_movie(self, movie_code): #Asigna una pelicula alquilada
        self.Client_movie_rented.append(movie_code)

    def return_movie(self,movie_code): #Devuelve una pelicula y la elimina
        for i in range(0, len(movie_files)):
            if self.Client_movie_rented[i] == movie_code:
                self.Client_movie_rented.pop(i)
                break


def save_client(): #Guarda los clientes
    #Obtiene los datos de los Entry
    name = entry_nameC.get() + " " + entry_lastnameC.get()
    id = entry_idC.get()
    client_files.append(register_client(name, id))#Llama a la funcion registrar cliente y la guarda en la lista
    client_write = open('clients.txt', 'a')
    client_write.write(client_files[-1].Client_id + '\n')
    client_write.write(client_files[-1].Client_name + '\n')
    client_write.write(str(client_files[-1].Client_movie_rented) + '\n')
    client_write.close()

def save_client1(id,name,rented_movies): #Guarda los clientes
    list = []
    code = ""
    for i in range(1,len(rented_movies)):
        if rented_movies[i] != '[' and rented_movies[i] != ']' and rented_movies[i] == ',':
            code = code + rented_movies[i]
        else:
            list.append(code)
            code = ''

    client_files.append(register_client1(name, id, list))#Llama a la funcion registrar cliente y la guarda en la lista
    print(client_files[0].Client_name)
    print(client_files[0].Client_id)
    print(client_files[0].Client_movie_rented)
def save_movie():#Guarda las peliculas creadas
    #Obtiene los datos de los Entry
    name = entry_nameM.get()
    code = entry_Code.get()
    genre = entry_Genre.get()
    price = entry_Price.get()
    movie_files.append(register_movie(name, code, genre, price))#Llama a la funcion registrar pelicula y la guarda en la lista
    print(movie_files[0].Movie_name)
    movie_write = open('movie.txt', 'a')
    movie_write.write(movie_files[-1].Movie_code + '\n')
    movie_write.write(movie_files[-1].Movie_name + '\n')
    movie_write.write(movie_files[-1].Movie_genre + '\n')
    movie_write.write(movie_files[-1].Movie_price + '\n')
    movie_write.write(str(movie_files[-1].Movie_is_rented) + '\n')
    movie_write.close()

def save_movie1(name,code,genre,price,rented):#Guarda las peliculas creadas
    bol = False
    if rented == "True":
        bol = True
    movie_files.append(register_movie1(name, code, genre, price, bol))#Llama a la funcion registrar pelicula y la guarda en la lista

def rent_movie():
    #Crea variables
    i = 0
    a = 0
    #Obtiene los valores de los entry
    code = entry_Ma.get()
    id = entry_Ca.get()
    client = False
    movie = False
    #Registra si el codigo ingresado esta dentro de la lista de peliculas
    for i in range(0, len(movie_files)):
        if movie_files[i].Movie_code == code:
            if movie_files[i].Movie_is_rented:#Revisa si la pelicula esta alquilada
                print("Ya esta alquilada")
                return 0
            else:
                movie_files[i].is_rented#Cambia el estado de la pelicula a rentada
                client = True
                break
    # Registra si el id ingresado esta dentro de la lista de clientes
    for a in range(0, len(client_files)):
        if client_files[a].Client_id == id:
            client_files[a].rent_movie(code)#Ingresa el codigo de la pelicula a la lista del cliente
            movie = True
            break
    if client == False or movie == False:#Envia aviso si alguno de datos recibidos no esta ingresado
        print("Pelicula o cliente no registrado")
    else:
        print("Su factura es de " + movie_files[i].Movie_price)#Devuelve el precio a pagar por el usuario


def return_movie():
    # Crea variables
    i = 0
    a = 0
    # Obtiene los valores de los entry
    code = entry_Ma.get()
    id = entry_Ca.get()
    client = False
    movie = False
    # Registra si el codigo ingresado esta dentro de la lista de peliculas
    for i in range(0, len(movie_files)):
        if movie_files[i].Movie_code == code:
            movie_files[i].not_rented  # Cambia el estado de la pelicula a no rentada
            client = True
            break
    # Registra si el id ingresado esta dentro de la lista de clientes
    for a in range(0, len(client_files)):
        if client_files[a].Client_id == id:
            client_files[a].return_movie(code)# Quita codigo de la pelicula de las alquiladas
            movie = True
            break
    if client == False or movie == False:  # Envia aviso si alguno de datos recibidos no esta ingresado
        print("Pelicula o cliente no registrado")
    else:
        print("Exito")


def see_movies():#
    #Obtiene los valosres del entry
    id = entry_see.get()
    for a in range(0, len(client_files)):#Revisa que el cliente este registrado
        if client_files[a].Client_id == id:
            for i in range(0, len(client_files[a].Client_movie_rented)):#Recorre la lista de peliculas alquiladas
                print(client_files[a].Client_movie_rented[i])#Imprime las peliculas alquiladas
        else:
            print("Cliente no registrado")
            break


def init():#lee los archivos de texto
    #Crea las variables
    i = 0
    a = 0
    id = ''
    name = ''
    rented_movies = ''
    code = ''
    genre = ''
    price = ''
    rented = ''
    #abre los archivos de texto
    clients_read = open('clients.txt', 'r')
    movies_read = open('movie.txt', 'r')
    readC = clients_read.readlines()
    readM = movies_read.readlines()

    for lineC in readC:# Obtiene los valores de los clientes
        if lineC[-1] == '\n':
            if i == 0:
                id = lineC[:-1]
                i = i + 1
            elif i == 1:
                name = lineC[:-1]
                i = i + 1
            else:
                rented_movies = lineC[:-1]
                i = 0
                save_client1(id,name,rented_movies)
    for lineC in readM:# Obtiene los valores de las peliculas
        if lineC[-1] == '\n':
            if a == 0:
                code = lineC[:-1]
                a = a + 1
            elif a == 1:
                name = lineC[:-1]
                a = a + 1
            elif a == 2:
                genre = lineC[:-1]
                a = a + 1
            elif a == 3:
                price = lineC[:-1]
                a = a + 1
            else:
                rented = lineC[:-1]
                a = 0
                save_movie1(name,code,genre,price,rented)


# Crea la ventana
window = Tk()
window.title("Alquiler de peliculas")
window.resizable(False, False)
window.geometry("650x400")

# Crea un frame para poner los widgets
myFrame = Frame()
myFrame.place(x=0, y=0)
myFrame.config(width=650, height=400)

# Crea widgets
myLabel1 = Label(myFrame, text="Nombre Pelicula")
myLabel1.place(x=2, y=2)
entry_nameM = Entry(myFrame)
entry_nameM.place(x=2, y=20)

myLabel1 = Label(myFrame, text="Codigo Pelicula")
myLabel1.place(x=130, y=2)
entry_Code = Entry(myFrame)
entry_Code.place(x=130, y=20)

myLabel1 = Label(myFrame, text="Genero de la Pelicula")
myLabel1.place(x=2, y=42)
entry_Genre = Entry(myFrame)
entry_Genre.place(x=2, y=60)

myLabel1 = Label(myFrame, text="Precio Pelicula")
myLabel1.place(x=130, y=42)
entry_Price = Entry(myFrame)
entry_Price.place(x=130, y=60)

myButton1 = tkinter.Button(myFrame, text="Guardar", command=save_movie)
myButton1.place(x=50, y=85)

myLabel1 = Label(myFrame, text="Nombre Cliente")
myLabel1.place(x=300, y=2)
entry_nameC = Entry(myFrame)
entry_nameC.place(x=300, y=20)

myLabel1 = Label(myFrame, text="Apellidos Cliente")
myLabel1.place(x=430, y=2)
entry_lastnameC = Entry(myFrame)
entry_lastnameC.place(x=430, y=20)

myLabel1 = Label(myFrame, text="Cedula Cliente")
myLabel1.place(x=300, y=42)
entry_idC = Entry(myFrame)
entry_idC.place(x=300, y=60)

myButton1 = tkinter.Button(myFrame, text="Guardar", command=save_client)
myButton1.place(x=430, y=60)

myLabel1 = Label(myFrame, text="Cliente que desea alquilar/devolver")
myLabel1.place(x=2, y=140)
entry_Ca = Entry(myFrame)
entry_Ca.place(x=2, y=160)

myLabel1 = Label(myFrame, text="Pelicula a alquilar/devolver")
myLabel1.place(x=2, y=200)
entry_Ma = Entry(myFrame)
entry_Ma.place(x=2, y=220)

myButton1 = tkinter.Button(myFrame, text="Alquilar", command=rent_movie)
myButton1.place(x=130, y=160)

myButton1 = tkinter.Button(myFrame, text="Devolver", command=return_movie)
myButton1.place(x=130, y=220)

myLabel1 = Label(myFrame, text="Ense??ar alquiladas")
myLabel1.place(x=200, y=140)
entry_see = Entry(myFrame)
entry_see.place(x=200, y=160)

myButton1 = tkinter.Button(myFrame, text="Ense??ar", command=see_movies)
myButton1.place(x=340, y=150)

init()

window.mainloop()
