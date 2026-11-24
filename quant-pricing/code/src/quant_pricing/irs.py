"""Schedules resolved externally. Periods: (payment time, accrual fraction)."""
def fixed_annuity(periods,discount):
    return sum(a*discount.df(t) for t,a in periods)

def fixed_leg(notional,rate,periods,discount):
    return notional*rate*fixed_annuity(periods,discount)

def floating_leg(notional,periods,discount,spread=0):
    """Periods: (payment time, accrual fraction, fixing or projected rate)."""
    return notional*sum(a*(r+spread)*discount.df(t) for t,a,r in periods)

def irs_npv(notional,fixed_rate,fixed_periods,float_periods,discount,pay_fixed=True,spread=0):
    pv=floating_leg(notional,float_periods,discount,spread)-fixed_leg(notional,fixed_rate,fixed_periods,discount)
    return pv if pay_fixed else -pv

def par_swap_rate(fixed_periods,float_periods,discount,spread=0):
    return floating_leg(1,float_periods,discount,spread)/fixed_annuity(fixed_periods,discount)
