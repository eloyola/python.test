"""
#capturar excepciones y manejar errores en codigo
try:    
    nombre = input('cual es tu nombre?')
    if len(nombre)>1:
        nombre_usuario = f'el nombre es {nombre}'
    print(nombre_usuario)
except:
    print('ha ocurrido un error')
else:
    print('todo ha ido bien')
finally:
    print('fin de iteracion')
"""

"""
# multiples excepciones
try:
    numero = int(input('numero para elevarlo al cuadrado:'))
    print(f'el cuadrado es: {str(numero*numero)}')
except TypeError:
    print('convertir cadenas a enteros en codigo')
except ValueError:
    print('introduce numero correcto')
except Exception as e:
    print('ha ocurrido un error', type(e).__name__)
"""

# excepciones personalizadas o lanzar exception
try:
    nombre =input('introduce el nombre:')
    edad=int(input('introduce edad:'))

    if edad<5 or edad>110:
        raise ValueError('edad introducida no es real')
    elif len(nombre)<=1:
        raise ValueError('nombre no esta completo')
    else:
        print(f'bienvenido {nombre}')
except ValueError:
    print('introduce datos correctos')
except Exception as e:
    print('existe un error', e)