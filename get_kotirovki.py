import pandas as pd
import requests

def get_kotirovki(date_from, date_till, date_interval, symbol_list):
    """
    Получает котировки для заданного временного диапазона и имени ценной бумаги.

    Аргументы:
    - date_from (str): Начальная дата в формате 'YYYY-MM-DD'.
    - date_till (str): Конечная дата в формате 'YYYY-MM-DD'.
    - date_interval (int): Интервал времени между котировками.
    - symbol_list (list of str): Список символов ценных бумаг.

    Возвращает:
    pandas.DataFrame: DataFrame с котировками для указанного диапазона дат.

    Пример использования:
    >>> df = get_kotirovki('2024-01-29', '2024-02-02', 1, ['symbol1', 'symbol2'])
    """
    str_html = r'http://iss.moex.com/iss/engines/stock/markets/shares/securities'
    frames = pd.DataFrame()
    for symbol in symbol_list:
        j = (requests.get(
            f'{str_html}/{symbol}/candles.json?from={date_from}&till={date_till}&interval={date_interval}').json())

        data = [{k: r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]
        frame = pd.DataFrame(data)
        frame['symbol'] = symbol
        frames = pd.concat([frames, frame])
    return frames
