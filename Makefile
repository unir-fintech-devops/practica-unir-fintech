### `Makefile`
Modificado para inyectar los parámetros correctos del préstamo en lugar de palabras.

```makefile
.PHONY: run test

# Ejecuta una simulación de préstamo estándar (ej. $10,000 a 15% por 12 meses)
run:
	python main.py 10000 15 12

# Comando de prueba con un préstamo a largo plazo (ej. $50,000 a 8.5% por 60 meses)
test:
	python main.py 50000 8.5 60