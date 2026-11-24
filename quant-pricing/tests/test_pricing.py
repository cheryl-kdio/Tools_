from datetime import date
import math
import pytest
from quant_pricing.conventions import year_fraction
from quant_pricing.rates import *
from quant_pricing.curves import DiscountCurve
from quant_pricing.bonds import *
from quant_pricing.irs import *
from quant_pricing.trs import *
from quant_pricing.options import *

def test_days():
    assert year_fraction(date(2024,1,1),date(2025,1,1),'ACT/ACT ISDA') == 1
    assert year_fraction(date(2024,1,1),date(2024,2,1)) == pytest.approx(31/360)
    assert year_fraction(date(2024,1,31),date(2024,3,31),'30E/360') == pytest.approx(60/360)
    assert year_fraction(date(2023,1,1),date(2024,1,1),'ACT/365F') == 1

def test_rates():
    assert overnight_factor([.03,.04],[3,1]) == pytest.approx((1+.03*3/360)*(1+.04/360))
    assert estr_interest(100,[0],[3]) == 0
    assert euribor_interest(100,.04,.5) == 2
    assert accumulation(convert_rate(.04,2,'simple','continuous'),2,'continuous') == pytest.approx(1.08)
    assert overnight_factor([-.01],[3]) < 1

def curve(): return DiscountCurve([0,1,2],[1,math.exp(-.03),math.exp(-.06)])

def test_curve():
    c=curve(); assert c.df(.5)==pytest.approx(math.exp(-.015))
    assert c.forward(0,1,1)==pytest.approx(math.expm1(.03))
    with pytest.raises(ValueError): c.df(3)

def test_bond():
    flows=[(1,5),(2,105)]
    assert price_from_yield(flows,.05,1)==pytest.approx(100)
    assert yield_to_maturity(flows,100,1)==pytest.approx(.05)
    assert dirty_price(flows,curve())==pytest.approx(5*math.exp(-.03)+105*math.exp(-.06))
    assert clean_price(101,accrued_interest(100,.04,.25))==100
    assert duration([(2,100)],.05,1)['macaulay']==pytest.approx(2)

def test_irs():
    c=curve(); fixed=[(1,1),(2,1)]; floating=[(1,1,c.forward(0,1,1)),(2,1,c.forward(1,2,1))]
    r=par_swap_rate(fixed,floating,c)
    assert irs_npv(1e6,r,fixed,floating,c)==pytest.approx(0,abs=1e-9)
    assert irs_npv(1e6,.02,fixed,floating,c)==-irs_npv(1e6,.02,fixed,floating,c,False)

def test_trs():
    c=curve(); p=[(1,1,total_return(100,105,2),.03)]
    assert par_trs_spread(p,c)==pytest.approx(.04)
    assert trs_npv(1e6,p,c,.04)==pytest.approx(0,abs=1e-9)

def test_options():
    call=black_scholes(100,100,1,.05,.2); put=black_scholes(100,100,1,.05,.2,'put')
    assert call==pytest.approx(10.450583572185565)
    assert call-put==pytest.approx(100-100*math.exp(-.05))
    assert implied_volatility(call,100,100,1,.05)==pytest.approx(.2)
    assert black76(100,90,0,.05,.2)==10
    assert greeks(100,100,1,.05,.2)['delta']==pytest.approx(.63683065)
