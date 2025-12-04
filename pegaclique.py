import pyautogui
import time

print("--- CAPTURADOR DE COORDENADAS ---")
print("Posicione o mouse em cima do botão/local desejado.")
print("A captura acontecerá em 5 segundos...")

# Contagem regressiva
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)

# Pega a posição atual
x, y = pyautogui.position()

print("-" * 30)
print(f"COORDENADA CAPTURADA: x={x}, y={y}")
print("-" * 30)