# ChatGPT: Kraken API trading fees and bot profitability calculations

- **Date:** 2026-02-28
- **Category:** Trading
- **Messages:** 2

---

## Human

I need you to research on the internet kraken fees, in particular api crypto fees and formulas people use to calculate them, then, especially for bot style trading purposes

---

## ChatGPT

The user wants me to research Kraken's API crypto trading fees, particularly how they're structured and what formulas people use to calculate them for bot trading purposes.
```
This block is not supported on your current device yet.
```

Let me get the specific fee schedule tiers and then search for bot-specific fee calculation formulas.
```
This block is not supported on your current device yet.
```

Now let me get the actual fee schedule with exact tiers, and search for bot-specific fee calculation formulas.
```
This block is not supported on your current device yet.
```

Let me try the support article for the fee schedule.
```
This block is not supported on your current device yet.
```

Now let me search for bot-specific fee calculation formulas and how to programmatically calculate/account for Kraken fees in trading bots.
```
This block is not supported on your current device yet.
```

Now let me search for the specific API endpoint to get your fee tier and how to programmatically calculate fees.
```
This block is not supported on your current device yet.
```

Now I have enough information. Let me compile a comprehensive response about Kraken API fees and bot trading formulas.Brock, here's a comprehensive breakdown of Kraken's API trading fees and the formulas you need for bot development.

---

## Kraken Spot Fee Schedule (API / Kraken Pro)

Fees are calculated as a percentage of the trade's quote currency volume by default. Certain pairs allow the fee to be calculated based on the trade's base currency, which can be specified when ordering using the Fee Currency option. API trades use the same maker/taker schedule as Kraken Pro — there's no extra charge for using the API itself.

**Spot Crypto Tiers:**

| 30-Day Volume (USD) | Maker | Taker |
|---|---|---|
| $0+ | 0.25% | 0.40% |
| $10,000+ | 0.20% | 0.35% |
| $50,000+ | 0.14% | 0.24% |
| $100,000+ | 0.12% | 0.22% |
| $250,000+ | 0.10% | 0.20% |
| $500,000+ | 0.08% | 0.18% |
| $1,000,000+ | 0.06% | 0.16% |
| $2,500,000+ | 0.04% | 0.14% |
| $5,000,000+ | 0.02% | 0.12% |
| $10,000,000+ | 0.00% | 0.10% |

Kraken Pro fees for makers go from 0.25% to as low as 0% at $10M+ volume, while taker fees range from 0.40% down to 0.10%.

**Futures Tiers** (separate volume calculation from spot):
Futures start at 0.02% maker / 0.05% taker and step down to 0.00% / 0.01% at the highest tiers.

**Key nuances:**
- Volume generated with Instant Buy does not count towards your 30-day volume incentives.
- Spot and futures volumes are tracked independently and don't cross-count.
- There's a maker fee incentive structure on select lower-liquidity spot pairs, where high-volume traders can actually earn maker rebates.
- Limit orders can also execute immediately, incurring a taker fee. Use the post-limit order option to ensure maker-only execution, or it gets cancelled.

---

## Core Fee Calculation Formulas for Bots

### 1. Basic Trade Fee

```python
# Default: fee calculated on QUOTE currency volume
fee = order_volume_in_quote * fee_rate

# Example: Buy 0.1 BTC at $50,000 (taker, lowest tier)
quote_volume = 0.1 * 50000  # = $5,000
fee = 5000 * 0.0040          # = $20.00
```

### 2. Round-Trip Cost (Buy + Sell)

This is the critical formula for bot profitability — every trade cycle has two fees:

```python
# Round-trip fee as percentage
round_trip_fee_pct = entry_fee_rate + exit_fee_rate

# If using all market orders (taker/taker) at base tier:
round_trip = 0.0040 + 0.0040  # = 0.80%

# If using all limit orders (maker/maker) at base tier:
round_trip = 0.0025 + 0.0025  # = 0.50%

# Mixed (limit entry, market exit stop-loss):
round_trip = 0.0025 + 0.0040  # = 0.65%
```

### 3. Breakeven Price Movement

Your trade must move this much just to cover fees before profit:

