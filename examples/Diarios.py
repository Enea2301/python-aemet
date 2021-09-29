from aemet import Aemet
import pandas as pd

# Cargamos el archivo de la apikey
aemet = Aemet(api_key_file='INSERTA AQUÍ LA DIRECCIÓN DE TU ARCHIVO aemet.key')

# Obtenemos los datos diarios en el período fijado para la estación dada
datos = aemet.get_valores_climatologicos_diarios("2021-01-01T00:00:00UTC", "2021-09-24T23:59:59UTC", "0200E")


# Con esta línea pasamos la lista obtenida a un dataframe en pandas, y de ahí a un csv para que quede todo ordenado y en un archivo fácilmente manipulable
df = pd.DataFrame(datos)
df.to_csv('/direccion/guardado/Nombre.csv', index=False)
