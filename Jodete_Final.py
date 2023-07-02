'''
Objetivo del programa (descripción del problema que resuelve): El Objetivo es quedarse sin cartas en la mano

Autor/es: Aparicio Tapia Dana Belen
          Ignacio Otranto
          Yessica Morinigo

Versión: 1

Fecha: 21/11/2022

Análisis de Casos (número de caso, estado inicial, transformación, estado final -se consideran casos base para la prueba del programa):

Ejemplo del comienzo de una partida: 

Inicio de Ronda
Los puntos del jugador son 0 y los de la computadora 0

			Turno de la computadora
La carta en meza es: ('E', 10)
La computadora tiene 6 cartas en mano

			Turno de la computadora
La carta en meza es: ('E', 11)
La computadora tiene 7 cartas en mano

			Turno del jugador
La carta en meza es: ('E', 11)
Su Mazo es
[('?', 0), ('C', 7), ('O', 4), ('C', 11), ('C', 3), ('E', 5), ('C', 6)]
Ingrese el lugar de la carta que desea tirar, 0 para perder turno y agarrar o -1 para avisar que le queda una carta: 6

			Turno de la computadora
La carta en meza es: ('E', 5)
La computadora tiene 6 cartas en mano

			Turno del jugador
La carta en meza es: ('O', 5)
Su Mazo es
[('?', 0), ('C', 7), ('O', 4), ('C', 11), ('C', 3), ('C', 6)]
Ingrese el lugar de la carta que desea tirar, 0 para perder turno y agarrar o -1 para avisar que le queda una carta: 3

Asi sucesivamente hasta que alguno llegue a 100 puntos.


Síntesis de Casos (composición de casos para la generalización):--------------------


Recursos (variables y funciones del programa -nombre y propósito)

    Datos a solicitar al usuario (sea en el prólogo o sea durante la resolución):
    Debe ingresar carta a tirar
    
    Auxiliares (necesarios para transformaciones intermedias):--------------------
    
    Resultados (a informar sea durante el desarrollo o en el epílogo):--------------------

    Funciones propias (necesarias para la descomposición del problema en subproblemas):
    

'''

from random import randint, shuffle

numero = range(1,13)
palo = ["O","E","B","C"]
JMazo=[] #Mazo del Jugador
CMazo=[] #Mazo de la computadora
Pjugador=0 #Puntos del jugador
Pcomputadora=0 #Puntos de la computadora
# DEFINICIÓN DE FUNCIONES (si se requieren para descomponer la solución del problema)
#def nom_función():

def CrearMazo(): #Crea el Mazo
  Mazo = []
  for p in palo:
    for v in numero:
      Mazo.append((p,v))
  Mazo.append(('?',0))
  Mazo.append(('?',0))
  return Mazo
  
Mazo = CrearMazo()

def RepartirMazo (): #Reparte el Mazo
    shuffle(Mazo)
    for n in range(7):
        JMazo.append(Mazo.pop(0))
        CMazo.append(Mazo.pop(0))

def Reset(): # Reset de Mazo general y jugadores
    global Mazo
    global JMazo
    global CMazo
    Mazo=CrearMazo()
    JMazo=[] #Mazo del Jugador
    CMazo=[] #Mazo de la computadora

def ContarMazo(quien): #Conteo de Puntos
    global Pcomputadora
    global Pjugador
    if quien=='jugador':
        for n in JMazo:
            if n[1]<=2:
                Pjugador+=20
            elif n[1]>=10:
                Pjugador+=10
            elif n[0]=='?':
                Pcomputadora=100
            else:
                Pjugador+=n[1]
    if quien=='computadora':
        for n in CMazo:
            if n[1]==1 or n[1]==2:
                Pcomputadora+=20
            if n[1]>=10:
                Pcomputadora+=10
            if n[0]=='?':
                Pcomputadora=100
            else:
                Pcomputadora+=n[1]

