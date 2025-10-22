import MetaTrader5 as mt5

from mtcli.logger import setup_logger
from mtcli_rvo.models.rvo_model import calcular_rvo

log = setup_logger()

TIMEFRAMES = {
    "M1": mt5.TIMEFRAME_M1,
    "M5": mt5.TIMEFRAME_M5,
    "M15": mt5.TIMEFRAME_M15,
    "M30": mt5.TIMEFRAME_M30,
    "H1": mt5.TIMEFRAME_H1,
    "H4": mt5.TIMEFRAME_H4,
    "D1": mt5.TIMEFRAME_D1,
    "W1": mt5.TIMEFRAME_W1,
    "MN1": mt5.TIMEFRAME_MN1,
}


def converter_timeframe(tf_str: str):
    """Converte um texto como 'M5' ou 'H1' para o código do MT5."""
    return TIMEFRAMES.get(str(tf_str).upper(), mt5.TIMEFRAME_M5)


def processar_rvo(
    symbol: str,
    timeframe: str = "M5",
    periodos: int = 20,
    historico: int = 5,
    tipo_volume: str = "tick",
    export: bool = False,
    json_out: bool = False,
):
    """Controla o fluxo: cálculo, exibição e exportação opcional do RVO."""
    if tipo_volume.lower() not in ["tick", "real"]:
        log.error(f"Volume inválido {tipo_volume}")
        raise ValueError(f"Volume inválido {tipo_volume}")

    tf_code = converter_timeframe(timeframe)
    resultado = calcular_rvo(
        symbol,
        timeframe=tf_code,
        periodos=periodos,
        historico=historico,
        tipo_volume=tipo_volume,
    )

    if not resultado:
        log.error("Falha ao calcular RVO — sem dados retornados")
        return

    return resultado
