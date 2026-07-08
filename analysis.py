"""
Air Passengers — Time Series Analysis
Classic monthly international airline passenger totals (1949-1960).

Covers: trend visualization, 12-month moving average, monthly seasonality
boxplots, additive seasonal decomposition, stationarity (ADF) test on raw
vs. first-differenced series, and a written conclusion.
"""

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

DATA_FILE = "Air_Passenger.csv"
OUT_DIR = "outputs/plots"


def load_data():
    df = pd.read_csv(DATA_FILE)
    df["Month"] = pd.to_datetime(df["Month"], format="%Y-%m")
    df = df.set_index("Month")
    return df["#Passengers"]


def main():
    series = load_data()
    print(f"Loaded {len(series)} monthly records: {series.index.min().date()} -> {series.index.max().date()}")
    print(f"Missing values: {series.isna().sum()}")

    # 1. Trend plot
    plt.figure(figsize=(11, 4))
    series.plot(title="Air Passengers — Monthly Totals (Trend)")
    plt.ylabel("Passengers (thousands)")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/01_trend.png", dpi=110)
    plt.close()

    # 2. 12-month moving average
    plt.figure(figsize=(11, 4))
    series.plot(alpha=0.4, label="Monthly total")
    series.rolling(12).mean().plot(label="12-month moving average", linewidth=2)
    plt.title("Air Passengers — 12-Month Moving Average")
    plt.ylabel("Passengers (thousands)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/02_moving_average.png", dpi=110)
    plt.close()

    # 3. Monthly boxplots (seasonality)
    df_box = series.to_frame("value")
    df_box["month"] = df_box.index.month
    plt.figure(figsize=(11, 5))
    df_box.boxplot(column="value", by="month")
    plt.title("Air Passengers — Monthly Distribution (Seasonality)")
    plt.suptitle("")
    plt.xlabel("Month")
    plt.ylabel("Passengers (thousands)")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/03_monthly_boxplot.png", dpi=110)
    plt.close()

    # 4. Seasonal decomposition
    decomposition = seasonal_decompose(series, model="multiplicative", period=12)
    fig = decomposition.plot()
    fig.set_size_inches(11, 8)
    fig.suptitle("Air Passengers — Seasonal Decomposition (Multiplicative)", y=1.02)
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/04_seasonal_decomposition.png", dpi=110)
    plt.close()

    # 5. Stationarity: raw vs differenced
    adf_raw = adfuller(series)
    diff = series.diff().dropna()
    adf_diff = adfuller(diff)

    plt.figure(figsize=(11, 4))
    diff.plot(title="Air Passengers — First-Differenced Series", color="darkorange")
    plt.ylabel("Change in passengers")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/05_differenced_series.png", dpi=110)
    plt.close()

    # Analysis summary
    strongest_month = df_box.groupby("month")["value"].mean().idxmax()
    weakest_month = df_box.groupby("month")["value"].mean().idxmin()
    growth = (series.iloc[-12:].mean() / series.iloc[:12].mean() - 1) * 100

    conclusion = f"""
Trend: Passenger volume shows a strong, steady upward trend across all 12 years (1949-1960),
with the final-year average roughly {growth:.0f}% higher than the first-year average — driven by
the post-war growth of commercial air travel.

Seasonality: Clear annual seasonality is present, peaking around month {strongest_month}
(summer travel season) and dipping around month {weakest_month} (winter low season). The
seasonal amplitude grows over time, which is why a multiplicative decomposition model fits
better than an additive one.

Cycles: No distinct multi-year business cycle is visible beyond the dominant trend and
seasonal pattern — the growth is largely monotonic rather than cyclical.

Stationarity: Raw series ADF statistic = {adf_raw[0]:.3f}, p-value = {adf_raw[1]:.4f}
({'stationary' if adf_raw[1] < 0.05 else 'non-stationary, as expected given the strong trend'}).
After first-differencing, ADF statistic = {adf_diff[0]:.3f}, p-value = {adf_diff[1]:.4f}
({'stationary' if adf_diff[1] < 0.05 else 'still non-stationary'}), confirming that removing the
trend is necessary before applying classical forecasting models.

Potential research questions: (1) Can the multiplicative seasonal pattern be used to forecast
short-term capacity planning for airlines? (2) How would an external shock (e.g. fuel price
spike, pandemic) alter the otherwise stable growth trend seen here?
"""

    with open("outputs/conclusion.md", "w") as f:
        f.write("# Air Passengers — Time Series Analysis: Conclusion\n")
        f.write(conclusion)

    print(conclusion)
    print("\nAll plots saved to outputs/plots/. Conclusion saved to outputs/conclusion.md")


if __name__ == "__main__":
    main()
