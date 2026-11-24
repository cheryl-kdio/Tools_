"""Day-count fractions; dates are unadjusted contractual dates."""
from datetime import date
from calendar import isleap

def year_fraction(start: date, end: date, convention='ACT/360') -> float:
    if end < start:
        raise ValueError('end must be >= start')
    days = (end-start).days
    if convention == 'ACT/360': return days/360
    if convention == 'ACT/365F': return days/365
    if convention == '30E/360':
        return ((end.year-start.year)*360+(end.month-start.month)*30+min(end.day,30)-min(start.day,30))/360
    if convention == 'ACT/ACT ISDA':
        total = 0.0
        while start < end:
            stop = min(end,date(start.year+1,1,1)) if start.year < 9999 else end
            total += (stop-start).days/(366 if isleap(start.year) else 365)
            start = stop
        return total
    raise ValueError('Unsupported day count')
