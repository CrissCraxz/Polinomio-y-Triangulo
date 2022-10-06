import math

# DONE: Devuelve el Ecuacion de 2º grado de 'nUno', 'nDos', 'nTres'. Para una ecuación de segundo grado con coeficientes reales o complejos existen siempre dos soluciones, no necesariamente distintas, llamadas raíces, que pueden ser reales o complejas (si los coeficientes son reales y existen dos soluciones no reales, entonces deben ser complejas conjugadas).
def ecuacionSegundoGrado(nUno: float, nDos: float, nTres: float) -> tuple:
    try:
            float(nUno)  
            float(nDos) 
            float(nTres)
            if nUno == 0:
                    print("El coeficiente a no puede ser igual a cero")
                    return "El coeficiente a no puede ser igual a cero"
            else:
                # El discriminante es ∆ = 'math.pow(nDos, 2) - (4 * nUno * nTres)' y sirve para analizar la naturaleza de las raíces que pueden ser reales o complejas
                discriminante = math.pow(nDos, 2) - (4 * nUno * nTres)
                if discriminante == 0:  # ∆ = 0
                    # Resultado unico
                    resultado = -nDos / (2 * nUno)
                    print(f"La raíz única es {resultado}")
                    return (resultado)
                elif discriminante > 0:  # ∆ > 0
                    # Resultado Reales
                    real1 = ((-nDos) + math.sqrt(discriminante)) / (2 * nUno)
                    real2 = ((-nDos) - math.sqrt(discriminante)) / (2 * nUno)
                    print(f"La raíz real (+) es = {real1}")
                    print(f"La raíz real (-) es = {real2}")
                    return (real1, real2)
                else:  # ∆ < 0
                    # Resultado complejas conjugadas
                    # 
                    print("raices imaginarias")
                    return   "raices imaginarias" 
        
    except ValueError:
        print("valor ingresado no numerico")
        return "valor ingresado no numerico"



# Inicio
#ecuacionSegundoGrado(1000, 6.22222, 4)