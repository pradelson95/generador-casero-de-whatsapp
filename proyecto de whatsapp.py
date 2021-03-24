import time 
import random as codigo_de_whatsapp

while True:
    try:
        
        print("=====menu de opciones=====")
        print("1.codigo de recuperación de whatsapp")
        print("2.recuperar informaciones personales")
        print("3.salir")
        
        opción = int(input("elige una opción de menu: ")) 
        número = codigo_de_whatsapp.randint(11758,15694)
        
        if opción==1:
            print("generando un nuevo codigo.....")
            time.sleep(2)
            print("su codigo de whatsapp es:",número)
            time.sleep(2)
            codigo = input("ingrese su codigo para la recuperación: ")
        
        elif codigo==número:
            print("su cuenta de whatsapp ha sido recuperada")
             
            
        elif opción==2:
            print("recuperando 24 videos")
            time.sleep(2)
            print("recuperando 57 fotos")
            time.sleep(2)
            print("recuperando 112 músicas")
            time.sleep(2)
            print("la recuperación de datos está completada")
            time.sleep(3)
            
        
        elif opción==3:
            print("gracias por visitarnos!")
            break 
    
    except ValueError:
        print("valor incorrecto, ingrese lo que se le pide")
    
    except Exception as error:
        print("algo salio mal, intente otra vez!")