# Manejo financiero Felipe y Francisco

El siguiente código escrito en Python tiene como propósito ayudar en las tareas de reparto de gastos a lo largo del mes, para así estar con las cuentas al día.

# Instalación
Se recomienda clonar el repositorio de Github para así acceder a todo el historial del proyecto, Para esto usar git en el directorio que usted desee hacerlo.
```sh
git clone https://github.com/panchouc/DptoMDI.git
```

# Uso
El flujo principal del programa se encuentra en los archivos main.py y app.py . En el archivo main.py usted puede
- Crear archivos de un determinado mes que contiene worksheets con todos los días de ese mes
- Hacer una estadística de los datos de ese archivo
- Visualizar los gastos personales
- Hacer un nuevo excel con toda la información de los días del mes que usted desee

En el archivo app.py debe usted cambiar el nombre del archivo que desea leer, tanto en la variable archivo_display, como en la variable, archivo_calculos. La variable archivo_display se usa para posteriormente hacer un renderizado en la web de la hoja excel. La variable archivo_calculos se utiliza para printear en la consola la estadística de ese archivo de excel. Mencionar que ambos archivos excel a leer deben estar en el directorio de los archivos main.py y app.py. Para poder usar streamlit, que es una librería que se utiliza, debe escribir usted en la consola, en el directorio en el que usted se encuentra:

```sh
streamlit run app.py
```

# Licencia
El proyecto es de libre uso.