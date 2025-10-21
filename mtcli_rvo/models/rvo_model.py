import MetaTrader5 as mt5
import pandas as pd
from mtcli.mt5_context import mt5_conexao
from mtcli.logger import setup_logger

log = setup_logger()

def calcular_rvo(symbol: str, timeframe: int, periodos: int = 20, historico: int = 5):
    """
    Calcula o Relative Volume Oscillator (RVO) e retorna o valor atual e histórico recente.
    """
    with mt5_conexao():
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, periodos + historico)
        if rates is None or len(rates) == 0:
            log.error(f"Sem dados para {symbol}")
            return None

    df = pd.DataFrame(rates)
    df["volume_ma"] = df["tick_volume"].rolling(periodos).mean()
    df["rvo"] = df["tick_volume"] / df["volume_ma"]

    # Últimos valores válidos
    ultimos = df.tail(historico).copy()
    rvo_atual = ultimos["rvo"].iloc[-1]
    vol_atual = ultimos["tick_volume"].iloc[-1]
    vol_medio = ultimos["volume_ma"].iloc[-1]

    return {
        "symbol": symbol,
        "rvo_atual": rvo_atual,
        "volume_atual": vol_atual,
        "volume_medio": vol_medio,
        "historico": ultimos[["time", "rvo"]].to_dict("records"),
    }
