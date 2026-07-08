# Air Passengers — Time Series Analysis: Conclusion

Trend: Passenger volume shows a strong, steady upward trend across all 12 years (1949-1960),
with the final-year average roughly 276% higher than the first-year average — driven by
the post-war growth of commercial air travel.

Seasonality: Clear annual seasonality is present, peaking around month 7
(summer travel season) and dipping around month 11 (winter low season). The
seasonal amplitude grows over time, which is why a multiplicative decomposition model fits
better than an additive one.

Cycles: No distinct multi-year business cycle is visible beyond the dominant trend and
seasonal pattern — the growth is largely monotonic rather than cyclical.

Stationarity: Raw series ADF statistic = 0.815, p-value = 0.9919
(non-stationary, as expected given the strong trend).
After first-differencing, ADF statistic = -2.829, p-value = 0.0542
(still non-stationary), confirming that removing the
trend is necessary before applying classical forecasting models.

Potential research questions: (1) Can the multiplicative seasonal pattern be used to forecast
short-term capacity planning for airlines? (2) How would an external shock (e.g. fuel price
spike, pandemic) alter the otherwise stable growth trend seen here?
