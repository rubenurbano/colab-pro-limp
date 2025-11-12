{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMRG0kMC4Zqt5cIkGfUgTVt",
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
    },
    {
      "cell_type": "code",
      "source": [
        "code = '''\n",
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
        "    app.run()\n",
        "'''\n",
        "\n",
        "with open(\"server_fastmcp.py\", \"w\", encoding=\"utf-8\") as f:\n",
        "    f.write(code)\n",
        "\n",
        "print(\"✅ Archivo Python real creado.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Kc5uzFsS_4VL",
        "outputId": "dca93af6-068f-48f2-de91-e567b00a5e76"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ Archivo Python real creado.\n"
          ]
        }
      ]
    }
  ]
}