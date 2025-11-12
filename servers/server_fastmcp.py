{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMTjC22Wn87wqSyXl0GkB6f",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rubenurbano/colab-pro-limp/blob/main/servers/server_fastmcp.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile server_fastmcp.py\n",
        "from fastmcp import FastMCP, tool\n",
        "\n",
        "app = FastMCP()\n",
        "\n",
        "@tool()\n",
        "def hola(nombre: str) -> str:\n",
        "    \"\"\"Saluda amablemente.\"\"\"\n",
        "    return f\"Hola {nombre}, soy tu servidor FastMCP funcionando correctamente 🚀\"\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    app.run()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RHNEM73g8xIe",
        "outputId": "6d3a7c56-5f7b-4a36-8f56-a05fbc122557"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting server_fastmcp.py\n"
          ]
        }
      ]
    }
  ]
}