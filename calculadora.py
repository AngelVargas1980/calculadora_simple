from tkinter import ttk
from tkinter import *

class Desk:
    def __init__(self, window):
        # Initializations
        
        #ancho
        ancho = 800
        
        #alto
        alto = 600
        
        # asignamos la ventana a una variable de la clase llamada wind
        self.wind = window

        #le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #centramos el contenido 
        self.wind.columnconfigure(0, weight=1)
        
        #le damos un titulo a la ventana
        self.wind.title('Aplicaci�n con interface gr�fica en Python - By Angel Vargas')
        

        # creamos un contenedor   LA SUMA
        frame = LabelFrame(self.wind, text = 'Sumar 2 valores')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)      
        
        # creamos un etiqueta
        Label(frame, text = 'primer numero: ').grid(row = 1, column = 0)
       
        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)

        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'segundo numero: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)
        
        #Creamos un boton para ejecutar la suma
        Button(frame, text = 'Sumar', command = self.sumar).grid(row = 3, columnspan = 2, sticky = W + E)

        #designamos un �rea para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    # creamos una funci�n para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0

    # esta es la funci�n que ejecuta la suma
    def sumar(self):
        if self.validation():
            resultado = float( self.var1.get() ) + float( self.var2.get() )
            self.message['text'] = 'La suma de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'






        # creamos un 2do. contenedor   LA RESTA
        frame = LabelFrame(self.wind, text = 'Restar 2 valores')
        frame.grid(row = 0, column = 10, columnspan = 3, pady = 20)

        # creamos una 2do. etiqueta
        Label(frame, text = 'primer numero: ').grid(row = 1, column = 0)

        #creamos un 2do. input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 5)

        # igual que arriba una 2da. etiqueta y un campo input para ingresar valores
        Label(frame, text = 'segundo numero: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 11)

        #Creamos un 2do. boton para ejecutar la resta
        Button(frame, text = 'Restar', command = self.restar).grid(row = 3, columnspan = 2, sticky = W + E)

        #designamos una segunda �rea para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 12, columnspan = 2, sticky = W + E)
        
    # creamos una funci�n para validar que los campos no esten en blanco
    #def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0
    
    

    # esta es la funci�n que ejecuta la resta
    def restar(self):
        if self.validation():
            resultado = float( self.var1.get() ) - float( self.var2.get() )
            self.message['text'] = 'La resta de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'



# creamos un 3er. contenedor LA MULTIPLICACI�N
        frame = LabelFrame(self.wind, text = 'Multiplicar 2 valores')
        frame.grid(row =11, column = 0, columnspan = 3, pady = 20)

        # creamos un 3er. etiqueta
        Label(frame, text = 'primer numero: ').grid(row = 1, column = 0)

        #creamos un 3er. input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 11, column = 1)

        # igual que arriba una 2da. etiqueta y un campo input para ingresar valores
        Label(frame, text = 'segundo numero: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 12, column = 1)

        #Creamos un 2do. boton para ejecutar la multiplicaci�n
        Button(frame, text = 'Multiplicar', command = self.multiplicar).grid(row = 13, columnspan = 2, sticky = W + E)

        #designamos una segunda �rea para mensajes
        self.message = Label(text = '', fg = 'black')
        self.message.grid(row = 13, column = 2, columnspan = 2, sticky = W + E)
        
    # creamos una funci�n para validar que los campos no esten en blanco
    #def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0
 

    # esta es la funci�n que ejecuta la multiplicaci�n
    def multiplicar(self):
        if self.validation():
            resultado = float( self.var1.get() ) * float( self.var2.get() )
            self.message['text'] = 'La multiplicaci�n de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'




# creamos un 4to. contenedor LA DIVISI�N
        frame = LabelFrame(self.wind, text = 'Dividir 2 valores')
        frame.grid(row = 10, column = 10, columnspan = 3, pady = 20)

        # creamos un 4ta. etiqueta
        Label(frame, text = 'primer numero: ').grid(row = 1, column = 0)

        #creamos un 4to. input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 11, column = 11)

        # igual que arriba una 2da. etiqueta y un campo input para ingresar valores
        Label(frame, text = 'segundo numero: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 12, column = 11)

        #Creamos un 4to. boton para ejecutar la divisi�n
        Button(frame, text = 'Dividir', command = self.dividir).grid(row = 3, columnspan = 2, sticky = W + E)

        #designamos una segunda �rea para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 13, column = 12, columnspan = 2, sticky = W + E)
        
    # creamos una funci�n para validar que los campos no esten en blanco
    #def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0
 

    # esta es la funci�n que ejecuta la divisi�n
    def dividir(self):
        if self.validation():
            resultado = float( self.var1.get() ) / float( self.var2.get() )
            self.message['text'] = 'La divisi�n de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'









#validamos si estamos en la aplicaci�n inicial
if __name__ == '__main__':
    
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Desk(window)

    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()

