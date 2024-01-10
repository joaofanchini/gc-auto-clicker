from pynput import keyboard

def on_press(key):
    try:
        print(f"Tecla pressionada: {key.char}")
    except AttributeError:
        # Tecla especial (não é um caractere)
        print(f"Tecla especial pressionada: {key}")

def solicitar_entrada():
    print("Digite algumas teclas e pressione Enter (ou 'exit' para sair):")

    while True:
        entrada = input("> ")
        if entrada.lower() == 'exit':
            break

        print(f"Você digitou: {entrada}")

if __name__ == "__main__":
    # Configura o listener de teclas
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Executa a função para solicitar entrada
    solicitar_entrada()

    # Encerra o listener de teclas
    listener.stop()
    listener.join()

    print("Programa encerrado.")
