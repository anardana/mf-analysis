import enum


class CoinExportHeaders(enum.Enum):
    client_id = "client_id"
    isin = "isin"
    scheme_name = "scheme_name"
    plan = "plan"
    transaction_mode = "transaction_mode"
    trade_date = "trade_date"
    ordered_at = "ordered_at"
    folio_number = "folio_number"
    amount = "amount"
    units = "units"
    nav = "nav"
    status = "status"
    remarks = "remarks"


class AmfiHeaders(enum.Enum):
    scheme_code = "Scheme Code"
    isin_payout_growth = "ISIN Div Payout/ ISIN Growth"
    isin_dividend_reinvestment = "ISIN Div Reinvestment"
    scheme_name = "Scheme Name"
    nav = "Net Asset Value"
    repurchase_prise = "Repurchase Price"
    sale_price = "Sale Price"
    date = "Date"
