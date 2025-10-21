import click
import json
from mtcli_rvo.controllers.rvo_controller import processar_rvo
from mtcli_rvo.views.rvo_view import exibir_rvo
from mtcli.logger import setup_logger
from mtcli_rvo.conf import (
    SYMBOL,
    PERIOD,
    BARS,
    VOLUME,
    HISTORICO,
)


log = setup_logger()

@click.command(help="Plugin para cálculo e exibição do Volume Relativo (RVO).")
@click.version_option(package_name="mtcli-rvo")
@click.option("--symbol", "-s", default=SYMBOL, show_default=True, help="Ticker do ativo a ser analisado.")
@click.option("--period", "-p", default=PERIOD, show_default=True, help="Timeframe a ser analizado.")
@click.option("--bars", "-b", default=BARS, show_default=True, help="Número de barras para média do volume.")
@click.option("--volume", "-v", default=VOLUME, show_default=True, help="Tipo de volume tick ou real.")
@click.option("--historico", "-h", default=5, show_default=True, help="Número de candles a exibir no histórico.")
@click.option("--export", "-e", is_flag=True, help="Exporta o histórico do RVO para arquivo CSV.")
@click.option("--json", "-j", is_flag=True, help="Exporta o histórico do RVO em formato JSON.")
def rvo(symbol, period, bars, volume, historico, export, json):
    """
    Calcula e exibe o indicador RVO (Relative Volume Oscillator).
    """
    log.info(f"Calculando RVO para {symbol} ({period}, {bars} períodos, volume {volume}, histórico={historico}, export={export}, json={json})")
    resultado = processar_rvo(symbol, timeframe=period, periodos=bars, volume=volume, historico=historico, export=export, json_out=json)
    exibir_rvo(resultado, timeframe=period, export=export, json_out=json)


if __name__ == "__main__":
    rvo()
