# Feature 08 - News Messages

## Prompt used

Get the latest 20 crypto news messages from all sources.

## Tool invocation

`mcp_altfins-mcp-s_news_getCryptoNewsMessages(from="last 7 days", size=20, sortField="timestamp", sortDirection="DESC")`

## Output received

```json
[
  {
    "id": 6003738,
    "assetSymbols": "BTC",
    "title": "Bitcoin ETF Inflows Rebound Despite Market Volatility Spike",
    "url": "https://coincu.com/markets/bitcoin-etf-inflows-rebound-market-volatility-2/",
    "newsSource": { "id": 47, "name": "CoinCu News" }
  },
  {
    "id": 6003730,
    "assetSymbols": "BTC, ETH, USDC",
    "title": "Sticker Mule Embraces Crypto: A Strategic Leap into Cryptocurrency Payments for Global Commerce",
    "url": "https://bitcoinworld.co.in/sticker-mule-cryptocurrency-payments-adoption/",
    "newsSource": { "id": 77, "name": "Bitcoin World" }
  },
  {
    "id": 6003709,
    "assetSymbols": "AAVE, UNI, DAO",
    "title": "Aave Will Win: Bold Framework Proposes 100% Revenue Shift to Supercharge DAO Treasury",
    "url": "https://bitcoinworld.co.in/aave-will-win-revenue-dao-treasury/",
    "newsSource": { "id": 77, "name": "Bitcoin World" }
  },
  {
    "id": 6003706,
    "assetSymbols": "ETH",
    "title": "Ethereum Hegota Upgrade Drops Framework Transactions Over Complexity Concerns",
    "url": "https://coincu.com/ethereum/ethereum-hegota-upgrade-framework-transactions-excluded-complexity/",
    "newsSource": { "id": 47, "name": "CoinCu News" }
  },
  {
    "id": 6003684,
    "assetSymbols": "BTC, ETH",
    "title": "Ethereum Price Drops Near $2,020, Downside Pressure Continues to Build",
    "url": "https://www.newsbtc.com/analysis/eth/ethereum-price-drops-near-2020/",
    "newsSource": { "id": 18, "name": "NewsBTC" }
  }
]
```

Note: output includes 20 articles with additional fields (`messageId`, `timestamp`, `content`); this file stores an excerpt.
