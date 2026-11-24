"""Linear same-currency TRS, fixed notional per supplied period.
Return inputs are realized or pricing-measure expected total returns, not forecasts
of historical performance. Cash flows assumed settled at supplied payment times.
"""
def total_return(start_price,end_price,income=0):
    if start_price<=0: raise ValueError('Positive initial price required')
    return (end_price-start_price+income)/start_price

def trs_npv(notional,periods,discount,spread=0,receive_return=True):
    """Periods: (payment time, accrual, total return, funding period return).
    Funding period return is already accrued (e.g. overnight factor minus one).
    Spread is annualized, added simply. No principal exchange.
    """
    pv=notional*sum((ret-funding-spread*a)*discount.df(t) for t,a,ret,funding in periods)
    return pv if receive_return else -pv

def par_trs_spread(periods,discount):
    periods=list(periods)
    return trs_npv(1,periods,discount)/sum(a*discount.df(t) for t,a,_,_ in periods)
