import os

from mtcli.conf import config

SYMBOL = os.getenv("SYMBOL", config["DEFAULT"].get("symbol", fallback="WIN$N"))
PERIOD = os.getenv("PERIOD", config["DEFAULT"].get("period", fallback="M5"))
BARS = os.getenv("BARS", config["DEFAULT"].getint("bars", fallback=20))
HISTORICO = os.getenv("HISTORICO", config["DEFAULT"].getint("historico", fallback=5))
VOLUME = os.getenv("VOLUME", config["DEFAULT"].get("volume", fallback="tick"))
DIGITOS = os.getenv("DIGITOS", config["DEFAULT"].getint("digitos", fallback=0))
