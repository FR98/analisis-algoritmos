"""
---------------------------------------------------------------------------------------------------
	Análisis y Diseño de Algoritmos
	MTF
	Author:
	    Francisco Rosal 18676
---------------------------------------------------------------------------------------------------
"""

def MTF(configuration, requests):
    print("Configuracion\tSolicitud\tCosto\tNueva Configuracion")
    total_cost = 0
    for s in requests:
        prev_config = str(configuration)
        cost = configuration.index(s) + 1
        total_cost += cost
        configuration.insert(0, configuration.pop(configuration.index(s)))
        print(prev_config, "\t", s, "\t", cost, "\t", configuration)
    print("Costo total: ", total_cost)

def IMTF(configuration, requests):
    print("Configuracion\tSolicitud\tCosto\tNueva Configuracion")
    total_cost = 0
    for i in range(len(requests)):
        prev_config = str(configuration)
        value = requests[i]
        cost = configuration.index(requests[i]) + 1
        limit = cost + i
        total_cost += cost

        if limit > len(requests):
            limit = len(requests)

        for j in range(i + 1, limit):
            if value == requests[j]:
                configuration.insert(0, configuration.pop(configuration.index(requests[i])))
        print(prev_config, "\t", value, "\t", cost, "\t", configuration)
    print("Costo total: ", total_cost)

# a)
MTF([0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4])

# b)
MTF([0, 1, 2, 3, 4], [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4])

# c)
# ¿Para  qué  secuencia  de 20 solicitudes se  obtiene  el  mínimo  costo total  de  acceso  utilizando  el algoritmo MTF para la configuración 0, 1, 2, 3, 4?
# ¿Cuál sería ese costo total de acceso?
# Se obtiene el minimo costo total cuando siempre se pide que se pase al frente el elemento que ya esta al frente.
MTF([0, 1, 2, 3, 4], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# d)
# ¿Para qué secuencia de 20 solicitudes se obtiene el peor de los casos utilizando el algoritmo MTF para la configuración 0, 1, 2, 3, 4?
# ¿Cuál sería ese costo total de acceso?
# Se obtiene el peor caso cuando siempre se pide que se pase al frente el elemento que se encuentra al final.
MTF([0, 1, 2, 3, 4], [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0])

# e)
MTF([0, 1, 2, 3, 4], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
MTF([0, 1, 2, 3, 4], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
# ¿Cuál sería  la  fórmula  para  calcular  el  costo  de n solicitudes del mismo elemento si éste  se encuentra inicialmenteen la k-ésima posición de la lista de configuración?
# n + k

# f)
IMTF([0, 1, 2, 3, 4], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
IMTF([0, 1, 2, 3, 4], [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0])

# g)
# ¿Cuál es la diferencia entre un algoritmo online y uno offline?
# ¿Cambiarían en algo su desempeño o su comportamiento MTF e IMTF si se usaran como algoritmos online
# (considere  el  efecto  de diferentes secuencias de solicitudes)?
"""
La principal diferencia entre un algoritmo online y uno offline es que el offline necesita tener todo el input desde el inicio para su ejecuccion,
a diferencia de un algoritmo online que  se puede in proporcionando el input durante la ejecuccion.
En cuanto a MTF no cambiaria.
En cuando a IMTF si cambiaría, ya que no podría saber si el elemento que se quiere mover aparece en las posiciones siguientes por no tener toda la informacion al inicio.
"""