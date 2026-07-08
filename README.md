# Air Passengers — Time Series Analysis

Trend, seasonality, 12-month moving average, seasonal decomposition, and stationarity testing (ADF) on the classic Air Passengers dataset (monthly international airline passenger totals, 1949–1960). Coursework project, MS Data Science, UET Lahore.

---

## Dataset

- **Source:** Classic Box-Jenkins Air Passengers dataset (also used in [Kaggle's intro-to-time-series-analysis notebook](https://www.kaggle.com/code/bryanb/introduction-to-time-series-analysis))
- **Records:** 144 monthly observations, Jan 1949 – Dec 1960
- **Columns:** `Month` (YYYY-MM), `#Passengers` (monthly total in thousands)
- **Missing values:** 0

## Analysis Performed

1. **Trend** — monthly passenger totals plotted over the full 12-year span
2. **12-month moving average** — smooths seasonal noise to isolate the underlying growth trend
3. **Monthly boxplots** — shows seasonality, which months are consistently high/low
4. **Seasonal decomposition** — multiplicative model (trend × seasonal × residual), chosen because seasonal amplitude grows with the trend
5. **Stationarity (ADF test)** — raw series vs. first-differenced series

## Key Findings

- Strong upward trend across all 12 years — final-year average is roughly **276% higher** than the first year, reflecting the rapid growth of commercial air travel post-WWII
- Clear annual seasonality: peaks around **July** (summer travel), dips around **November** (winter low season)
- Seasonal swing widens over time → multiplicative decomposition fits better than additive
- Raw series is **non-stationary** (ADF p = 0.99); first-differencing brings it closer to stationary (ADF p = 0.054), confirming the trend must be removed before classical forecasting models (ARIMA) can be applied

Full written conclusion with all statistics: [`conclusion.md`](conclusion.md)

## How to Run

```bash
pip install pandas matplotlib statsmodels --break-system-packages
python3 analysis.py
```

Outputs land in `outputs/plots/` (5 PNGs) and `outputs/conclusion.md`.

## Files

```
├── README.md
├── Air_Passenger.csv
├── analysis.py
└── outputs/
    ├── conclusion.md
    └── plots/
        ├── 01_trend.png
        ├── 02_moving_average.png
        ├── 03_monthly_boxplot.png
        ├── 04_seasonal_decomposition.png
        └── 05_differenced_series.png
```
