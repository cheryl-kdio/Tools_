"""Rates in decimal units, times in years."""
import math

def accumulation(rate, time, convention='simple', frequency=1):
    if time < 0 or frequency <= 0: raise ValueError('Invalid time/frequency')
    if convention == 'continuous': return math.exp(rate*time)
    if convention == 'simple': factor = 1+rate*time
    elif convention == 'periodic':
        if 1+rate/frequency <= 0: raise ValueError('Invalid periodic base')
        factor = (1+rate/frequency)**(frequency*time)
    else: raise ValueError('Unknown convention')
    if factor <= 0: raise ValueError('Nonpositive factor')
    return factor

def discount_factor(rate,time,convention='continuous',frequency=1):
    return 1/accumulation(rate,time,convention,frequency)

def convert_rate(rate,time,source='simple',target='continuous',source_frequency=1,target_frequency=1):
    if time <= 0 or target_frequency <= 0: raise ValueError('Invalid time/frequency')
    a = accumulation(rate,time,source,source_frequency)
    if target == 'simple': return (a-1)/time
    if target == 'continuous': return math.log(a)/time
    if target == 'periodic': return target_frequency*math.expm1(math.log(a)/(target_frequency*time))
    raise ValueError('Unknown target')

def overnight_factor(rates, days, basis=360):
    """One fixing per observation interval; days includes weekends/holidays."""
    rates, days = list(rates), list(days)
    if len(rates)!=len(days) or not days or basis<=0 or any(d<=0 for d in days): raise ValueError('Invalid observations')
    return math.prod(accumulation(r,d/basis) for r,d in zip(rates,days))

def compounded_overnight_rate(rates,days,basis=360):
    days=list(days)
    return (overnight_factor(rates,days,basis)-1)*basis/sum(days)

def estr_interest(notional,rates,days):
    return notional*(overnight_factor(rates,days)-1)

def euribor_interest(notional,fixing,accrual,spread=0):
    return notional*(fixing+spread)*accrual
