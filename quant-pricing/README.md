# Quant Pricing — bibliothèque Python

Bibliothèque pédagogique de valorisation en finance quantitative, compatible Python 3.11+. Taux, spreads et volatilités en décimal (100 bp = 0,01). Temps en années, montants en devise. Les exemples sont fictifs, sans données de marché live.

## Structure

- `code/src/quant_pricing/conventions.py` : fractions d'année ACT/360, ACT/365F, ACT/ACT ISDA, 30E/360 Eurobond (pas la variante ISDA).
- `rates.py` : accumulation simple, périodique, continue, conversion, actualisation, €STR composé et coupon Euribor.
- `curves.py` : courbe de facteurs d'actualisation, interpolation log-linéaire, taux forward simple. Pas d'extrapolation.
- `bonds.py` : prix sale/propre, coupon couru, rendement actuariel, durations Macaulay et modifiée.
- `irs.py` : jambes fixe et variable, NPV, taux au pair.
- `trs.py` : rendement total, NPV, spread au pair.
- `options.py` : Black-Scholes-Merton, Black-76, grecques BSM et volatilité implicite BSM.
- `code/notebooks/` : exemples interactifs.
- `tests/` : tests numériques et identités financières.
- `pyproject.toml` : dépendances et installation du package.

## Installation

Depuis la racine :

```bash
python -m venv .venv
```

Activer avec `source .venv/bin/activate` (Linux/macOS) ou `.\.venv\Scripts\Activate.ps1` (PowerShell), puis :

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
jupyter lab
```

## Hypothèses et API

### Taux
`accumulation(r,t,convention,frequency)` renvoie 1+r*t (simple), (1+r/m)^(m*t) (periodic), exp(r*t) (continuous). `discount_factor` est son inverse. `convert_rate` conserve le facteur d'accumulation à l'horizon choisi.

`overnight_factor(rates,days,basis=360)` calcule le produit des (1+r_i*d_i/360). Chaque fixing couvre le nombre de jours calendaires fourni, y compris week-ends et jours fériés. `compounded_overnight_rate` annualise le rendement. `estr_interest` retourne le montant des intérêts. Aucun calendrier ni lookback, lockout ou observation shift automatique. `euribor_interest` calcule un coupon simple avec fraction d'année fournie (normalement ACT/360). Ne pas traiter Euribor comme un overnight.

### Courbes et obligations
`DiscountCurve(times,factors)` exige un point (0,1), puis des temps croissants et facteurs strictement positifs. `forward(start,end,accrual)` utilise (DF(start)/DF(end)-1)/accrual. Une courbe de projection distincte peut être utilisée pour les forwards. Les courbes sont fournies, non calibrées.

`dirty_price(cashflows,curve)` actualise les couples (temps de paiement, montant). Le principal doit être inclus dans le dernier flux. `clean_price(dirty,accrued)` soustrait le coupon couru. `accrued_interest` suppose un coupon fixe et une fraction courue déjà déterminée selon le contrat. Pas de règles ex-coupon. `price_from_yield` utilise un rendement nominal composé à la fréquence spécifiée, avec temps cohérents avec cette convention. `yield_to_maturity` suppose des flux positifs et une racine dans la borne numérique utilisée. `duration` renvoie les durations en années. Prix en devise, pas en pourcentage du nominal.

### IRS
`irs_npv(notional,fixed_rate,fixed_periods,float_periods,discount,pay_fixed=True,spread=0)` retourne PV variable moins PV fixe pour le payeur fixe. Périodes fixes : (temps de paiement, fraction d'année). Périodes variables : (temps de paiement, fraction d'année, taux annualisé déjà fixé ou projeté). `par_swap_rate` résout la NPV nulle. Pour un OIS, fournir le taux effectif composé annualisé compatible avec la fraction d'année. Échéanciers et fixings à déterminer en amont; pas d'échange de nominal.

### TRS
`total_return(start_price,end_price,income)` calcule (prix final - prix initial + revenus)/prix initial. Utiliser des prix cohérents (dirty pour une obligation et coupons versés). `trs_npv` reçoit des périodes (temps de paiement, fraction d'année, rendement total de période, rendement de financement de période). Le spread annuel est ajouté simplement. NPV positive = gain pour receveur de performance. `par_trs_spread` donne le spread annualisé annulant la NPV. Modèle linéaire, même devise, nominal constant, sans échange de principal. Pour les périodes futures, les rendements fournis doivent être des espérances compatibles avec la mesure de pricing et l'actualisation; des prévisions historiques ne suffisent pas à obtenir une juste valeur. Pas de modélisation du reset stochastique, repo, crédit, FX, collatéral ou optionalité.

### Options
`black_scholes(spot,strike,time,rate,vol,kind='call',dividend=0)` et `black76(forward,strike,time,rate,vol,kind='call')` : options européennes, taux continus, volatilité constante, sous-jacent et strike positifs. `greeks` : delta, gamma, vega par unité de volatilité, theta par année de temps écoulé, rho par unité de taux. Diviser vega/rho par 100 pour une variation d'un point de pourcentage. `implied_volatility` utilise Brent avec une borne supérieure de 10 (1000 %), pas de garantie de solution hors de cette plage.

## Limites

Pas de calendrier TARGET, génération automatique des échéanciers, conventions de règlement, bootstrap, calibration de smile, ajustements XVA, options américaines ou modèle normal Bachelier. Ce code n'est pas un moteur de production validé. Les paramètres contractuels doivent être vérifiés avant toute valorisation réelle.

## Références

- BCE, [€STR](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_short-term_rate/html/eurostr_overview.en.html).
- EMMI, [Euribor](https://www.emmi-benchmarks.eu/faq/euribor/).
- OpenGamma Strata, [Day Counts](https://strata.opengamma.io/day_counts/).
- Black & Scholes (1973), The Pricing of Options and Corporate Liabilities; Black (1976), The Pricing of Commodity Contracts.