'''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    def CrearMazo(): nada
    def ContarMazo(quien): a que jugador cuanta las cartas. 
    
    Objetivo (descripción de lo que hace o devuelve):
    def CrearMazo(): crear un mazo
    def RepartirMazo (): mezcla el mazo y reparte las cartas para cada jugador. 
    def Reset(): vuelve a crear el mazo y reinicia las cartas para cada jugador.
    def ContarMazo(quien): cuenta los puntos del final de la ronda. 
    
    Análisis de Casos (número de caso, estado inicial, transformación, estado final -se consideran casos base para la prueba
    de la función): Ninguno 

    Síntesis de Casos (composición de casos para la generalización): Ninguno 

    Recursos (variables o funciones internas -nombre y propósito)

    Auxiliares (necesarios para transformaciones intermedias): Ninguno
    
    Resultados (si la función devuelve):
    def CrearMazo(): devuelve el mazo creado

    Funciones internas (necesarias para la descomposición del problema en subproblemas): Ninguna

'''
    #1 PRÓLOGO
    # Establecimiento de valores iniciales para datos auxiliares o que se transformarán en resultados (opcional)
CartaMeza=[] # Creación de la variable que contendra la ultima carta jugada.
RecienCantado=0 # Variable, para saber que se canto uno en el turno reciente
    #2 RESOLUCIÓN
    # Descomposición del problema en subproblemas 2.x que a su vez pueden requerir inicialización de datos o mostrar resultados

    #3 EPÍLOGO
    # Devolución de valor o valores o muestra de resultados

# PROGRAMA    
#1 PRÓLOGO
#1.1 Presentación
print('Bienvenido a Jodete un juego de cartas similar al uno\n El Objetivo es quedarse sin cartas en la mano.\nInicio y desarrollo del juego: \nSe reparten siete cartas a cada jugador y se deja una boca arriba en la mesa, junto al mazo. Cada jugador debe tirar (si tiene) una carta con igual índice (cambio de palo) o una del mismo palo que la que está en la mesa. Si no tiene debe tomar una del mazo y ver si le sirve. Si no le sirve dice "paso" y continúa el jugador de su derecha (o el otro, si se juega de a dos).\nCuando al jugador le queda una carta está obligado a decir "me queda una", porque si no lo hace, los demás le hacen levantar siete cartas.\n\nCartas especiales\nHay algunas cartas que hacen que el juego se complique y se haga más divertido:\n• Si alguien tira un 10, el jugador siguiente debe levantar una carta del mazo y no puede descartarse.\n• Si alguien tira un 11, cambia la dirección del juego. Por ejemplo: Jugadores A, B, C y D. Primero juega el A, luego el B y el C tira un 11. Entonces, al que le toca jugar nuevamente es al B. Si éste tira otro 11, el siguiente en jugar es el C, ya que vuelve a cambiar la dirección del juego. Si se juega de a dos, el que tira el 11 juega dos veces seguidas.\n• Si alguien tira un 12, se saltea al siguiente jugador. Por ejemplo: Juega el jugador A, luego el B tira un 12. Entonces el siguiente a jugar es el D. Si se juega de a dos, el que tira el 12 juega dos veces seguidas.\n• Si alguien tira un 2, el jugador siguiente levanta 2 cartas. Si se tira otro 2, el siguiente levanta 4 cartas. Y si se tira nuevamente otro 2, el siguiente levanta 6 cartas. Por último si se tira otro 2, elsiguiente levanta 8 cartas. No hay descartes cuando levantan las cartas.\n• Cuando se descarta un comodín, todos los demás jugadores deben levantar una carta y el que tiró elcomodín se vuelve a descartar. El comodín es muy peligroso: no tiene que quedar en la mano deljugador cuando otro corta, puesto que se pierde el partido.\n\nPuntaje\nEl partido se juega hasta 100 puntos.\nEl que corta obtiene -10 (menos diez). Los demás deben sumar los puntos de sus cartas de acuerdo con el siguiente puntaje:\n• el 1 y el 2 valen 20 puntos;\n• las figuras valen 10 puntos;\n• las demás cartas lo que tienen en sus índices.')

