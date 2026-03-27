# Feature 06 - Crypto Calendar Events

## Prompt used

Show crypto calendar events coming in the next 7 days.

## Tool invocation

`mcp_altfins-mcp-s_getCryptoCalendarEvents(eventFrom="2026-03-27T00:00:00.000", eventTo="2026-04-03T00:00:00.000", size=10, sortField="dateEvent", sortDirection="ASC")`

## Output received

```json
[
  {
    "id": 88366,
    "title": "Goliath Mainnet",
    "coinMarketCalCategories": "RELEASE",
    "description": "The Onyx Goliath mainnet public version launches.",
    "dateEvent": 1774569600,
    "hot": false,
    "trending": true,
    "significant": false
  },
  {
    "id": 88367,
    "title": "Stable Summit IV",
    "coinMarketCalCategories": "CONFERENCE",
    "description": "Where stablecoin builders, issuers, institutions and regulators convene.",
    "dateEvent": 1774569600,
    "hot": false,
    "trending": false,
    "significant": false
  },
  {
    "id": 88408,
    "title": "Quantum Bitcoin Space",
    "coinMarketCalCategories": "DEV_UPDATE",
    "description": "Join panel members as they break down Core's quantum-resistant upgrade.",
    "dateEvent": 1774569600,
    "hot": false,
    "trending": false,
    "significant": false
  },
  {
    "id": 88409,
    "title": "Token Unlock",
    "coinMarketCalCategories": "TOKENOMICS",
    "description": "Walrus has an investor cliff unlock and start of vesting.",
    "dateEvent": 1774569600,
    "hot": false,
    "trending": true,
    "significant": false
  },
  {
    "id": 88421,
    "title": "Community AMA",
    "coinMarketCalCategories": "AMA",
    "description": "Founders host AMA on Discord about proposal and ecosystem plans.",
    "dateEvent": 1774569600,
    "hot": false,
    "trending": false,
    "significant": false
  }
]
```

Note: full objects include additional nested securityIdentifier fields; this file stores a concise excerpt.
