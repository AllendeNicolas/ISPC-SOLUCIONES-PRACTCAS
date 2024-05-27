# EPS: Queremos saber, si el jugador esta asistiendo al entrenamiento, cumple con la asitencia, pero si sufrio una lesion, no se encuentra apto para jugar.
#  ENTRADA: variables: asistencia_practica y sufrio_lesion.
#  SALIDA: se pretende conocer el estado actual del jugador.
#  PROCESO:

asistencia_practica = False #bool (input ("INDICAR SI EL JUGADOR CUMPLE CON LA ASISTENCIA, MEDIANTE TRUE O FALSE: "))
sufrio_lesion = True #bool (input ("INDICAR SI EL JUGADOR PADECIÓ  ALGUNA LESIÓN, MEDIANTE TRUE O FALSE: "))

# Verificamos si el jugador asistió al entrenamiento y si no sufrió una lesión

if asistencia_practica and not sufrio_lesion:
    print("El jugador cumple con la asistencia y está apto para jugar.")
else:
    print("El jugador no cumple con la asistencia o no está apto para jugar debido a una lesión.")