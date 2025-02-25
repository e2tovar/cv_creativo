import subprocess


# Lanzar la aplicación de Streamlit
print("Iniciando la aplicación...")
# Ejecutar app.py usando streamlit run con la ruta absoluta
subprocess.run(["streamlit", "run", 'app.py'])
