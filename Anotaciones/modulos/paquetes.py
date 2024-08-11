# Los paquetes no son mas que una carpeta con modulos 
# para considerar una carpeta como paquete debe contener un archivo "__init__.py"
import sys
sys.path.append("C:\\Users\\admin\\Desktop\\Cursos\\Python Dalto")

import modulos_propios as own
print(own.__path__)