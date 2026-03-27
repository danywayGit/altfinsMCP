# Feature 02 - Latest Analytics Datapoint

## Prompt used

Get the latest RSI14 history datapoint for BTC.

## Tool invocation

`mcp_altfins-mcp-s_analytics_getAllLatestHistoryData(symbol="BTC", analyticsType="RSI14", timeInterval="DAILY")`

## Output received

```json
[
  {
    "symbol": "BTC",
    "time": 1774483200.0,
    "value": "46.1188517045909927",
    "nonNumericalValue": null
  }
]
```
