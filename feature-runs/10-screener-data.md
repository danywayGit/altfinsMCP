# Feature 10 - Screener Data

## Prompt used

Get screener data for top coins with bullish trend and volume above average.

## Tool invocation

`mcp_altfins-mcp-s_screener_getAltfinsScreenerData(timeInterval="DAILY", displayTypes=["LAST_PRICE","VOLUME","VOLUME_RELATIVE","SHORT_TERM_TREND"], signalFilters=[{"signalFilterType":"SHORT_TERM_TREND","signalFilterValue":"UP"}], analyticsComparisonsFilters=[{"analyticsComparisonsFilterType":"VOLUME_VS_VOLUME_AVG","analyticsComparisonsFilterValue":"ABOVE"}], size=10, sortField="MARKET_CAP", sortDirection="DESC")`

## Output received

```json
[
  {
    "symbol": "USDC",
    "name": "USDC",
    "lastPrice": "0.9998719247998825",
    "additionalData": {
      "VOLUME": "3,462,252,923.19",
      "VOLUME_RELATIVE": "1.069",
      "SHORT_TERM_TREND": "Strong Up (9/10)"
    }
  },
  {
    "symbol": "USDE",
    "name": "Ethena USDe",
    "lastPrice": "0.9997033024843409",
    "additionalData": {
      "VOLUME": "41,403,937.56",
      "VOLUME_RELATIVE": "0.92210236",
      "SHORT_TERM_TREND": "Up (8/10)"
    }
  },
  {
    "symbol": "DAI",
    "name": "Dai",
    "lastPrice": "0.999185",
    "additionalData": {
      "VOLUME": "16,351,940.96",
      "VOLUME_RELATIVE": "1.5073",
      "SHORT_TERM_TREND": "Up (8/10)"
    }
  },
  {
    "symbol": "M",
    "name": "MemeCore",
    "lastPrice": "2.1120652154209623",
    "additionalData": {
      "VOLUME": "2,735,820.55",
      "VOLUME_RELATIVE": "2.3606",
      "SHORT_TERM_TREND": "Strong Up (10/10)"
    }
  },
  {
    "symbol": "USDG",
    "name": "USDG",
    "lastPrice": "1.0",
    "additionalData": {
      "VOLUME": "3,035,765.97",
      "VOLUME_RELATIVE": "0.92691093",
      "SHORT_TERM_TREND": "Strong Up (10/10)"
    }
  }
]
```

Note: output contains many rows; this file stores an excerpt.
