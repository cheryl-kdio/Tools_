"""European vanilla options, continuous rates and dividend yield."""
import math
from scipy.special import ndtr
from scipy.optimize import brentq

def _sign(kind):
    if kind not in ('call','put'): raise ValueError('call or put required')
    return 1 if kind=='call' else -1

def black76(forward,strike,time,rate,vol,kind='call'):
    s=_sign(kind)
    if min(forward,strike)<=0 or min(time,vol)<0: raise ValueError('Invalid inputs')
    df=math.exp(-rate*time)
    if time==0 or vol==0: return df*max(s*(forward-strike),0)
    v=vol*math.sqrt(time); d1=math.log(forward/strike)/v+v/2; d2=d1-v
    return df*s*(forward*ndtr(s*d1)-strike*ndtr(s*d2))

def black_scholes(spot,strike,time,rate,vol,kind='call',dividend=0):
    return black76(spot*math.exp((rate-dividend)*time),strike,time,rate,vol,kind)

def greeks(spot,strike,time,rate,vol,kind='call',dividend=0):
    s=_sign(kind)
    if min(spot,strike,time,vol)<=0: raise ValueError('Positive inputs required')
    root=math.sqrt(time); d1=(math.log(spot/strike)+(rate-dividend+vol**2/2)*time)/(vol*root); d2=d1-vol*root
    p=math.exp(-d1*d1/2)/math.sqrt(2*math.pi); dq=math.exp(-dividend*time); dr=math.exp(-rate*time)
    return dict(delta=s*dq*ndtr(s*d1),gamma=dq*p/(spot*vol*root),vega=spot*dq*p*root,theta=-spot*dq*p*vol/(2*root)+s*dividend*spot*dq*ndtr(s*d1)-s*rate*strike*dr*ndtr(s*d2),rho=s*strike*time*dr*ndtr(s*d2))

def implied_volatility(price,spot,strike,time,rate,kind='call',dividend=0):
    if time<=0: raise ValueError('Positive maturity required')
    f=lambda v:black_scholes(spot,strike,time,rate,v,kind,dividend)-price
    if f(0)==0: return 0.0
    if f(0)>0 or f(10)<=0: raise ValueError('Price outside supported volatility bracket [0,10)')
    return brentq(f,0,10)
