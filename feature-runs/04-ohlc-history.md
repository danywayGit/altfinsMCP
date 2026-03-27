# Feature 04 - OHLC History

## Prompt used

Get daily OHLC history for ETH for the last 6 months.

## Tool invocation

`mcp_altfins-mcp-s_ohlc_getHistoryData(symbol="ETH", timeInterval="DAILY", from="2025-09-27T00:00:00.000", to="2026-03-27T00:00:00.000", size=200, sortField="time", sortDirection="ASC")`

## Output received

```json
[
  {
    "symbol": "ETH",
    "time": 1758931200,
    "open": "4032.62627791581407216",
    "high": "4039.269250537696496836",
    "low": "3973.407536598525348892",
    "close": "4018.85107805288497211",
    "volume": "1039943.87795822603966027"
  },
  {
    "symbol": "ETH",
    "time": 1759017600,
    "open": "4018.899402236347527638",
    "high": "4145.227582704225187637",
    "low": "3966.303651444325937201",
    "close": "4142.694096841869975692",
    "volume": "1406451.812832209312030498"
  },
  {
    "symbol": "ETH",
    "time": 1759104000,
    "open": "4142.858632907443021264",
    "high": "4236.57030399730001503",
    "low": "4082.834526465803426677",
    "close": "4215.664375956524873055",
    "volume": "2014787.412725008992807941"
  },
  {
    "symbol": "ETH",
    "time": 1759190400,
    "open": "4215.643407069907876082",
    "high": "4245.46229026290872199",
    "low": "4092.691327671653364779",
    "close": "4145.388858707299029207",
    "volume": "2117626.027816437032976105"
  },
  {
    "symbol": "ETH",
    "time": 1759276800,
    "open": "4145.424162217792665199",
    "high": "4356.105340683931677054",
    "low": "4123.535790531034987598",
    "close": "4350.348446756658173467",
    "volume": "2522452.193444825192192548"
  }
]
```

Note: output contains many candles; this file stores an excerpt.
