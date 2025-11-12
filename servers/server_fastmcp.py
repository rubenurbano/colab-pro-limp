from fastmcp import FastMCP
from fastmcp.tools import FunctionTool

def hola(nombre: str) -> str:
    """Saluda amablemente."""
    return f"Hola {nombre}, soy tu servidor FastMCP funcionando correctamente 🚀"

# Registrar la herramienta al construir FastMCP
app = FastMCP(tools=[FunctionTool.from_function(hola)])

if __name__ == "__main__":
    app.run()
