import random
compu_opciones  = ("piedra", "papel", "tijera")
user_opciones = ("piedra", "papel", "tijera")
usuario_opciones = " "
ronda = 1



while ronda < 4:
        usuario_opciones = input ("elija piedra, papel ó tijera ")
        usuario_opciones = usuario_opciones.lower()
        computador_opciones = random.choice(compu_opciones)
        if ronda == 3: 
                print("aqui termina el juego")
        if usuario_opciones not in user_opciones :
                print("la opcion elejda es incorrecta")      
        if usuario_opciones == computador_opciones:
                print(f" ya estas en la ronda {ronda}")
                print( f"usted eligio {usuario_opciones} y la maquina {computador_opciones} hay empate")
                ronda +=1
                continue
                #(continue) se salta las demas instrucciones dentro del ciclo
        elif usuario_opciones == "piedra" :
                if computador_opciones == "tijera":
                        print(f" ya estas en la ronda {ronda}")
                        print(f"usted eligio {usuario_opciones} y la maquina {computador_opciones}  usted gano")
                        ronda +=1
                        continue
                else:
                        print(f" ya estas en la ronda {ronda}")
                        print(f"usted eligio {usuario_opciones} y la maquina {computador_opciones}  usted perdio")
                        ronda +=1
                        continue
        
                
        elif usuario_opciones == "papel":
                if computador_opciones == "piedra":
                        print(f" ya estas en la ronda {ronda}")
                        print(f"usted eligio {usuario_opciones} y la maquina {computador_opciones} usted gano")
                        ronda +=1
                        continue
                else:
                        print(f" ya estas en la ronda {ronda}")
                        print(f"usted eligio {usuario_opciones} y la maquina {computador_opciones} usted perdio")
                        ronda +=1
                        continue

        elif usuario_opciones == "tijera":
                if computador_opciones == "papel":
                        print(f" ya estas en la ronda {ronda}")
                        print(f"usted eligio {usuario_opciones} y la maquina {computador_opciones} usted gano")
                        ronda +=1
                        continue
                else:
                        print(f" ya estas en la ronda {ronda}")
                        print(f"usted eligio {usuario_opciones} y la maquina {computador_opciones} usted perdio")
                        ronda +=1
                        
        
                        
                        


        





        