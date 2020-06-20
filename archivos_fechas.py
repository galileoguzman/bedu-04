'''
Listar los archivos del directorio actual y mostrar su última fecha de modificación.

Usaremos las bibliotecas `os` & `datetime`
'''

import os
from datetime import datetime

files = os.listdir()
for f in files:
    last_updated_at = os.path.getmtime(f) # Here is a timestamp
    last_updated_at = datetime.fromtimestamp(last_updated_at) # Switch to date format
    print(f'{f} last modified : {last_updated_at}')

# comentario