```python
# Minimum price movement to break even
breakeven_move_pct = round_trip_fee_pct / (1 - exit_fee_rate)

# At base tier, all taker:
breakeven = 0.008 / (1 - 0.004)  # ≈ 0.803%

# At base tier, all maker:
breakeven = 0.005 / (1 - 0.0025)  # ≈ 0.501%
```

### 4. Net Profit/Loss Calculation

```python
def calculate_net_pnl(entry_price, exit_price, volume_base, 
                       entry_fee_rate, exit_fee_rate):
    # Entry cost
    entry_quote = volume_base * entry_price
    entry_fee = entry_quote * entry_fee_rate
    total_entry_cost = entry_quote + entry_fee  # for a buy
    
    # Exit proceeds  
    exit_quote = volume_base * exit_price
    exit_fee = exit_quote * exit_fee_rate
    total_exit_proceeds = exit_quote - exit_fee  # for a sell
    
    net_pnl = total_exit_proceeds - total_entry_cost
    net_pnl_pct = (net_pnl / total_entry_cost) * 100
    
    return net_pnl, net_pnl_pct
```

### 5. Fee-Adjusted Position Sizing

```python
def max_position_with_fees(available_balance, price, fee_rate):
    """How much base currency you can actually buy 
       after accounting for the fee"""
    max_base = available_balance / (price * (1 + fee_rate))
    return max_base

# Example: $10,000 balance, BTC at $50,000, taker fee 0.40%
max_btc = 10000 / (50000 * 1.004)  # = 0.19920 BTC (not 0.20000)
```

### 6. Effective Spread + Fee Cost

For scalping bots, the real cost includes the bid-ask spread:

```python
def total_execution_cost(bid, ask, fee_rate_entry, fee_rate_exit):
    spread_pct = (ask - bid) / ((ask + bid) / 2)
    total_cost = spread_pct + fee_rate_entry + fee_rate_exit
    return total_cost

# If BTC bid=49,990 ask=50,010, taker/taker base tier:
# spread = ~0.04%, total = 0.04% + 0.40% + 0.40% = 0.84%
```

---

## Querying Your Fees via API

Use the `GetTradeVolume` endpoint to programmatically get your current fee tier:

```python
import krakenex

k = krakenex.API()
k.load_key('kraken.key')

# Get your current fee tier for a specific pair
response = k.query_private('TradeVolume', {'pair': 'XXBTZUSD'})

# Returns:
# - currency: fee volume currency
# - volume: current 30-day volume
# - fees: {pair: {fee, minfee, maxfee, nextfee, nextvolume, tiervolume}}
# - fees_maker: same structure for maker fees

current_taker_fee = float(response['result']['fees']['XXBTZUSD']['fee'])
current_maker_fee = float(response['result']['fees_maker']['XXBTZUSD']['fee'])
```

The GetTradeVolume endpoint returns 30-day USD trading volume and resulting fee schedule for any asset pair provided. If an asset pair is on a maker/taker schedule, the taker side is given in `fees` and maker side in `fees_maker`.

---

## Bot-Specific Optimization Tips

**Use post-only limit orders** — This is the single biggest lever. At base tier, switching from taker to maker saves you 0.15% per trade (0.30% round-trip). On $100K monthly volume that's $300/month saved. The `oflags=post` parameter in the AddOrder API call ensures your limit order gets cancelled rather than filling as a taker.

**Fee currency option** — Certain pairs allow the fee to be calculated based on the trade's base currency, which can be specified when ordering using the Fee Currency option. This can matter for your accounting if you're tracking P&L in a specific denomination.

**Volume tier awareness** — Build your bot to query `GetTradeVolume` periodically and dynamically adjust strategy thresholds as your fee tier improves during the month. At $50K volume you drop to 0.14%/0.24%, which meaningfully changes your breakeven calculations.

**KFEE credits** — If you have any Kraken fee credits, they're auto-applied. 1,000 KFEE = $10 in fees. Your bot should factor this into P&L tracking.

**Rate limits** — Kraken enforces rate limits to ensure system stability. The default limit is one call per second, with higher limits for certain endpoints. Build in proper throttling or you'll get temporarily blocked.

For your Mr. Wonderful crypto bot specifically, the key formula to wire in is that breakeven calculation — at the base tier with mixed maker/taker execution, you need roughly 0.65% price movement minimum before you're profitable on any given trade. That should be your minimum signal threshold.

---
