"""Log-linear interpolation of discount factors. No extrapolation."""
import numpy as np
class DiscountCurve:
    def __init__(self,times,factors):
        self.times=np.array(times,dtype=float); self.factors=np.array(factors,dtype=float)
        if self.times.ndim!=1 or self.times.shape!=self.factors.shape or len(self.times)<2 or not np.all(np.isfinite(self.times)) or not np.all(np.isfinite(self.factors)) or self.times[0]!=0 or self.factors[0]!=1 or np.any(np.diff(self.times)<=0) or np.any(self.factors<=0): raise ValueError('Invalid curve; include (0,1)')
    def df(self,t):
        if not 0<=t<=self.times[-1]: raise ValueError('Outside curve')
        return float(np.exp(np.interp(t,self.times,np.log(self.factors))))
    def forward(self,start,end,accrual):
        if end<=start or accrual<=0: raise ValueError('Invalid period')
        return (self.df(start)/self.df(end)-1)/accrual
