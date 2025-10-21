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
@click.option("--symbol", "-s", default=SYMBOL, show_default=True, help="Simbolo do ativo.")
@click.option("--period", "-p", default=PERIOD, show_default=True, help="Timeframe (ex: M1, M5, M15, H1, D1).")
@click.option("--bars", "-b", default=BARS, show_default=True, help="Número de barras para média de volume.")
@click.option("--historico", "-h", default=5, show_default=True, help="Número de candles a exibir no histórico.")
@click.option("--export", "-e", is_flag=True, help="Exporta o histórico do RVO para arquivo CSV.")
@click.option("--json", "-j", is_flag=True, help="Exporta o histórico do RVO em formato JSON.")
def rvo(symbol, period, bars, historico, export, json):
    """
    Calcula e exibe o indicador RVO (Relative Volume Oscillator) com histórico, exportação e opções CLI.
    """
    log.info(f"Calculando RVO para {symbol} ({period}, {bars} períodos, histórico={historico}, export={export}, json={json})")
    resultado = processar_rvo(symbol, timeframe=period, periodos=bars, historico=historico, export=export, json_out=json)
    exibir_rvo(resultado, timeframe=period, export=export, json_out=json)


if __name__ == "__main__":
    rvo()
