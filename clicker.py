import tkinter as tk 

monedas = 0
click_valor = 1
precio=10
def valor():
    global monedas, click_valor,precio
    if(monedas>=precio):
        click_valor=click_valor+1
        monedas=monedas-precio
        precio=precio*2
        boton_2.config(text=str(f"mejora\n{precio}"))   
        contenido.config(text=str(monedas))

def accion():
    global monedas,click_valor
    monedas = monedas+click_valor
    contenido.config(text=str(monedas))
    

ventana = tk.Tk()
ventana.title("clicker")
ventana.geometry("600x600")

boton_1 = tk.Button(ventana , text="monedas" , command=accion)
boton_1.place(relx=.5,rely=.1,anchor="center",height=80, width=80)
boton_2 = tk.Button(ventana , text=f"mejora\n{precio}" , command=valor)
boton_2.place(relx=.2,rely=.5,anchor="center",height=80, width=80)
contenido=tk.Label(ventana, text=("0"), font=("Arial, 15"))
contenido.place(relx=.5,rely=.8)

ventana.mainloop()
