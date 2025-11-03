import os
import sys

def resource_path(relative_path):
    # retorna o arquivo absoluto dos arquivos, isso é necessário para que o programa rode num .exe
    try:
        # PyInstaller cria uma pasta temporária
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)