import sys

def calcular_cuota_mensual(monto, tasa_anual, meses):
    """Calcula la cuota mensual de un préstamo usando el sistema de amortización francés."""
    if tasa_anual == 0:
        return monto / meses
    
    tasa_mensual = (tasa_anual / 100) / 12
    cuota = (monto * tasa_mensual) / (1 - (1 + tasa_mensual) ** -meses)
    return cuota

if __name__ == '__main__':
    # Espera 3 argumentos: monto, tasa_anual, meses
    if len(sys.argv) == 4:
        try:
            monto = float(sys.argv[1])
            tasa_anual = float(sys.argv[2])
            meses = int(sys.argv[3])
            
            print("--- FinTech Solutions S.A. | División de Préstamos ---")
            print(f"Monto solicitado: ${monto:,.2f}")
            print(f"Tasa de interés anual: {tasa_anual}%")
            print(f"Plazo: {meses} meses")
            
            cuota_mensual = calcular_cuota_mensual(monto, tasa_anual, meses)
            total_pagar = cuota_mensual * meses
            
            print("\nResultado de la simulación:")
            print(f"- Cuota mensual estimada: ${cuota_mensual:,.2f}")
            print(f"- Total a pagar al final del plazo: ${total_pagar:,.2f}")
        except ValueError:
            print("Error: Los parámetros deben ser numéricos.")
            print("Uso: python main.py <monto> <tasa_interes_anual> <meses>")
    else:
        print("Error: Por favor, proporciona los parámetros del préstamo.")
        print("Uso: python main.py <monto> <tasa_interes_anual> <meses>")
        print("Ejemplo: python main.py 15000 12.5 24")