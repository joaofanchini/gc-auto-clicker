from pynput.keyboard import Controller, Key
import time

# Cria uma instância do controlador do teclado
teclado = Controller()

# Simula o pressionamento e a liberação da tecla Enter
teclado.press(Key.enter)
teclado.release(Key.enter)

# Aguarda um curto período (opcional)

while True:
# Exemplo adicional: Simula pressionamento contínuo da tecla Enter por 2 segundos
    time.sleep(0.3)
    teclado.press(Key.enter)
    time.sleep(0.2)
    teclado.release(Key.enter)