#1.1.1 Impresión del título del programa en pantalla

#1.1.2 Descripción o aclaraciones al usuario (opcional)
print('\n\nPara tirar una carta usted debe escribir la posicion en la que se encuentra, comenzando desde el uno hasta la ultima carta\nEn caso de no tener carta para poder tirar, escribiendo 0 salteara su turno y recibira una carta\nCuando le quede una carta debe escribir -1 para avisar de esta forma que le queda una carta al computador')

#1.2 Datos iniciales 
#1.2.1 Solicitud e ingreso de datos desde teclado (opcional, si los datos se piden durante la resolución)

#1.2.2 Establecimiento de valores iniciales para datos auxiliares o que se transformarán en resultados (opcional)

#2 RESOLUCIÓN
# Descomposición del problema en subproblemas 2.x que a su vez pueden requerir ingreso o inicialización de datos o mostrar resultados
while Pjugador<=99 or Pcomputadora<=99: #Finalizacion del programa, cuando algun jugador obtiene 100 puntos.
    print('\n\nInicio de Ronda')
    print(f'Los puntos del jugador son {Pjugador} y los de la computadora {Pcomputadora}\n\n')
    Reset() # Reinicio de la partida. 
    mano=randint(0, 1) # devuelve 0 o 1 en forma aleatoria (0 es mano el Jugador, 1 es mano el computadora)
    RepartirMazo() # Reparte el mazo 
    CartaMeza=Mazo.pop(0) # Coloca la primera carta del mazo en la mesa.
    while len(JMazo)!=0 or len(CMazo)!=0: # while esta activo durante la ronda.
        while mano==0 and len(JMazo)!=0: #Turno de jugador
            if len(JMazo)!=1 and RecienCantado==0: # verificador de que el jugador tiene una carta 
              Uno=0
            RecienCantado=0 #Pasado el turno en el que se canto
            if len(Mazo)==0: # si el mazo esta vacio lo reinicia, removiendo las cartas que tienen en mano el  jugador y la computadora. 
              Mazo = CrearMazo()
              shuffle(Mazo)
              for n in JMazo:
                Mazo.remove(n)
              for n in CMazo:
                Mazo.remove(n)
              print('Reinicio de Mazo')
            print('\n\t\t\tTurno del jugador')
            print(f'La carta en meza es: {CartaMeza}')
            print('Su Mazo es')
            print(JMazo)
            n=0
            while n!=1: #Ingreso y verificador de numero correcto ingresado por el jugador, si ingresa una carta que no tiene no hace nada. 
                Carta=int(input('Ingrese el lugar de la carta que desea tirar, 0 para perder turno y agarrar o -1 para avisar que le queda una carta: '))-1
                if Carta <= len(JMazo):
                    if JMazo[Carta][1]==CartaMeza[1] or JMazo[Carta][0]==CartaMeza[0] or JMazo[Carta][0]=='?' or CartaMeza[0]=='?':
                        n=1
                    elif Carta==-1 or Carta==-2:
                        n=1
            if Carta >=0: #Si lo que tira es una carta, realiza la accion especial, si lo tiene. 
                if JMazo[Carta][1]==10: #accion especial del 10.
                    CMazo.append(Mazo.pop(0))
                    mano=0 #Pierde el turno
                elif JMazo[Carta][1]==11: #accion especial del 11.
                    mano=0 #Pierde el turno 
                elif JMazo[Carta][1]==12: #accion especial del 12.
                    mano=0 #Pierde el turno
                elif JMazo[Carta][1]==2: #accion especial del 2, suma +2.
                    for m in range(2):
                      CMazo.append(Mazo.pop(0))
                    mano=0 #Pierde el turno
                elif JMazo[Carta][0]=='?': #accion especial del comodín. 
                    CMazo.append(Mazo.pop(0))
                    mano=0 #Pierde el turno
                else:mano=1 #cambio de mano
                CartaMeza=JMazo.pop(Carta) #reemplazo de la carta en la mesa, por la carta tirada. 
            elif Carta==-2:  # accion especial cuando queda una carta en la mano. 
                print ('¡¡Me queda una!!')
                if len(JMazo)==2:
                  Uno=1
                  RecienCantado=1
                else:
                  print ('Mal cantado, Suma 2 y pierde turno')
                  JMazo.append(Mazo.pop(0))
                  JMazo.append(Mazo.pop(0))
                  mano=1
            else:    # accion especial de saltar el turno. 
                JMazo.append(Mazo.pop(0))
                mano=1
            if Uno==1:
              print('Haz dicho uno en esta ronda')
        if len(JMazo)==0 or len(CMazo)==0: #termino de ronda, cuando una de las dos manos esta vacia. 
          break
        while mano==1 and len(CMazo)!=0: #Turno computadora
            if len(Mazo)==0: # Reinicio del mazo en el caso de estar vacio. 
              Mazo = CrearMazo()
              shuffle(Mazo)
              for n in JMazo:
                Mazo.remove(n)
              for n in CMazo:
                Mazo.remove(n)
              print('Reinicio de Mazo')
            print('\n\t\t\tTurno de la computadora')
            print(f'La carta en meza es: {CartaMeza}')
            if len(JMazo)==1 and Uno==0: #aviso de que el jugador no canto uno. 
              print ('No dijiste Uno, suma 7')
              for m in range(7):
                JMazo.append(Mazo.pop(0))
            n=0
            for carta in CMazo: #eleccion de carta por parte de la computadora, en caso de no tener nada agarra una carta y pierde el turno. 
                if carta[1]==CartaMeza[1] or carta[0]==CartaMeza[0] or carta[0]=='?' or CartaMeza[0]=='?':
                    Carta=carta
                    break
                else:
                    n+=1
                if n==len(CMazo):
                    Carta=-1
            if Carta!=-1:
                if Carta[1]==10:
                    JMazo.append(Mazo.pop(0))
                    mano=1 #Pierde el turno
                    print ('\tEl jugador agarra una carta')
                elif Carta[1]==11:
                    mano=1 #Pierde el turno 
                elif Carta[1]==12:
                    mano=1 #Pierde el turno
                elif Carta[1]==2:
                    for m in range(2):
                      JMazo.append(Mazo.pop(0))
                    mano=1 #Pierde el turno
                elif Carta[0]=='?':
                    JMazo.append(Mazo.pop(0))
                    mano=1 #Pierde el turno
                    print ('\tEl jugador agarra una carta')
                else: mano=0
                if len(CMazo)!=0: 
                  CartaMeza=Carta
                  CMazo.remove(Carta)
                if len(CMazo)==1: #la computadora grita uno cuando le queda una carta. 
                  print('\t\t\tLa computadora grita: <¡¡Me queda una carta!!>')
            else:
                CMazo.append(Mazo.pop(0))
                mano=0
            print(f'La computadora tiene {len(CMazo)} cartas en mano') #aviso al jugador de cuantas cartas tiene la computadora
        if len(JMazo)==0 or len(CMazo)==0: #termino de ronda, cuando una de las dos manos esta vacia. 
          break
    if len(CMazo)==0: # en caso de mano computadora vacio, contar cartas  de jugador y restarle 10 puntos a la computadora. 
        ContarMazo('jugador')
        Pcomputadora-=10
    if len(JMazo)==0: # en caso de mano jugador vacio, contar cartas de computador y restarle 10 puntos a la jugador. 
        ContarMazo('computadora')
        Pjugador=-10
    if Pjugador>=100: # aviso de que el computador gano
      print('El Computador a vencido')
      break
    if Pcomputadora>=100: # aviso de que el jugador gano
      print('El Jugador a vencido')
      break

#3 EPÍLOGO
#3.1 Muestra de la solución del problema por pantalla (opcional, si sólo se muestran resultados durante la resolución)

#3.2 Pausa para ver resultados en pantalla que se puede obviar, si los resultados se van mostrando durante la resolución
print() # salto de línea
input('Pulse tecla Enter para terminar el programa...') # pausa forzada
