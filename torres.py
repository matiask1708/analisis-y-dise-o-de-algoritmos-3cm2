def torres_de_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover disco 1 desde poste {origen} a poste {destino}")
        return

    torres_de_hanoi(n-1, origen, destino, auxiliar)
    print(f"Mover disco {n} desde poste {origen} a poste {auxiliar}")
    torres_de_hanoi(n-1,auxiliar,origen,destino)

n=int(input("Ingrese el numero de discos para la torre"))
torres_de_hanoi(n, 'A', 'B', 'C')