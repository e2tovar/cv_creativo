import os
import subprocess

from app.initialize_embeddings import init_embeddings

# Ruta al directorio raíz del proyecto
project_root = os.path.dirname(os.path.abspath(__file__))

# Verificar si los embeddings ya están generados
if not os.path.exists("app/assets/embeddings.pkl"):
    print("Generando embeddings...")
    init_embeddings()

# Lanzar la aplicación de Streamlit
print("Iniciando la aplicación...")
# Ejecutar app.py usando streamlit run con la ruta absoluta
subprocess.run(["streamlit", "run", 'app.py'])
