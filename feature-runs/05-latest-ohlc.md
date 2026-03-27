# Feature 05 - Latest OHLC Candle

## Prompt used

Get the latest 1h OHLC candle for SOL.

## Tool invocation

`mcp_altfins-mcp-s_ohlc_getLatestData(symbols="SOL", timeInterval="HOURLY")`

## Output received

```json
[
  {
    "symbol": "SOL",
    "time": 1774584599.999,
    "open": "86.41673090182873",
    "high": "86.41673090182873",
    "low": "85.70514541274257",
    "close": "85.76811391210448",
    "volume": "276738.331546115"
  }
]
```
