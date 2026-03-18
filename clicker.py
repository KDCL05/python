import tkinter as tk 
import time
import random

evento_activo = False
evitar_penalizacion = False
tiempo_evento = 0
monedas = 0
click_valor = 1
precio_boton2=10
precio_boton3=100
monedas_pasivas = 0
ultimo_tiempo = time.time()

def mejora_boton_coin():
    global monedas, click_valor,precio_boton2
    if(monedas>=precio_boton2):
        click_valor=click_valor+1
        monedas=monedas-precio_boton2
        precio_boton2=precio_boton2*2
        boton_2.config(text=str(f"mejora\n{precio_boton2}"))   
        contenido.config(text=str(int(((monedas)))))

def boton_coin():
    global monedas,click_valor
    monedas = monedas+click_valor
    contenido.config(text=str(int(((monedas)))))

def mejora_pasiva():
    global monedas_pasivas,precio_boton3,ultimo_tiempo,monedas
    if(monedas>=precio_boton3):
        monedas_pasivas=monedas_pasivas+1
        monedas=monedas-precio_boton3
        precio_boton3=precio_boton3*2
        boton_3.config(text=str(f"mejora\n{precio_boton3}"))   
        contenido.config(text=str(int(((monedas)))))
    
def generar_pasivo():
    global monedas, monedas_pasivas, ultimo_tiempo

    tiempo_actual = time.time()
    delta = tiempo_actual - ultimo_tiempo

    monedas += monedas_pasivas * delta
    ultimo_tiempo = tiempo_actual

    contenido.config(text=str(int(((monedas)))))

    ventana.after(100, generar_pasivo)

def programar_evento():
    global tiempo_evento

    tiempo_evento = random.randint(20, 60) 
    ventana.after((tiempo_evento - 15) * 1000, mostrar_boton)

def mostrar_boton():
    global evento_activo

    evento_activo = True
    boton_4.place(relx=.8, rely=.5, anchor="center", height=80, width=120)

    print("¡Evento en 15 segundos!")

    ventana.after(15000, resolver_evento)

def resolver_evento():
    global monedas, evitar_penalizacion, evento_activo

    if not evitar_penalizacion:
        monedas /= 2
        print("El sat te audito")
    else:
        print("Le pagaste al sat")

    evitar_penalizacion = False
    evento_activo = False

    contenido.config(text=str(int(monedas)))

    boton_4.place_forget() 

    programar_evento()


def evitar():
    global evitar_penalizacion, evento_activo

    if evento_activo:
        evitar_penalizacion = True
        print("Intentando evitar...")




    
    

ventana = tk.Tk()
ventana.title("clicker")
ventana.geometry("600x600")


    

boton_1 = tk.Button(ventana , text="monedas" , command=boton_coin)
boton_1.place(relx=.5,rely=.1,anchor="center",height=80, width=80)
boton_2 = tk.Button(ventana , text=f"mejora\n10" , command=mejora_boton_coin)
boton_2.place(relx=.2,rely=.5,anchor="center",height=80, width=80)
boton_3 = tk.Button(ventana , text=f"mejora pasiva\n100" , command=mejora_pasiva)
boton_3.place(relx=.2,rely=.6,anchor="center",height=80, width=80)
boton_4 = tk.Button(ventana, text="Pagar al sat", command=evitar)
contenido=tk.Label(ventana, text=("0"), font=("Arial, 15"))
contenido.place(relx=.5,rely=.8)

generar_pasivo()
programar_evento()

