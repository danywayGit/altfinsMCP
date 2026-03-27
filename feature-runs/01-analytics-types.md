# Feature 01 - Analytics Types Discovery

## Prompt used

Show all analytics types available from altFINS so I can pick one for historical analysis.

## Tool invocation

`mcp_altfins-mcp-s_analytics_getAnalyticsTypes()`

## Output received

```json
[
  {
    "id": "PERFORMANCE",
    "friendlyName": "EAnalyticsTypeData_PERFORMANCE.TXT"
  },
  {
    "id": "MARKET_CAP",
    "friendlyName": "EAnalyticsTypeData_MARKET_CAP.TXT"
  },
  {
    "id": "CMC_RANK",
    "friendlyName": "EAnalyticsTypeData_CMC_RANK.TXT"
  },
  {
    "id": "CIRCULATING_SUPPLY",
    "friendlyName": "EAnalyticsTypeData_CIRCULATING_SUPPLY.TXT"
  },
  {
    "id": "HIGH",
    "friendlyName": "EAnalyticsTypeData_HIGH.TXT"
  },
  {
    "id": "LOW",
    "friendlyName": "EAnalyticsTypeData_LOW.TXT"
  },
  {
    "id": "PRICE_CHANGE_1D",
    "friendlyName": "EAnalyticsTypeData_PRICE_CHANGE_1D.TXT"
  },
  {
    "id": "PRICE_CHANGE_1W",
    "friendlyName": "EAnalyticsTypeData_PRICE_CHANGE_1W.TXT"
  },
  {
    "id": "PRICE_CHANGE_1M",
    "friendlyName": "EAnalyticsTypeData_PRICE_CHANGE_1M.TXT"
  },
  {
    "id": "PRICE_CHANGE_3M",
    "friendlyName": "EAnalyticsTypeData_PRICE_CHANGE_3M.TXT"
  }
]
```

Note: output is a large list; this file stores an excerpt of the first entries.
