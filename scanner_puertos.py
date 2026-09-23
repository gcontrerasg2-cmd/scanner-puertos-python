import socket
import sys

def escanear_puerto(ip, puerto):
    """
    Intenta establecer una conexión TCP con el puerto especificado.
    Retorna True si el puerto está abierto, False en caso contrario.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            resultado = s.connect_ex((ip, puerto))
            return resultado == 0
    except (socket.timeout, socket.error):
        return False

def main():
    print("=" * 40)
    print("           ESCANER DE PUERTOS           ")
    print("=" * 40)

    # 1. Ingreso de la IP
    ip = input("IP: ").strip()
    if not ip:
        print("Error: Debe ingresar una dirección IP válida.")
        sys.exit(1)

    # 2 y 3. Ingreso del rango de puertos
    try:
        inicio = int(input("Desde: "))
        fin = int(input("Hasta: "))
    except ValueError:
        print("Error: Los puertos deben ser números enteros.")
        sys.exit(1)

    if inicio < 1 or fin > 65535 or inicio > fin:
        print("Error: Rango de puertos inválido (debe estar entre 1 y 65535, con 'Desde' <= 'Hasta').")
        sys.exit(1)

    # 4. Realizar el escaneo
    print("\nEscaneando...\n")
    
    puertos_abiertos = []
    total_analizados = (fin - inicio) + 1

    try:
        for puerto in range(inicio, fin + 1):
            if escanear_puerto(ip, puerto):
                # 5. Mostrar los puertos abiertos encontrados
                print(f"Puerto {puerto} - ABIERTO")
                puertos_abiertos.append(puerto)
    except KeyboardInterrupt:
        print("\n\n[!] Escaneo interrumpido por el usuario.")

    # 6. Mostrar el resumen de los resultados
    print("-" * 40)
    print(f"Puertos analizados: {total_analizados}")
    print(f"Puertos abiertos: {len(puertos_abiertos)}")
    if puertos_abiertos:
        print(f"Lista de puertos abiertos: {puertos_abiertos}")
    print("=" * 40)

if __name__ == "__main__":
    main()
