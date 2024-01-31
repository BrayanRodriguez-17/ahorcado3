class Ahorcado:
    def __init__(self):
        self.palabra_secreta = "Ahorcado"
        self.letras_correctas = []
        self.intentos_restantes = 8
        self.muñeco = [ "  O", " \|/",  "  |", " / \\"]

    def mostrar_palabra(self):
        resultado = ''
        for letra in self.palabra_secreta:
            resultado += letra if letra in self.letras_correctas else '_'
            resultado += ' '
        return resultado

    def mostrar_muñeco(self):
        resultado = ''
        for i in range(8 - self.intentos_restantes):
            resultado += self.muñeco[i]
        return resultado

    def jugar(self):
        print("¡Bienvenido al Juego del Ahorcado!")
        print("Descubre la palabra oculta. ¡Buena suerte!")

        while self.intentos_restantes > 0:
            print(f"{self.mostrar_muñeco()}")
            print(self.mostrar_palabra())

            letra_usuario = self.obtener_letra()
            if letra_usuario in self.palabra_secreta and letra_usuario not in self.letras_correctas:
                self.letras_correctas = [letra_usuario] + self.letras_correctas
                print(f"¡Correcto! Letras correctas: {', '.join(self.letras_correctas)}")
            else:
                self.intentos_restantes -= 1
                print(f"Incorrecto. Te quedan {self.intentos_restantes} intentos.")

            if all(letra in self.letras_correctas for letra in self.palabra_secreta):
                print("¡Felicidades! ¡Has adivinado la palabra!")
                break

        if not all(letra in self.letras_correctas for letra in self.palabra_secreta):
            print(f"¡Lo siento! Se acabaron los intentos. La palabra era '{self.palabra_secreta}'.")
            print(self.mostrar_muñeco())

    def obtener_letra(self):
        while True:
            letra = input("Ingresa una letra: ")
            if letra:
                return letra
            else:
                print("Por favor, ingresa un carácter.")

juego = Ahorcado()
juego.jugar()
