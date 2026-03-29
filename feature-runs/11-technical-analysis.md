# Feature 11 - Technical Analysis Data

## Prompt used

Get technical analysis data for ADA on the 4h timeframe.

## Tool invocation

`technicalAnalysis_getTechnicalAnalysisData(symbol="ADA")`

## Output received

```json
[
  {
    "symbol": "ADA",
    "friendlyName": "Cardano",
    "updatedDate": 1774522594.0,
    "nearTermOutlook": "Neutral",
    "patternType": "Sideways Channel",
    "patternStage": "Emerging",
    "description": "Trade setup and pattern details returned (HTML formatted).",
    "imgChartUrl": "https://cdn2.altfins.com/cdn-cgi/image/format=auto/img/curated_chart/2c9ac7db-a281-4c30-b7b8-bda2e0fe0f0f",
    "imgChartUrlDark": "https://cdn2.altfins.com/cdn-cgi/image/format=auto/img/curated_chart/52818827-093c-4ba7-8f40-cd0ea3628979",
    "logoUrl": "https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png"
  }
]
```

Note: output includes a long HTML `description` field; this file stores a concise excerpt.
