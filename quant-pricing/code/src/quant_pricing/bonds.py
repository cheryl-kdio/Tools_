"""Cash flows supplied explicitly; prices in currency, not percent of par."""
from scipy.optimize import brentq
from .rates import discount_factor

def dirty_price(cashflows,curve):
    return sum(amount*curve.df(t) for t,amount in cashflows)

def accrued_interest(notional,coupon_rate,elapsed_fraction):
    return notional*coupon_rate*elapsed_fraction

def clean_price(dirty,accrued): return dirty-accrued

def price_from_yield(cashflows,ytm,frequency=2):
    return sum(c*discount_factor(ytm,t,'periodic',frequency) for t,c in cashflows)

def yield_to_maturity(cashflows,price,frequency=2):
    flows=list(cashflows)
    if price<=0 or not flows or any(t<=0 or c<0 for t,c in flows) or not any(c>0 for t,c in flows): raise ValueError('Positive future cash flows required')
    return brentq(lambda y:price_from_yield(flows,y,frequency)-price,-frequency+1e-8,100)

def duration(cashflows,ytm,frequency=2):
    flows=list(cashflows); p=price_from_yield(flows,ytm,frequency)
    mac=sum(t*c*discount_factor(ytm,t,'periodic',frequency) for t,c in flows)/p
    return {'macaulay':mac,'modified':mac/(1+ytm/frequency)}
