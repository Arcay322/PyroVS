import Pyro4

@Pyro4.expose
class FactorialServer:
    def factorial(self, n):
        if n < 0:
            raise ValueError("El número debe ser no negativo.")
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

def start_server():
    daemon = Pyro4.Daemon()  # Iniciar el servidor Pyro
    uri = daemon.register(FactorialServer)  # Registrar el objeto remoto
    ns = Pyro4.locateNS()  # Localizar el servicio de nombres
    ns.register("example.factorial", uri)  # Registrar el objeto con un nombre

    print("Servidor de factorial listo.")
    daemon.requestLoop()  # Iniciar el bucle del servidor

if __name__ == "__main__":
    start_server()
