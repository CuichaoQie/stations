{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/CuichaoQie/stations/blob/master/stations.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3iBf-V_tORpA",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 70
        },
        "outputId": "210dc507-1da3-483a-c420-71e93b52fa21"
      },
      "source": [
        "import re, requests, colorama\n",
        "from pprint import pformat\n",
        "\n",
        "colorama.init()\n",
        "\n",
        "url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9028'\n",
        "response = requests.get(url, verify=False)\n",
        "stations = re.findall(u'([\\u4e00-\\u9fa5]+)\\|([A-Z]+)', response.text)\n",
        "str = pformat(dict(stations), indent=4)\n",
        "\n",
        "f = open('station.py', 'w', encoding='utf-8')\n",
        "f.write('stations = ' + str)\n",
        "f.close()"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/urllib3/connectionpool.py:847: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
            "  InsecureRequestWarning)\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G0CnXus6T7kA",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}