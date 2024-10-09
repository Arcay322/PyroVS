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
    port = 5000  # Establecer un puerto
    daemon = Pyro4.Daemon(port=port)  # Iniciar el servidor Pyro en el puerto especificado
    uri = daemon.register(FactorialServer)  # Registrar el objeto remoto

    # Localizar el servicio de nombres
    ns = Pyro4.locateNS(host='127.0.0.1', port=9090)  
    ns.register("example.factorial", uri)  # Registrar el objeto con un nombre

    print("Servidor de factorial listo en puerto", port)
    daemon.requestLoop()  # Iniciar el bucle del servidor

if __name__ == "__main__":
    start_server()
