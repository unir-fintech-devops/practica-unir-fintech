# Práctica UNIR - FinTech Solutions S.A.

Este repositorio contiene el código base para la actividad grupal de flujos de trabajo con Git y GitHub.

El proyecto consiste en un simulador de préstamos desarrollado en Python. La aplicación recibe el monto del crédito, la tasa de interés anual y el plazo en meses, devolviendo la cuota mensual estimada.

## Requisitos
- Python 3.x
- Make (opcional, para automatizar comandos con el Makefile)

## Ejecución básica
Para probar la aplicación en local, debes pasar los 3 parámetros en el siguiente orden: monto, interés y meses. Ejecuta en tu terminal:

```bash
python main.py 10000 15 12
```

### Ejemplo de salida en consola
Si ejecutas el comando anterior, la aplicación devolverá la siguiente simulación:

```text
--- FinTech Solutions S.A. | División de Préstamos ---
Monto solicitado: $10,000.00
Tasa de interés anual: 15.0%
Plazo: 12 meses
```

Resultado de la simulación:
- Cuota mensual estimada: $902.58
- Total a pagar al final del plazo: $10,831.00


## Uso con Makefile
Para facilitar las pruebas, puedes utilizar los comandos preconfigurados con make:

- Ejecutar make run: Lanza una simulación estándar de $10,000 a 12 meses.
- Ejecutar make test: Lanza una simulación de prueba de $50,000 a 60 meses.