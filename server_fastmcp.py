
from fastmcp import FastMCP, tool

app = FastMCP()

@tool()
def hola(nombre: str) -> str:
    """Saluda amablemente."""
    return f"Hola {nombre}, soy tu servidor FastMCP funcionando correctamente 🚀"

if __name__ == "__main__":
    app.run()
