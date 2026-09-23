# Manual de Uso — Escáner de Puertos de Red

Universidad Estatal de Milagro (UNEMI)
Grupo #13 de Seguridad Informática

Este manual explica cómo instalar y utilizar el programa de escaneo de
puertos desarrollado en Python.

---

## Índice

1. [Requisitos](#1-requisitos)
2. [Instalación](#2-instalación)
3. [Cómo iniciar la aplicación](#3-cómo-iniciar-la-aplicación)
4. [Cómo ingresar la IP](#4-cómo-ingresar-la-ip)
5. [Cómo seleccionar el rango de puertos](#5-cómo-seleccionar-el-rango-de-puertos)
6. [Cómo ejecutar el escaneo](#6-cómo-ejecutar-el-escaneo)
7. [Cómo interpretar los resultados](#7-cómo-interpretar-los-resultados)
8. [Mensajes de error](#8-mensajes-de-error)
9. [Solución de problemas](#9-solución-de-problemas)
10. [Advertencia legal](#10-advertencia-legal)

---

## 1. Requisitos

| Requisito | Detalle |
|---|---|
| Computador | Windows, Linux o macOS |
| Python | Versión 3.6 o superior |
| Editor de código | Visual Studio Code (recomendado) |
| Bibliotecas | Ninguna externa: `socket` y `sys` vienen incluidas en Python |

Para comprobar si Python está instalado, abra una terminal y escriba:

```bash
python --version
```

Si el sistema responde con algo como `Python 3.12.1`, ya puede continuar. Si
aparece un error, descargue Python desde <https://www.python.org/downloads/>
y, en Windows, marque la casilla **Add Python to PATH** durante la
instalación.

---

## 2. Instalación

El programa es un único archivo, por lo que no requiere instalación formal.

**Opción A — Clonar el repositorio:**

```bash
git clone https://github.com/gcontrerasg2-cmd/scanner-puertos-python
cd scanner-puertos-python
```

**Opción B — Descarga manual:**

1. Ingrese al repositorio en GitHub.
2. Presione el botón verde **Code** y elija **Download ZIP**.
3. Descomprima la carpeta.
4. Ábrala con Visual Studio Code (**Archivo → Abrir carpeta**).

---

## 3. Cómo iniciar la aplicación

1. Abra una terminal dentro de la carpeta del proyecto (en VS Code:
   **Terminal → Nueva terminal**).
2. Ejecute:

```bash
python scanner_puertos.py
```

En Linux o macOS use `python3 scanner_puertos.py`.

Al iniciar, el programa muestra este encabezado y pide directamente la IP:

```
========================================
           ESCANER DE PUERTOS
========================================
IP:
```

---

## 4. Cómo ingresar la IP

Escriba la dirección del equipo a analizar y presione Enter:

| Valor | Significado |
|---|---|
| `127.0.0.1` | El propio computador |
| `192.168.1.10` | Otro equipo dentro de la misma red local |

**Importante:** este programa no valida si la dirección tiene un formato
correcto ni si el host existe. Si se deja el campo vacío, el programa muestra
un error y se cierra:

```
Error: Debe ingresar una dirección IP válida.
```

**¿Cómo conocer la IP del equipo?**

- Windows: ejecute `ipconfig` y revise *Dirección IPv4*.
- Linux o macOS: ejecute `ip a` o `ifconfig`.

Si va a escanear otro equipo de su red doméstica, ambos deben estar
conectados a la misma red (por ejemplo, el mismo Wi-Fi).

---

## 5. Cómo seleccionar el rango de puertos

El programa solicita dos valores:

```
Desde: 1
Hasta: 100
```

Reglas de validación del programa:

- Ambos valores deben ser números enteros (si se escribe texto, el programa
  se cierra con error).
- `Desde` debe ser mayor o igual a 1.
- `Hasta` debe ser menor o igual a 65535.
- `Desde` no puede ser mayor que `Hasta`.

Rangos sugeridos:

| Rango | Descripción |
|---|---|
| 1 – 100 | Prueba rápida, ideal para la demostración en clase |
| 1 – 1024 | Puertos conocidos (HTTP, FTP, SSH, etc.) |
| 1 – 65535 | Análisis completo — puede tardar varios minutos |

> **Nota:** este programa revisa los puertos uno por uno, sin ejecutar
> varias verificaciones al mismo tiempo. Por eso, rangos amplios (por
> ejemplo, más de 5000 puertos) tardan bastante. Para las pruebas se recomienda usar
> rangos moderados, como 1–1024.

---

## 6. Cómo ejecutar el escaneo

El escaneo empieza automáticamente después de ingresar el puerto final:

```
Escaneando...

Puerto 22 - ABIERTO
Puerto 80 - ABIERTO
```

El programa no muestra una barra de progreso: solo imprime una línea cada vez
que encuentra un puerto abierto. Si no aparece ninguna línea entre
"Escaneando..." y el resumen final, significa que no se encontró ningún
puerto abierto en ese rango.

Para interrumpir el escaneo antes de que termine, presione **Ctrl + C**. El
programa detecta la interrupción, muestra un aviso y de todas formas imprime
el resumen con lo analizado hasta ese momento:

```
[!] Escaneo interrumpido por el usuario.
```

---

## 7. Cómo interpretar los resultados

Al finalizar (o al interrumpirse) el escaneo, se muestra un resumen:

```
----------------------------------------
Puertos analizados: 100
Puertos abiertos: 2
Lista de puertos abiertos: [22, 80]
========================================
```

| Campo | Significado |
|---|---|
| **Puertos analizados** | Cantidad total de puertos revisados en el rango indicado |
| **Puertos abiertos** | Cuántos de esos puertos respondieron como accesibles |
| **Lista de puertos abiertos** | El número exacto de cada puerto abierto, solo aparece si se encontró al menos uno |

**Importante:** a diferencia de otras versiones del escáner, este programa
**no indica qué servicio corresponde a cada puerto** (por ejemplo, no dice
si el puerto 80 es HTTP). Solo informa si el puerto está abierto o no. Para
identificar el servicio, puede apoyarse en esta tabla de referencia:

| Puerto | Servicio habitual |
|---|---|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP (correo) |
| 53 | DNS |
| 80 | HTTP (páginas web) |
| 443 | HTTPS |
| 3306 | MySQL |
| 3389 | Escritorio remoto (RDP) |
| 8080 | HTTP alternativo, común en servidores de prueba |

Si la lista de puertos abiertos aparece vacía, es un resultado válido: quiere
decir que, en ese rango, el equipo no tiene servicios escuchando o un
firewall bloqueó las conexiones.

---

## 8. Mensajes de error

El programa puede detenerse con alguno de estos mensajes:

| Mensaje | Causa | Qué hacer |
|---|---|---|
| `Error: Debe ingresar una dirección IP válida.` | Se dejó el campo IP vacío | Vuelva a ejecutar el programa e ingrese una IP |
| `Error: Los puertos deben ser números enteros.` | Se escribió texto o un número decimal en "Desde" o "Hasta" | Ingrese solo números enteros |
| `Error: Rango de puertos inválido (...)` | El rango está fuera de 1–65535, o "Desde" es mayor que "Hasta" | Verifique los valores e inténtelo de nuevo |

En todos los casos el programa se cierra (`sys.exit(1)`) y debe ejecutarse
nuevamente desde el inicio.

---

## 9. Solución de problemas

| Problema | Causa probable | Solución |
|---|---|---|
| `python: command not found` | Python no instalado o fuera del PATH | Reinstale marcando *Add Python to PATH*; pruebe con `python3` |
| El escaneo tarda mucho | Rango de puertos muy amplio | Reduzca el rango (por ejemplo, a 1–1024) |
| No aparece ningún puerto abierto | Firewall activo o sin servicios corriendo | Pruebe primero con `127.0.0.1` y un servidor de prueba (ver abajo) |
| El programa se cierra apenas se ejecuta | Se ingresó un dato vacío o inválido | Revise que la IP y los puertos estén bien escritos |

**Para generar un puerto abierto de prueba** en el propio equipo, abra una
segunda terminal y ejecute:

```bash
python -m http.server 8080
```

Deje esa terminal abierta y, en la terminal del escáner, escanee `127.0.0.1`
en el rango 8000–8100. El puerto 8080 debe aparecer como `ABIERTO`. Esto sirve
para demostrar, en la sustentación, que el programa detecta correctamente
servicios reales.

---

## 10. Advertencia legal

El escaneo de puertos sobre equipos o redes ajenas, sin autorización del
propietario, puede constituir una infracción legal en Ecuador y en la mayoría
de países. Este programa se entrega con fines estrictamente académicos.

Realice las pruebas únicamente sobre su propio equipo o sobre otros equipos
de su red personal, con conocimiento de las personas involucradas.
