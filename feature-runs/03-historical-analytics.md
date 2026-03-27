# Feature 03 - Historical Analytics

## Prompt used

Get SMA50 historical values for BTC over the last 90 days.

## Tool invocation

`mcp_altfins-mcp-s_analytics_getHistoryData(symbol="BTC", analyticsType="SMA50", timeInterval="DAILY", from="last 90 days", to="today", size=100, sortField="timestamp", sortDirection="ASC")`

## Output received

```json
[
  {
    "symbol": "BTC",
    "time": 1766880000,
    "value": "90860.3130799090744",
    "nonNumericalValue": null
  },
  {
    "symbol": "BTC",
    "time": 1766966400,
    "value": "90510.1578130421951",
    "nonNumericalValue": null
  },
  {
    "symbol": "BTC",
    "time": 1767052800,
    "value": "90159.5409825083894",
    "nonNumericalValue": null
  },
  {
    "symbol": "BTC",
    "time": 1767139200,
    "value": "89850.7226294148344",
    "nonNumericalValue": null
  },
  {
    "symbol": "BTC",
    "time": 1767225600,
    "value": "89593.9508597636244",
    "nonNumericalValue": null
  },
  {
    "symbol": "BTC",
    "time": 1767312000,
    "value": "89399.9834795606955",
    "nonNumericalValue": null
  },
  {
    "symbol": "BTC",
    "time": 1767398400,
    "value": "89320.9437152234987",
    "nonNumericalValue": null
  },
  {
    "symbol": "BTC",
    "time": 1767484800,
    "value": "89239.9411407559639",
    "nonNumericalValue": null
  },
  {
    "symbol": "BTC",
    "time": 1767571200,
    "value": "89232.0754908776555",
    "nonNumericalValue": null
  },
  {
    "symbol": "BTC",
    "time": 1767657600,
    "value": "89262.8310282343005",
    "nonNumericalValue": null
  }
]
```

Note: output is a long time series; this file stores an excerpt.
