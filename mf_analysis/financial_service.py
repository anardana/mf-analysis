from datetime import datetime
from pprint import pprint

from mf_analysis.coin_file_parse_service import parse, read_file
from mf_analysis.financial import xirr
from mf_analysis.headers import CoinExportHeaders


def xirr_zerodha(transactions, final_date, final_amount):
    cashflow = []
    for log in transactions:
        if log[CoinExportHeaders.status] == "Allotted":
            trade_date = datetime.strptime(log[CoinExportHeaders.trade_date], "%d/%m/%y")
            trade_amount = log[CoinExportHeaders.amount]
            cashflow.append((trade_date, 0 - float(trade_amount)))
        elif log[CoinExportHeaders.status] == "Redeemed":
            trade_date = datetime.strptime(log[CoinExportHeaders.trade_date], "%d/%m/%y")
            trade_amount = log[CoinExportHeaders.amount]
            cashflow.append((trade_date, float(trade_amount)))
    cashflow.append((datetime.strptime(final_date, "%d/%m/%y"), final_amount))

    return xirr(cashflow)


def xirr_zerodha_scheme_wise(isin, transactions, final_date, final_nav):
    cashflow = []
    count = 0

    for log in transactions:
        if log[CoinExportHeaders.isin] == isin:
            if log[CoinExportHeaders.status] == "Allotted":
                trade_date = datetime.strptime(log[CoinExportHeaders.trade_date], "%Y-%m-%d")
                trade_amount = log[CoinExportHeaders.amount]
                cashflow.append((trade_date, 0 - float(trade_amount)))
                count = count + float(log[CoinExportHeaders.units])
            elif log[CoinExportHeaders.status] == "Redeemed":
                trade_date = datetime.strptime(log[CoinExportHeaders.trade_date], "%Y-%m-%d")
                trade_amount = log[CoinExportHeaders.amount]
                cashflow.append((trade_date, float(trade_amount)))
                count = count - float(log[CoinExportHeaders.units])

    cashflow.append((datetime.strptime(final_date, "%Y-%m-%d"), (final_nav * count)))

    return xirr(cashflow)


def zerodha_get_all_isin(transactions):
    isin = set()
    for transaction in transactions:
        isin.add(transaction[CoinExportHeaders.isin])

    return isin


pprint(xirr_zerodha(parse(read_file("<>")), "10/03/19", <>))
