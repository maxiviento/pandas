{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "padron_resultados_2011.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyN4kxM94q+7H9qUdDyoPIF+",
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
        "<a href=\"https://colab.research.google.com/github/maxiviento/pandas/blob/main/padron_resultados_2011.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vSxgruZqqwOS"
      },
      "source": [
        "import pandas as pd\n",
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "#https://www.justiciacordoba.gob.ar/Jel/Contenido/escrutinios.aspx"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YhAkd8UD_mn6"
      },
      "source": [
        "html_doc = 'https://www.justiciacordoba.gob.ar/Estatico/JEL/Escrutinios/ReportesEleccion20070902/Index.html'\n",
        "page = requests.get(html_doc)\n",
        "soup = BeautifulSoup(page.text, 'html.parser')\n",
        "select_combo = soup.find(id='cmbCircuitosTodos').findAll(\"option\")\n",
        "select_combo = select_combo[1:]\n",
        "lista=[]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OV3vLMPup6Vm"
      },
      "source": [
        "for value in select_combo:\n",
        "  v=str(value)\n",
        "  a=str(v).find('value=')\n",
        "  b=str(v).find('|')\n",
        "  n=v[a+7:b]\n",
        "  lista.append(n)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OS7nqzBSrH8T"
      },
      "source": [
        "lista_df =[]\n",
        "for p in lista:\n",
        "  p = str(p.replace(' ','%20'))\n",
        "  print(p)\n",
        "  url='https://www.justiciacordoba.gob.ar/Estatico/JEL/Escrutinios/ReportesEleccion20070902/Resultados/E20070902_C{}_CA2_0.htm'.format(p)\n",
        "  print(url)\n",
        "  try:\n",
        "    df_electores2011  = pd.read_html(url, match='Total de ELECTORES EN PADRON')\n",
        "    df = df_electores2011[0]\n",
        "    df = df.iloc[:,[9,11]]\n",
        "    circuito = df.loc[3,9]\n",
        "    print(circuito)\n",
        "    df['circuito']=circuito\n",
        "    df = df[df[11].notnull()]\n",
        "    lista_df.append(df)\n",
        "  except:\n",
        "    print('no se encontro')\n",
        "  \n",
        "df_unido = pd.concat(lista_df)\n",
        "df_unido.to_csv('unido2007.csv')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gl55P2Ft2ftj"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}