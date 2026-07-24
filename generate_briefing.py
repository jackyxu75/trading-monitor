import json
from datetime import datetime, date, timezone

# ── MACRO SUMMARY ──────────────────────────────────────────────────────────────
macro_summary = {
    'market_regime': 'BULL',
    'vix': 16.90,
    'treasury_10yr': 4.45,
    'dxy': 101.21,
    'copper_trend': 'RISING',
    'spy_5d_return': 0.008,
    'spy_20d_return': 0.035,
    'spy_price': 745.40,
    'sp500': 7482.71,
    'cross_strait_risk': 'MEDIUM-HIGH',
    'macro_themes': [
        "Fed held rates at 3.5-3.75% in June 2026 (Warsh era begins); dot plot FLIPPED to project a hike — 9/18 members see a hike in Oct 2026. Market now pricing 50bps higher by year-end. Rising-rate risk is REAL and the biggest macro headwind for high-multiple growth stocks.",
        "Inflation sticky at PCE 3.6% / CPI 4.2% (May). Higher-for-longer confirmed. 10yr yield at 4.45% (peaked 4.58% recent high) — DCF headwind for NVDA, PLTR, ARM. Favors value/cash-flow names.",
        "US-China chip export controls: H200 allowed under 50% volume cap + 25% tariff; Blackwell (B200/B300) remains restricted. NVDA China revenue capped but Blackwell demand from non-China markets overwhelms. Geopolitical risk is permanent structural headwind.",
        "Four hyperscalers (AMZN, GOOGL, MSFT, META) deploying $725B in AI-related capex in 2026 — up 77% YoY from $410B in 2025. Capital is flowing: AI infra buildout is real, sustained, and not slowing. Every infrastructure layer benefits.",
        "META launched 'Meta Compute' (July 1) — selling excess AI compute capacity to enterprise customers, directly challenging AWS/Azure/GCP. Stock +10% on announcement. Structural revenue stream addition and cost amortization catalyst. CoreWeave -12% same day (read-through: pure-play GPU rental margins compress).",
    ],
    'emerging_tech_themes': [
        "NVDA GB300 (Blackwell Ultra) shipments tracking +129% YoY in 2026 — Morgan Stanley projects 60k rack units vs 28k in 2025. GB300 on-demand rates firm at $9.16/hr as of July 2026. Vera Rubin (next-gen) in full production; first customer shipments H2 2026 per Jensen at GTC Taipei June 1.",
        "TSMC CoWoS capacity ramping to 127k WPM by end-2026. NVDA holds 60% (~595k wafers). N2 node sold out through year — 5 fab phases in first 12 months. Unprecedented ramp. Arizona advanced packaging facility accelerating per CNBC April 2026.",
        "HBM4 CRITICAL UPDATE: ALL THREE suppliers (SK Hynix 60-70%, Samsung 25-30%, Micron ~10%) now certified for NVDA Vera Rubin per Jensen Huang June 5. Earlier sole-source thesis for MU is DEAD. SK Hynix is the dominant HBM4 winner. MU is the smallest share holder.",
        "Inference overtakes training: inference = 2/3 of AI compute in 2026 (up from 50% in 2025). $50B inference chip market emerging. Benefits NVDA (still dominant), opens gap for AMD EPYC, MRVL custom ASIC, QCOM edge AI. XPU/ASIC segment growing 22% vs GPU 19%.",
        "AI networking 1.6Tbps inflection: ANET launched 7060XE7 switches for rack-scale AI fabric — Meta, Microsoft, Oracle, AMD, Broadcom as early partners. BlackRock named ANET one of its top 30 AI stocks July 2026. 800G → 1.6T transition creating upgrade supercycle.",
    ],
    'govt_catalysts': [
        {'company': 'PLTR', 'type': 'DoD/Project Maven', 'amount': '$10B+ Army data contracts + Maven permanent program', 'status': 'CONFIRMED', 'priced_in': 'PARTIAL', 'upside': 'Maven becoming permanent = recurring federal budget line; additional IC and NATO expansion not priced', 'risk': 'Contract protest from competitors; geopolitical sensitivity'},
        {'company': 'MSFT/AMZN/NVDA/ORCL', 'type': 'Pentagon AI Classified', 'amount': 'Classified (8-firm deal)', 'status': 'CONFIRMED', 'priced_in': 'PARTIAL', 'upside': 'DoD AI spending expanding aggressively; classified workloads = premium pricing, sticky revenue', 'risk': 'Audit risk; classified program termination'},
        {'company': 'TSM', 'type': 'CHIPS Act + DOC', 'amount': '$6.6B+ (final award)', 'status': 'CONFIRMED', 'priced_in': 'YES', 'upside': 'Arizona N2 ramp timing pull-forward (2028 → 2027 possible)', 'risk': 'Geopolitical escalation triggers export restriction on Arizona-made chips'},
        {'company': 'CEG/VST', 'type': 'DOE Nuclear + Policy', 'amount': 'Policy support (no direct grant)', 'status': 'CONFIRMED', 'priced_in': 'PARTIAL', 'upside': 'Federal nuclear loan guarantees being expanded; SMR permitting accelerated', 'risk': 'Grid interconnection bottlenecks; PUC regulatory risk'},
        {'company': 'NVDA/MSFT/AMZN', 'type': 'Stargate AI Infrastructure', 'amount': '$500B committed', 'status': 'CONFIRMED', 'priced_in': 'PARTIAL', 'upside': 'Phase 2 contract awards not yet announced; TX → multi-state expansion', 'risk': 'Government sequestration; competing with sovereign AI initiatives'},
    ],
    'taiwan_signals': [
        "TSMC CoWoS SOLD OUT through 2026-2027; N2 node booked solid — no capacity available for new customers. NVDA and AMD combined hold >70% of all CoWoS allocation.",
        "Cross-strait risk: CFR assigns 50%+ probability to a Taiwan Strait crisis in 2026. PLA building toward 2027 invasion readiness milestone. Gray-zone coercion ongoing (CCG vessels in Dongsha waters). MEDIUM-HIGH risk — discount ~15% on TSM valuation vs equivalent US foundry.",
        "TSMC Arizona accelerating: advanced packaging (CoWoS) facility added to Arizona plan per CNBC April 2026. N2 Arizona expected 2028 (possibly 2027). Reduces but does not eliminate cross-strait supply chain risk.",
        "Taiwan produces 92% of world's most advanced chips — any conflict scenario means global semiconductor supply shock. Single largest concentration risk in institutional portfolios.",
        "TSMC VP Liu bought 2,000 shares open-market May 2026 at $69.98. Small but notable — insider comfort at sub-$70. Stock now at $79. Insider paid up; thesis intact.",
    ],
}

# ── ROTATION SUMMARY ────────────────────────────────────────────────────────────
rotation_summary = {
    'sector_rotation_today': 'AI_NETWORKING → INFRASTRUCTURE → ENERGY',
    'rotation_favored': ['ANET', 'AVGO', 'META', 'MSFT', 'AMZN', 'MRVL', 'CRDO', 'CEG', 'VST', 'GEV', 'VRT', 'AMD'],
    'rotation_disfavored': ['MU', 'SMCI', 'INTC'],
    'rotation_rationale': 'AI hardware semis (SOXX +89% YTD) had the first-half run. Institutional rotation is broadening: networking (ANET +8.76% today on new 1.6T switches), custom silicon/ASIC (AVGO +4.83% on Apple deal extension), cloud platforms (META +10% last week on Meta Compute), and nuclear power/energy infrastructure. Memory and commodity semis are the clear DISFAVORED trade — MU insiders selling at 14-year pace confirms distribution.',
}

# ── ETF FLOWS ───────────────────────────────────────────────────────────────────
etf_flow_dict = {
    'SOXX': 'INFLOW',     # +89% YTD; 5d -$518M (slight profit taking) but 1mo +$2.9B, 3mo +$5.9B
    'SMH':  'INFLOW',     # +64% YTD; consistent inflow
    'IGV':  'OUTFLOW',    # -1.75% recent; software lagging hardware
    'XLK':  'NEUTRAL',    # +1.24% today; broad tech mixed
    'XLY':  'NEUTRAL',
    'XLF':  'NEUTRAL',
    'XLV':  'NEUTRAL',
    'XLE':  'INFLOW',     # Nuclear/energy rotation underway
    'XLI':  'INFLOW',     # Infrastructure / grid buildout
    'XLC':  'NEUTRAL',
    'XLRE': 'NEUTRAL',
    'XLU':  'NEUTRAL',
    'XLP':  'NEUTRAL',
    'ARKK': 'OUTFLOW',    # Speculative risk-off at margins
}

# ── ALL CANDIDATES ──────────────────────────────────────────────────────────────
CORE_STOCKS = ['TSM','NVDA','ANET','VRT','MU','AVGO','PLTR','VST','CEG','ORCL','AMZN','META','MSFT']

all_candidates = [

  {
    'symbol': 'ANET', 'company': 'Arista Networks',
    'is_core': True, 'filter_status': 'PASSED',
    'ai_category': 'Optical & Networking',
    'close': 181.05, 'rs_vs_spy_20d': 0.087, 'pct_from_52w_high': -0.02, 'volume_ratio': 3.1,
    'quant_score': 92,
    'valuation': {'forwardPE': 45, 'peg': 2.1, 'vs_peers': 'FAIR'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'No material open-market buys or sells — executives hold via RSU vesting. No red flags.',
    'short_interest_pct': 0.018, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-07-29', 'earnings_days_away': 20, 'earnings_risk': 'EARNINGS_NEAR',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': 'Call sweep volume 3x average post-KeyBanc upgrade; $200 strike Aug calls bought aggressively.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'KeyBanc PT $200 (June 18); Morgan Stanley PT $190; BofA PT $200. Strong Buy consensus 18/18 analysts.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'BULLISH',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'POSITIVE', 'taiwan_exposure': 'NONE',
    'govt_catalyst': 'NONE',
    'pricing_power': 'PRICING_LEADER',
    'pricing_power_detail': 'EOS (Extensible Operating System) creates deep CLI/automation lock-in across AI hyperscalers — 90%+ customer retention. New 7060XE7 1.6Tbps switches co-developed with Meta, Microsoft, Oracle, AMD, Broadcom; no viable alternative at this bandwidth/latency spec. Gross margins ~62%, expanding.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'BlackRock named ANET one of top 30 most important AI stocks (July 2026). Institutional ownership growing — Vanguard, BlackRock, T. Rowe Price all increased Q1 2026.',
    'buy_zone': '$165-$182',
    'price_target': '$215',
    'stop_loss': '$148',
    'thesis_hold_conditions': 'Hold as long as: AI networking capex from hyperscalers growing; ANET maintains >85% market share in AI cluster front-end networking; gross margins above 60%; no viable EOS-compatible competitor emerges',
    'thesis_break_triggers': 'EXIT if: Cisco or Juniper ships a competitive AI fabric OS with >10% hyperscaler design wins OR ANET loses a top-3 hyperscaler customer to a competitor OR gross margins decline below 58% for 2 consecutive quarters',
    'key_catalysts': 'Q2 earnings July 29 (catalyst), 1.6T switch ramp, Meta/Microsoft AI fabric expansion, front-end refresh supercycle',
    'key_risks': 'Premium multiple (45x PE) at risk if AI capex pauses; earnings miss July 29 = immediate -10% risk; Cisco competitive response',
    'analyst_note': 'ANET is the clearest institutional buy on the board today. The +8.76% move is not momentum speculation — it is BlackRock stamp of approval, confirmed by three simultaneous analyst upgrades to $200 and launch of 1.6T switches co-engineered with every major AI customer. Revenue growth near 26% with $1.6B FCF, zero debt, 62% gross margins, and a software-defined network OS that hyperscalers have zero incentive to rip out. Q2 earnings in 20 days creates a binary event but positioning is long-biased. The networking refresh cycle from 400G → 800G → 1.6T is a multi-year revenue tailwind that the market keeps underestimating. ANET is the infrastructure layer nobody talks about as much as NVDA but it touches every AI rack.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'AMZN', 'company': 'Amazon.com',
    'is_core': True, 'filter_status': 'PASSED',
    'ai_category': 'Cloud',
    'close': 264.03, 'rs_vs_spy_20d': 0.031, 'pct_from_52w_high': -0.04, 'volume_ratio': 1.2,
    'quant_score': 78,
    'valuation': {'forwardPE': 38, 'peg': 1.7, 'vs_peers': 'FAIR'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'Routine 10b5-1 sales by Jassy and Bezos trusts. No cluster buying or unusual selling patterns.',
    'short_interest_pct': 0.007, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-07-30', 'earnings_days_away': 21, 'earnings_risk': 'EARNINGS_NEAR',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': 'Large call sweep into Q2 earnings; $280 Aug calls bought.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Multiple banks PT $310+. AWS AI revenue accelerating drives re-rating.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'BULLISH',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'NEUTRAL', 'taiwan_exposure': 'LOW',
    'govt_catalyst': 'CONFIRMED',
    'pricing_power': 'PRICING_LEADER',
    'pricing_power_detail': 'AWS holds ~31% cloud market share — enterprises in AWS ecosystem face substantial switching costs (re-architect + retrain staff). Trainium/Inferentia custom silicon reduces NVDA dependency and expands margins. Pentagon JWCC + IC classified contracts = recurring high-margin government revenue.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Tiger Global holds AMZN as top-5 position Q1 2026. Average institutional allocation 4.54% across major funds.',
    'buy_zone': '$250-$265',
    'price_target': '$330',
    'stop_loss': '$215',
    'thesis_hold_conditions': 'Hold as long as: AWS revenue growth >20% YoY; AI capex from hyperscalers remains elevated; Trainium/Inferentia gaining meaningful share vs NVDA GPUs; operating margins expanding',
    'thesis_break_triggers': 'EXIT if: AWS revenue growth decelerates below 15% for 2 consecutive quarters OR Meta Compute captures >10% of AMZN cloud customers OR antitrust breakup of AWS accelerates materially',
    'key_catalysts': 'Q2 earnings July 30, Trainium chip ramp, Stargate Phase 2 contracts, Project Kuiper broadband',
    'key_risks': 'Meta Compute enters GPU rental market (structural margin pressure), rising yields compress FCF multiple, antitrust',
    'analyst_note': 'AMZN trades at a sum-of-parts discount — retail + advertising + AWS + Trainium are each mispriced individually. AWS at 31% cloud share with Trainium displacing NVDA on internal workloads = structural margin expansion story. Pentagon classified AI contracts (8-firm deal announced May 2026) lock in government revenue for 5+ years. The key risk is META Compute entering the GPU rental market, which compresses CoreWeave/hyperscaler on-demand pricing — but AMZN enterprise lock-in is far stickier than spot GPU rentals. Q2 earnings in 21 days = near-term binary event; positioning is aggressively bullish.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'NVDA', 'company': 'NVIDIA Corporation',
    'is_core': True, 'filter_status': 'PASSED',
    'ai_category': 'Chips',
    'close': 204.12, 'rs_vs_spy_20d': 0.042, 'pct_from_52w_high': -0.01, 'volume_ratio': 1.4,
    'quant_score': 84,
    'valuation': {'forwardPE': 42, 'peg': 2.3, 'vs_peers': 'FAIR'},
    'insider_activity': 'BEARISH_INSIDER',
    'insider_detail': '⚠️ RED FLAG: Insiders net sold $249.2M trailing 6 months. CEO Jensen Huang trust sold 885,000 shares at weighted avg $209-210 on June 18, 2026 — just above current price. Pattern is consistent 10b5-1 but scale is significant. No insider has bought open-market in 2026.',
    'short_interest_pct': 0.011, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-08-20', 'earnings_days_away': 42, 'earnings_risk': 'LOW',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': 'Consistent $220+ call buying; bullish options skew despite insider selling.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Multiple banks PT $250-280. Goldman, Morgan Stanley bullish on GB300 cycle.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'BULLISH',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'POSITIVE', 'taiwan_exposure': 'HIGH',
    'govt_catalyst': 'CONFIRMED',
    'pricing_power': 'PRICING_LEADER',
    'pricing_power_detail': 'CUDA software ecosystem = deepest moat in tech. NVDA controls GB300/GB300 NVL72 allocation — hyperscalers pay whatever asked. CoWoS 60% allocation locked through 2027. Vera Rubin in production per Jensen June 2026. No viable GPU alternative at frontier AI scale.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Largest institutional add in Q1 2026: +$187.2B across 37 major filers. Tiger Global NVDA top-3 position. Average allocation 5.75% — highest of any stock.',
    'buy_zone': '$185-$205',
    'price_target': '$265',
    'stop_loss': '$160',
    'thesis_hold_conditions': 'Hold as long as: GB300/Vera Rubin demand from hyperscalers growing; CUDA maintains >80% AI developer mindshare; gross margins above 72%; no viable competitive GPU at frontier AI scale',
    'thesis_break_triggers': 'EXIT if: AMD MI400 or Google TPUv6 captures >15% of new hyperscaler GPU orders OR Blackwell/Rubin manufacturing yields disappoint causing multi-quarter delay OR export control expansion cuts total addressable market >25%',
    'key_catalysts': 'Vera Rubin H2 2026 ramp, GB300 shipment doubling, Stargate Phase 2, $500B AI infrastructure cycle',
    'key_risks': '⚠️ BEARISH_INSIDER ALERT: CEO sold $40M+ at $209-210 — stock NOW trading below insider sale prices. Inference shift reduces training GPU premium. Export controls cap China revenue. 42x PE = significant compression risk if AI capex pauses.',
    'analyst_note': 'NVDA remains the singular must-own AI infrastructure stock with the deepest software moat in history. GB300 shipments +129% YoY, Vera Rubin in full production, and $187B in institutional accumulation are undeniable fundamentals. BUT: CEO insider sale of 885k shares at $209-210 — stock now at $204 — is a technical warning. Insiders have net sold $249M in 6 months with zero open-market buys. This does NOT break the thesis (CUDA moat is intact) but it suggests the $200-210 zone is where management sees fair value today. Conviction investors should hold — but new buyers should size appropriately and wait for a pullback to $185-190 for optimal entry. The inference shift (now 2/3 of all AI compute) still favors NVDA overwhelmingly in the near term.',
    'sector_rotation_impact': 'NEUTRAL',
  },

  {
    'symbol': 'MSFT', 'company': 'Microsoft Corporation',
    'is_core': True, 'filter_status': 'PASSED',
    'ai_category': 'Cloud',
    'close': 421.87, 'rs_vs_spy_20d': 0.028, 'pct_from_52w_high': -0.03, 'volume_ratio': 1.1,
    'quant_score': 76,
    'valuation': {'forwardPE': 35, 'peg': 1.9, 'vs_peers': 'FAIR'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'Routine Satya Nadella 10b5-1 sales. No unusual activity.',
    'short_interest_pct': 0.006, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-07-29', 'earnings_days_away': 20, 'earnings_risk': 'EARNINGS_NEAR',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': '$440+ call buying ahead of Q4 FY26 earnings.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Multiple PT raises post-Azure AI acceleration; Strong Buy consensus.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'BULLISH',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'NEUTRAL', 'taiwan_exposure': 'LOW',
    'govt_catalyst': 'CONFIRMED',
    'pricing_power': 'PRICING_LEADER',
    'pricing_power_detail': 'Microsoft 365 + Azure enterprise lock-in is the deepest in enterprise software. Azure OpenAI = only approved GPT-4/o3 deployment for 95% of Fortune 500. Pentagon Azure Gov classified contracts (DoD Impact Level 6). Palantir AIP runs ON Azure. Every government AI dollar flows through Azure.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Universal institutional holding; consistent adds across Coatue, Tiger, Viking in Q1 2026.',
    'buy_zone': '$405-$425',
    'price_target': '$510',
    'stop_loss': '$355',
    'thesis_hold_conditions': 'Hold as long as: Azure revenue growth >25% YoY; Microsoft 365 Copilot ARPU expanding; Pentagon/government AI contracts sustained; OpenAI partnership exclusive',
    'thesis_break_triggers': 'EXIT if: Azure growth decelerates below 20% for 2 quarters OR antitrust forces OpenAI stake divestiture OR Meta Compute or AWS wins a key Microsoft enterprise vertical',
    'key_catalysts': 'Q4 FY26 earnings July 29, Copilot monetization, Azure OpenAI expansion, Palantir AIP on Azure scale',
    'key_risks': 'Premium multiple, Google Gemini competitive threat in enterprise, rising yields DCF headwind',
    'analyst_note': 'MSFT is the most defensible large-cap AI play. Azure has OpenAI exclusivity for enterprise, PLTR AIP runs on Azure Government, and the company collects a toll on every enterprise AI deployment regardless of which AI model wins. Copilot monetization is just beginning — $30/seat/month × 400M Office subscribers = $144B/yr addressable TAM at full penetration. Q4 FY26 earnings July 29 will either confirm the Azure AI inflection or create a buying opportunity. At $422 and 35x PE, this is the cheapest way to own AI infrastructure at scale.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'AVGO', 'company': 'Broadcom Inc.',
    'is_core': True, 'filter_status': 'PASSED',
    'ai_category': 'Chips',
    'close': 388.69, 'rs_vs_spy_20d': 0.051, 'pct_from_52w_high': -0.05, 'volume_ratio': 1.8,
    'quant_score': 86,
    'valuation': {'forwardPE': 38, 'peg': 1.8, 'vs_peers': 'FAIR'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'Routine Hock Tan 10b5-1 sales. No unusual activity.',
    'short_interest_pct': 0.014, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-09-03', 'earnings_days_away': 56, 'earnings_risk': 'LOW',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': '$420 call sweep post-Apple deal extension news.',
    'analyst_action': 'NEUTRAL', 'analyst_detail': 'Wells Fargo PT $430 (January). Last downgrade from Erste Group July 7 (minor). Strong Buy consensus held.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'BULLISH',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'POSITIVE', 'taiwan_exposure': 'MEDIUM',
    'govt_catalyst': 'NONE',
    'pricing_power': 'PRICING_LEADER',
    'pricing_power_detail': 'Sole designer of Google TPU, Apple custom silicon, AWS Trainium — three of the four largest AI chip programs in the world. Custom ASIC design is a decade-long relationship: hyperscalers do not switch ASIC partners. Apple extended chip deal to 2031 (July 2026). Q2 FY26 AI semiconductor revenue $10.8B — record. Target >$100B AI revenue by 2027.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Top institutional holding across Coatue, Fidelity, Vanguard. Consistent adds post-VMware integration.',
    'buy_zone': '$370-$392',
    'price_target': '$490',
    'stop_loss': '$315',
    'thesis_hold_conditions': 'Hold as long as: Custom ASIC design wins with Google/Apple/AWS intact; AI semiconductor revenue growing toward $100B target; VMware integration synergies materializing; gross margins above 70%',
    'thesis_break_triggers': 'EXIT if: Google or Apple brings ASIC design in-house fully OR NVDA develops a competitive custom ASIC design service OR AI semiconductor revenue misses by >20% for 2 quarters',
    'key_catalysts': 'Apple chip deal to 2031, Google TPU scale, AWS Trainium ramp, Q3 FY26 earnings Sept 3',
    'key_risks': 'Q2 earnings reaction (-12% on report) shows market expectations are high; AI revenue target >$100B may slip to 2028; VMware integration risk',
    'analyst_note': 'AVGO is the best-positioned custom silicon play. While NVDA owns the GPU market, AVGO designs the custom ASIC silicon for every major hyperscaler building away from NVDA. Google TPU, Apple Neural Engine, AWS Trainium — all AVGO. Apple deal extended to 2031 eliminates years of uncertainty. The Q2 earnings drop (-12%) created an entry point: $10.8B AI revenue in a single quarter with a clear path to $100B+ by 2027. At $389 and 38x forward, this is cheaper than NVDA for a more diversified AI chip exposure. Earnings not until September 3 — a 56-day clean window to accumulate.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'META', 'company': 'Meta Platforms',
    'is_core': True, 'filter_status': 'PASSED',
    'ai_category': 'Cloud',
    'close': 619.00, 'rs_vs_spy_20d': 0.095, 'pct_from_52w_high': -0.01, 'volume_ratio': 2.3,
    'quant_score': 90,
    'valuation': {'forwardPE': 30, 'peg': 1.4, 'vs_peers': 'CHEAP'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'Zuckerberg routine 10b5-1 sales. No unusual selling. Foundation sells are per pre-disclosed charity plan.',
    'short_interest_pct': 0.008, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-07-29', 'earnings_days_away': 20, 'earnings_risk': 'EARNINGS_NEAR',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': '$650 call sweep post-Meta Compute announcement. Heavy bullish positioning into Q2 earnings.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Multiple upgrades post-Meta Compute announcement (July 1). PT range $680-740.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'BULLISH',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'NEUTRAL', 'taiwan_exposure': 'LOW',
    'govt_catalyst': 'NONE',
    'pricing_power': 'PRICING_LEADER',
    'pricing_power_detail': 'Social media monopoly (3.3B DAU) + now Meta Compute cloud platform = dual pricing power. $125-145B capex in 2026 transforms META from AI consumer to AI PROVIDER. Excess compute monetization is pure margin — no additional CapEx needed, sunk cost now becomes revenue. Llama open-source strategy pulls developers into Meta ecosystem.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Tiger Global top-5 holding. Coatue active META position. D1 Capital, Lone Pine accumulating Q1 2026.',
    'buy_zone': '$590-$622',
    'price_target': '$740',
    'stop_loss': '$510',
    'thesis_hold_conditions': 'Hold as long as: Meta Compute monetization progressing; advertising revenue growing >15% YoY; AI capex generating returns (compute margin contribution visible by Q4 2026); Llama adoption accelerating',
    'thesis_break_triggers': 'EXIT if: Meta Compute launch delayed beyond Q1 2027 OR advertising revenue growth falls below 10% for 2 quarters OR EU regulatory action forces data separation at material cost',
    'key_catalysts': 'Meta Compute launch timeline, Q2 earnings July 29, nuclear PPA delivery starting late 2026, Llama enterprise licensing',
    'key_risks': 'Meta Compute is still rumored — official launch timeline unconfirmed. 6.6GW nuclear PPA by 2035 is long-dated. Regulatory risk in EU. Stock +10% already on news — execution must deliver.',
    'analyst_note': 'META is the most undervalued mega-cap AI play on the board. At 30x forward earnings with PEG 1.4, it trades at a 30% discount to NVDA and MSFT on valuation despite superior near-term earnings growth. The Meta Compute announcement (July 1) is transformational: $125-145B capex becomes a revenue-generating asset, not just a cost. META transitions from AI consumer to AI infrastructure provider — a category that commands 40-50x multiples, not 30x. Q2 earnings July 29 will be the first chance to see Meta Compute economics disclosed. 6.6GW nuclear deals with Vistra, Constellation, Oklo, TerraPower lock in power costs for 20 years. BUY on any weakness into earnings.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'MRVL', 'company': 'Marvell Technology',
    'is_core': False, 'filter_status': 'PASSED',
    'ai_category': 'Chips',
    'close': 98.50, 'rs_vs_spy_20d': 0.062, 'pct_from_52w_high': -0.08, 'volume_ratio': 1.5,
    'quant_score': 78,
    'valuation': {'forwardPE': 48, 'peg': 2.2, 'vs_peers': 'FAIR'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'Routine RSU vesting sales. No material open-market buys.',
    'short_interest_pct': 0.021, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-09-02', 'earnings_days_away': 55, 'earnings_risk': 'LOW',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': '$110 call sweep; inference rotation trade.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Inference shift narrative driving multiple PT raises. Custom ASIC winner thesis widely held.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'BULLISH',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'POSITIVE', 'taiwan_exposure': 'MEDIUM',
    'govt_catalyst': 'PENDING',
    'pricing_power': 'STRONG_POSITION',
    'pricing_power_detail': 'Amazon Trainium 2/3 and Google Axion CPU design wins locked multi-year. Inference ASICs are purpose-built — hyperscalers do not replace mid-cycle. MRVL has 3 confirmed top-tier hyperscaler ASIC programs with no announced competition for existing contracts.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Multiple top hedge funds added MRVL as inference-shift beneficiary Q1-Q2 2026.',
    'buy_zone': '$88-$100',
    'price_target': '$140',
    'stop_loss': '$76',
    'thesis_hold_conditions': 'Hold as long as: inference demand for custom ASIC growing; Amazon Trainium and Google Axion on track; PAM-4 optical DSP market share growing; revenue >25% YoY',
    'thesis_break_triggers': 'EXIT if: Amazon or Google brings ASIC design in-house OR NVDA launches a custom ASIC design service capturing >1 hyperscaler OR revenue growth decelerates below 20% for 2 consecutive quarters',
    'key_catalysts': 'Inference cycle acceleration, Amazon Trainium 3 design win disclosure, Google Cloud Next announcements',
    'key_risks': 'High valuation (48x), execution risk on 3nm ASIC yields, NVDA entering custom silicon business',
    'analyst_note': 'MRVL is the pure inference-cycle beneficiary. While NVDA dominates training, the shift to inference (now 2/3 of all AI compute) favors purpose-built ASICs over general-purpose GPUs on a cost-per-token basis. MRVL holds confirmed design wins at Amazon (Trainium 2/3), Google (Axion), and Microsoft. These are decade-long commitments — the customer writes software stack around the chip. The inference TAM is $50B and growing 35%+ annually. At $98 with earnings not until September, this is a clean 55-day accumulation window. The risk is valuation (48x) and a broader tech selloff.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'AMD', 'company': 'Advanced Micro Devices',
    'is_core': False, 'filter_status': 'PASSED',
    'ai_category': 'Chips',
    'close': 420.00, 'rs_vs_spy_20d': 0.055, 'pct_from_52w_high': -0.06, 'volume_ratio': 1.4,
    'quant_score': 82,
    'valuation': {'forwardPE': 40, 'peg': 1.9, 'vs_peers': 'FAIR'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'Lisa Su routine 10b5-1 sales. No unusual activity.',
    'short_interest_pct': 0.024, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-07-29', 'earnings_days_away': 20, 'earnings_risk': 'EARNINGS_NEAR',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': 'Goldman PT raise to $640 catalyzed $470 call buying on July 5.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Goldman Sachs PT raised $450 → $640 on July 5, 2026. DC revenue +57% YoY in Q1. Strong Buy consensus.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'BULLISH',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'POSITIVE', 'taiwan_exposure': 'HIGH',
    'govt_catalyst': 'NONE',
    'pricing_power': 'STRONG_POSITION',
    'pricing_power_detail': 'EPYC server CPU near-monopoly in hyperscaler and enterprise data centers. MI300X/MI400 GPU gaining traction as NVDA alternative at 60-70% of cost. Inference shift specifically benefits AMD: EPYC CPUs run inference workloads efficiently. Q1 DC revenue $5.8B +57% YoY = thesis validating quarterly.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Coatue, D1 Capital, and Dragoneer adding AMD as inference beneficiary trade Q1-Q2 2026.',
    'buy_zone': '$400-$425',
    'price_target': '$560',
    'stop_loss': '$348',
    'thesis_hold_conditions': 'Hold as long as: EPYC CPU wins in new data center builds; MI-series GPU gaining share; inference workloads on CPU remaining viable; DC revenue growing >40% YoY',
    'thesis_break_triggers': 'EXIT if: EPYC market share reversal (Intel comes back) OR NVDA launches competitive CPU OR DC revenue growth falls below 30% for 2 consecutive quarters',
    'key_catalysts': 'Q2 earnings July 29, MI400 ramp, EPYC data center wins, Goldman PT $640 creates near-term momentum',
    'key_risks': 'NVDA moat in training remains impenetrable; MI-series software ecosystem lags CUDA; earnings July 29 near-term binary',
    'analyst_note': 'AMD is the best-value large-cap AI chip play today. Goldman Sachs effectively doubled their price target ($450→$640) — that is not a fine-tuning, that is a thesis change. Data Center revenue +57% to $5.8B in Q1 validates EPYC dominance. The inference shift is AMD\'s structural tailwind: EPYC CPUs handle inference workloads at a fraction of GPU cost, and the MI300X/MI400 GPU is 40% cheaper than NVDA equivalent with improving software. At $420 vs a Goldman PT of $640, AMD offers 52% upside with strong Q2 earnings catalyst in 20 days.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'VRT', 'company': 'Vertiv Holdings',
    'is_core': True, 'filter_status': 'PASSED',
    'ai_category': 'Cooling & Power',
    'close': 322.30, 'rs_vs_spy_20d': 0.048, 'pct_from_52w_high': -0.15, 'volume_ratio': 1.3,
    'quant_score': 80,
    'valuation': {'forwardPE': 52, 'peg': 1.8, 'vs_peers': 'FAIR'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'Insufficient open-market data. Routine RSU vestings only.',
    'short_interest_pct': 0.028, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-07-29', 'earnings_days_away': 20, 'earnings_risk': 'EARNINGS_NEAR',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': '$340 call positioning ahead of July 29 earnings.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Strong Buy consensus (18/25 analysts). Avg PT $363-377. Upside ~17-20% from current.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'BULLISH',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'NEUTRAL', 'taiwan_exposure': 'LOW',
    'govt_catalyst': 'NONE',
    'pricing_power': 'STRONG_POSITION',
    'pricing_power_detail': 'Liquid cooling for AI racks requires certified thermal integration — VRT is the market leader. Hyperscalers cannot switch mid-build. Q1 FY26 revenue +30% YoY, adjusted EPS guidance raised 51%. Backlog growing. AI data center density (GB200/GB300) requires liquid cooling at 120kW+ rack — VRT thermal solutions are spec\'d into NVDA reference designs.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Institutional ownership growing rapidly as AI data center buildout demand confirms. Multiple large-cap growth funds added in Q1 2026.',
    'buy_zone': '$295-$325',
    'price_target': '$400',
    'stop_loss': '$258',
    'thesis_hold_conditions': 'Hold as long as: AI data center buildout expanding; liquid cooling spec rate increasing for high-density GPU racks; revenue growing >25% YoY; adjusted EPS tracking to $6.35 guidance',
    'thesis_break_triggers': 'EXIT if: Alternative cooling technology (immersion cooling) disrupts VRT liquid cooling market OR AI capex pause by 2+ hyperscalers OR Q2 revenue misses and guidance cut July 29',
    'key_catalysts': 'Q2 FY26 earnings July 29 (20 days — near-term binary), hyperscaler data center expansion, GB200/GB300 rack density increasing VRT content per rack',
    'key_risks': 'High PE (52x), 15% below 52-week high (recovery play), earnings miss risk July 29, supply chain constraints on lead times',
    'analyst_note': 'VRT is the picks-and-shovels play on GB200/GB300 density. Every NVDA Blackwell Ultra rack requires liquid cooling — VRT is spec\'d into NVDA reference designs. Q1 revenue +30% and EPS guidance +51% are not coincidences; they are the direct output of hyperscalers building to accommodate 120kW+ racks. At $322 with a consensus PT of $370+ and earnings in 20 days, the trade is earnings into a bull setup. Biggest risk: Q2 miss = -15% instantly. Size accordingly; the risk/reward favors accumulation in the $295-$325 zone.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'CEG', 'company': 'Constellation Energy',
    'is_core': True, 'filter_status': 'PASSED',
    'ai_category': 'Energy',
    'close': 245.87, 'rs_vs_spy_20d': 0.022, 'pct_from_52w_high': -0.12, 'volume_ratio': 1.1,
    'quant_score': 72,
    'valuation': {'forwardPE': 22, 'peg': 0.9, 'vs_peers': 'CHEAP'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'Insufficient data; no material open-market transactions noted.',
    'short_interest_pct': 0.031, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-08-05', 'earnings_days_away': 27, 'earnings_risk': 'LOW',
    'options_flow': 'NEUTRAL', 'options_detail': 'Moderate positioning; no unusual activity.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Nuclear PPA deals driving PT raises across energy desk. Strong Buy consensus.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'NEUTRAL',
    'tech_impact': 'INDIRECT',
    'taiwan_signal': 'NEUTRAL', 'taiwan_exposure': 'NONE',
    'govt_catalyst': 'CONFIRMED',
    'pricing_power': 'PRICING_LEADER',
    'pricing_power_detail': 'Nuclear power is the only 24/7 carbon-free baseload energy at scale. Meta 20-year PPA (Illinois, June 2025). Meta, Microsoft, and Google all competing for CEG nuclear capacity — seller\'s market. Q1 2026 revenue +64% YoY. FY26 guidance $11-12 EPS ($2.74 Q1 actual). PEG 0.9 = cheapest high-quality AI power play.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Wellington, BlackRock energy desks accumulating nuclear exposure. Clean energy mandates driving institutional flows.',
    'buy_zone': '$228-$250',
    'price_target': '$320',
    'stop_loss': '$195',
    'thesis_hold_conditions': 'Hold as long as: AI data center power demand growing; nuclear PPA demand at premium pricing; FY26 EPS on track to $11-12 guidance; federal nuclear policy supportive (DOE loan guarantees)',
    'thesis_break_triggers': 'EXIT if: Hyperscaler AI capex cuts reduce power demand PPA pipeline OR nuclear safety incident at CEG plants (PR/regulatory risk) OR grid interconnection delays push revenue recognition beyond 2027',
    'key_catalysts': 'New PPA announcements, additional hyperscaler nuclear deals, DOE nuclear loan guarantee expansion, SMR permitting acceleration',
    'key_risks': 'Nuclear operations risk, grid interconnection bottlenecks, falling natural gas prices could reduce nuclear premium, 12% below 52-week high',
    'analyst_note': 'CEG is the cheapest genuine AI power play at PEG 0.9. While NVDA trades at 40x earnings, CEG trades at 22x despite delivering 64% revenue growth and $11-12 EPS this year. The thesis is simple: AI data centers need power 24/7/365, and nuclear is the ONLY source that is zero-carbon, baseload, and scale. Meta, Microsoft, and Google are ALL competing for CEG\'s limited nuclear output — that is a seller\'s market. The 20-year PPA structure means revenue is locked in regardless of spot power markets. At $245 this is a high-conviction buy with significant upside and the lowest valuation on the board.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'TSM', 'company': 'Taiwan Semiconductor Mfg.',
    'is_core': True, 'filter_status': 'PASSED',
    'ai_category': 'Foundry',
    'close': 79.00, 'rs_vs_spy_20d': 0.018, 'pct_from_52w_high': -0.08, 'volume_ratio': 1.0,
    'quant_score': 74,
    'valuation': {'forwardPE': 24, 'peg': 1.1, 'vs_peers': 'CHEAP'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'VP Liu bought 2,000 shares open-market at $69.83-$69.98 May 2026. Small but positive signal — executive paid up, stock now at $79. CFO bought ESPP shares at $76.01 June 5. Pattern is constructive.',
    'short_interest_pct': 0.009, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-10-16', 'earnings_days_away': 99, 'earnings_risk': 'LOW',
    'options_flow': 'NEUTRAL', 'options_detail': 'Moderate institutional positioning; no unusual flow.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Multiple PT raises on N2 ramp and CoWoS sold-out thesis.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'NEUTRAL',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'POSITIVE', 'taiwan_exposure': 'EXTREME',
    'govt_catalyst': 'CONFIRMED',
    'pricing_power': 'PRICING_LEADER',
    'pricing_power_detail': 'Only sub-3nm foundry globally — NVDA, AMD, Apple, Qualcomm have no alternative. CoWoS advanced packaging SOLD OUT through 2027. N2 node booked solid with unprecedented 5-fab-phase ramp. Arizona advanced packaging facility adds US-based capacity. Geopolitical risk premium limits valuation but does not remove pricing power.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Tiger Global holds TSM as top-5 position Q1 2026. Multiple sovereign wealth funds and long-only funds added on N2 ramp thesis.',
    'buy_zone': '$72-$80',
    'price_target': '$105',
    'stop_loss': '$60',
    'thesis_hold_conditions': 'Hold as long as: N2 and CoWoS demand from NVDA/AMD/Apple growing; cross-strait military situation remains below armed conflict; gross margins expanding; Arizona facility on track',
    'thesis_break_triggers': 'EXIT if: PLA conducts armed incursion or blockade of Taiwan OR Intel achieves competitive process node at scale (18A or better with >10% hyperscaler adoption) OR CoWoS demand cancellations >20% from top customers',
    'key_catalysts': 'N2 ramp, CoWoS capacity expansion, Arizona packaging facility, CHIPS Act funding deployment, NVDA GB300 demand',
    'key_risks': '⚠️ CROSS-STRAIT RISK ELEVATED: CFR assigns 50%+ probability to crisis in 2026. PLA building toward 2027 readiness. Any geopolitical escalation = -30%+ immediate move. This risk is real and must be sized appropriately. Discount 15-20% from fundamental value for geopolitical risk premium.',
    'analyst_note': 'TSM is simultaneously the most important company in the world and one of the most politically complex holdings in institutional portfolios. The fundamental case is iron-clad: only sub-3nm foundry, CoWoS sold out, N2 in unprecedented ramp. The risk is equally real: CFR assigns 50%+ cross-strait crisis probability in 2026, and any military escalation triggers immediate supply chain panic across the entire technology sector. Position sizing should reflect this: TSM should be in every portfolio, but sized smaller than fundamentals alone would suggest. VP Liu\'s open-market buy at $69.98 when stock is now $79 shows insider comfort — but executives in Taiwan may have less visibility into geopolitical tail risk than the US intelligence community.',
    'sector_rotation_impact': 'NEUTRAL',
  },

  {
    'symbol': 'VST', 'company': 'Vistra Corp.',
    'is_core': True, 'filter_status': 'PASSED',
    'ai_category': 'Energy',
    'close': 185.00, 'rs_vs_spy_20d': 0.028, 'pct_from_52w_high': -0.20, 'volume_ratio': 1.0,
    'quant_score': 68,
    'valuation': {'forwardPE': 18, 'peg': 0.8, 'vs_peers': 'CHEAP'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'Insufficient open-market data for 2026.',
    'short_interest_pct': 0.045, 'squeeze_risk': 'MEDIUM',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-08-05', 'earnings_days_away': 27, 'earnings_risk': 'LOW',
    'options_flow': 'NEUTRAL', 'options_detail': 'Moderate positioning.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Buy consensus, PT $232 consensus. 38% Strong Buy.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'NEUTRAL',
    'tech_impact': 'INDIRECT',
    'taiwan_signal': 'NEUTRAL', 'taiwan_exposure': 'NONE',
    'govt_catalyst': 'CONFIRMED',
    'pricing_power': 'PRICING_LEADER',
    'pricing_power_detail': 'Meta 20-year PPA for 2,600 MW from VST nuclear plants (Davis-Besse, Perry, Beaver Valley) starting late 2026. Cogentrix 5,500 MW natural gas acquisition underway. 4.5 GW capacity additions confirmed. Nuclear scarcity + long-term PPA structure = locked-in cash flows at premium pricing.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Clean energy and AI power funds accumulating. Short interest at 4.5% creates squeeze potential on good earnings.',
    'buy_zone': '$168-$188',
    'price_target': '$260',
    'stop_loss': '$145',
    'thesis_hold_conditions': 'Hold as long as: Meta nuclear PPA revenue starting as scheduled; Cogentrix acquisition closing without issues; nuclear capacity factor above 90%; AI data center power demand growing',
    'thesis_break_triggers': 'EXIT if: Meta renegotiates or cancels PPA terms OR nuclear plant extended outage >6 months OR natural gas prices collapse eliminating thermal generation margin',
    'key_catalysts': 'Meta PPA revenue commencement late 2026, Cogentrix close, Q3 2026 earnings',
    'key_risks': '20% below 52-week high suggests distribution. Short interest 4.5% — elevated. PPA doesn\'t start until late 2026.',
    'analyst_note': 'VST offers the highest upside (40%+ to consensus $232) of any energy name on the board at the cheapest valuation (PEG 0.8). The Meta nuclear deal for 2,600 MW of baseload capacity is a 20-year locked revenue stream. Stock is 20% below its 52-week high — this reflects execution risk on Cogentrix and PPA commencement timing, not thesis invalidation. 4.5% short interest = modest squeeze potential. The risk/reward at $185 with a path to $260 is compelling for a 12-18 month hold.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'ASML', 'company': 'ASML Holding N.V.',
    'is_core': False, 'filter_status': 'PASSED',
    'ai_category': 'Chips',
    'close': 1680.00, 'rs_vs_spy_20d': 0.041, 'pct_from_52w_high': -0.04, 'volume_ratio': 1.2,
    'quant_score': 78,
    'valuation': {'forwardPE': 40, 'peg': 1.7, 'vs_peers': 'FAIR'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'Dutch company; Form 4 filings limited. No unusual activity noted.',
    'short_interest_pct': 0.008, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-10-15', 'earnings_days_away': 98, 'earnings_risk': 'LOW',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': 'Bernstein PT raise to $2,623 (from $1,971) catalyzed call buying.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Bernstein PT $1,971 → $2,623 on July 6, 2026. Consensus PT $1,741 — Bernstein sees 56% above consensus. Strong Buy.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'NEUTRAL',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'POSITIVE', 'taiwan_exposure': 'HIGH',
    'govt_catalyst': 'CONFIRMED',
    'pricing_power': 'PRICING_LEADER',
    'pricing_power_detail': 'Global monopoly on EUV lithography — TSMC, Samsung, and Intel cannot produce sub-7nm chips without ASML EUV machines. N2 ramp requires next-gen High-NA EUV. There is no second supplier, no substitute, no alternative. This is the most structurally defensible pricing position in all of technology. ASML raises prices; customers pay.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Coatue added ASML as newest position Q1 2026 — notable given Coatue was trimming NVDA simultaneously.',
    'buy_zone': '$1600-$1690',
    'price_target': '$2200',
    'stop_loss': '$1360',
    'thesis_hold_conditions': 'Hold as long as: TSMC N2 and N1.4 ramp requires ASML High-NA EUV; Samsung/Intel EUV demand confirmed; no viable EUV alternative emerges; backlog growing',
    'thesis_break_triggers': 'EXIT if: Chinese domestic EUV clone achieves >5nm production capability OR TSMC encounters fundamental N2 yield issue causing ramp delay >4 quarters OR Dutch government imposes new ASML export restrictions materially beyond current China controls',
    'key_catalysts': 'High-NA EUV ramp, TSMC N2 capacity expansion, Bernstein PT $2,623 creates momentum',
    'key_risks': 'TSMC cross-strait risk (ASML biggest customer), Chinese EUV clone risk (long-dated), current China export controls reduce backlog ~15%',
    'analyst_note': 'ASML is the most durable structural monopoly in all of technology. Bernstein\'s $2,623 PT — 56% above Wall Street consensus — reflects what happens when you model true scarcity: TSMC cannot build N2 without ASML High-NA EUV, period. Coatue adding ASML while trimming NVDA is the most institutional signal on this board. The key risk is the same as TSM: cross-strait exposure via TSMC. But ASML is Dutch and machines are replaceable (vs. fabs). For investors who want AI infrastructure without the full Taiwan political risk, ASML at $1,680 is the cleanest expression.',
    'sector_rotation_impact': 'NEUTRAL',
  },

  {
    'symbol': 'PLTR', 'company': 'Palantir Technologies',
    'is_core': True, 'filter_status': 'PASSED',
    'ai_category': 'AI Software',
    'close': 129.00, 'rs_vs_spy_20d': 0.035, 'pct_from_52w_high': -0.02, 'volume_ratio': 1.2,
    'quant_score': 74,
    'valuation': {'forwardPE': 95, 'peg': 3.2, 'vs_peers': 'EXPENSIVE'},
    'insider_activity': 'BEARISH_INSIDER',
    'insider_detail': '⚠️ WARNING: Insiders selling consistently under 10b5-1. CTO Shyam Sankar sold in June. Director Moore sold 16,000 shares at ~$130 June 15. Jeffrey Buckley sold 1,481 shares at $128.80 June 11. Pattern: insiders selling near all-time highs under pre-planned schemes — standard for SBC-heavy company, but scale is notable at $129.',
    'short_interest_pct': 0.038, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-08-04', 'earnings_days_away': 26, 'earnings_risk': 'LOW',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': 'Bullish positioning on government AI expansion thesis.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Strong Buy consensus. Project Maven permanent status drives PT raises.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'BULLISH',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'NEUTRAL', 'taiwan_exposure': 'NONE',
    'govt_catalyst': 'CONFIRMED',
    'pricing_power': 'STRONG_POSITION',
    'pricing_power_detail': 'Gotham (government) and Foundry (enterprise) platforms are deeply embedded in DoD/IC workflows — switching cost is a multi-year retraining and re-integration project. Project Maven: permanent DoD program of record with recurring 9-figure annual appropriations. $10B+ Army data contracts. AIP (AI Platform) now on Azure Government. 8-firm Pentagon AI deal participant.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Institutional ownership increasing as government AI becomes a budget line item rather than experimental program.',
    'buy_zone': '$118-$130',
    'price_target': '$165',
    'stop_loss': '$100',
    'thesis_hold_conditions': 'Hold as long as: Project Maven annual appropriations growing; commercial AIP revenue growing >40% YoY; government AI spending expanding as % of DoD budget; net revenue retention >115%',
    'thesis_break_triggers': 'EXIT if: Project Maven appropriations cut >20% OR major DoD contract dispute materially impairs Gotham revenue OR commercial AIP growth falls below 25% for 2 quarters OR DOGE-style federal spending cuts hit IC/DoD AI budgets',
    'key_catalysts': 'Project Maven budget expansion, new IC contract disclosures, commercial AIP Fortune 500 wins, Q2 earnings Aug 4',
    'key_risks': '⚠️ EXPENSIVE at 95x PE, PEG 3.2. Insider selling at $128-130 creates technical ceiling. DOGE risk to federal IT spending. Stock needs to grow into its valuation — any miss = -20%.',
    'analyst_note': 'PLTR is the most expensive stock on the board and the most government-dependent. Project Maven becoming a permanent program of record (not just annual experiment) is the key fundamental shift — it turns volatile government contract revenue into something resembling a recurring subscription. $10B+ Army contracts and Pentagon AI deals (8-firm) create a moat competitors cannot replicate without years of security clearances. BUT: 95x PE is demanding, insiders are selling at $128-130, and a miss will hurt. This is a HOLD for existing investors and a BUY ONLY on a 10-15% pullback for new investors. Sizing below 5% of portfolio until valuation rationalizes.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'ARM', 'company': 'Arm Holdings plc',
    'is_core': False, 'filter_status': 'PASSED',
    'ai_category': 'Chips',
    'close': 148.00, 'rs_vs_spy_20d': 0.044, 'pct_from_52w_high': -0.10, 'volume_ratio': 1.3,
    'quant_score': 77,
    'valuation': {'forwardPE': 85, 'peg': 2.8, 'vs_peers': 'EXPENSIVE'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'SoftBank majority holder. No material Form 4 activity.',
    'short_interest_pct': 0.032, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-07-29', 'earnings_days_away': 20, 'earnings_risk': 'EARNINGS_NEAR',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': '$160 call buying ahead of Q1 FY27 earnings July 29.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'AI chip royalty thesis driving PT increases. Q1 FY27 earnings July 29 expected strong.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'BULLISH',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'NEUTRAL', 'taiwan_exposure': 'LOW',
    'govt_catalyst': 'NONE',
    'pricing_power': 'PRICING_LEADER',
    'pricing_power_detail': 'ARM ISA is the standard for mobile, edge, and increasingly server AI (AWS Graviton, Apple M-series, NVDA Grace CPU, Qualcomm Snapdragon). Every NVDA GB200 NVL72 rack includes ARM-based Grace CPU cores generating royalties. Custom silicon trend (every hyperscaler building ASICs) = every new custom chip pays ARM royalties. ARM collects on the AI chip supercycle regardless of who wins GPU competition.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Multiple growth funds added ARM as royalty play on AI silicon boom — Dragoneer, Whale Rock adding Q1 2026.',
    'buy_zone': '$135-$150',
    'price_target': '$195',
    'stop_loss': '$115',
    'thesis_hold_conditions': 'Hold as long as: Royalty revenue per chip expanding (ARM v9 migration driving ASP uplift); custom silicon trend continuing; server ARM adoption growing; SoftBank not dumping shares',
    'thesis_break_triggers': 'EXIT if: RISC-V adoption at hyperscale exceeds 10% of new chip designs OR SoftBank mass sells stake OR Q1 FY27 royalty revenue misses significantly July 29',
    'key_catalysts': 'Q1 FY27 earnings July 29, v9 architecture royalty uplift, AWS Graviton 5, Apple M5, custom ASIC proliferation',
    'key_risks': 'Expensive at 85x PE. RISC-V existential threat (long-dated but real). SoftBank overhang. Earnings July 29 near-term binary.',
    'analyst_note': 'ARM is the toll booth on the AI chip superhighway. Every NVDA GB200 (Grace CPU = ARM), every Apple chip, every Amazon Graviton, every custom hyperscaler ASIC pays ARM royalties. The custom silicon trend — which benefits AVGO and MRVL — also benefits ARM because every new ASIC requires an ISA license. ARM v9 architecture charges 2-3x the royalty rate of v8. At $148 and 10% below its 52-week high with earnings July 29, this is a clean setup for a royalty expansion story.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'CRDO', 'company': 'Credo Technology Group',
    'is_core': False, 'filter_status': 'PASSED',
    'ai_category': 'Optical & Networking',
    'close': 72.00, 'rs_vs_spy_20d': 0.071, 'pct_from_52w_high': -0.06, 'volume_ratio': 1.8,
    'quant_score': 80,
    'valuation': {'forwardPE': 60, 'peg': 2.4, 'vs_peers': 'FAIR'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'Insider activity neutral; routine RSU vesting.',
    'short_interest_pct': 0.055, 'squeeze_risk': 'MEDIUM',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-09-10', 'earnings_days_away': 63, 'earnings_risk': 'LOW',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': '$80 call sweep on ANET-driven AI networking momentum.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Multiple upgrades on AI networking acceleration. Riding ANET tailwind.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'BULLISH',
    'tech_impact': 'DIRECT_BENEFICIARY',
    'taiwan_signal': 'POSITIVE', 'taiwan_exposure': 'LOW',
    'govt_catalyst': 'NONE',
    'pricing_power': 'STRONG_POSITION',
    'pricing_power_detail': 'PAM-4 SerDes and Active Electrical Cable technology for 800G/1.6T AI networking. Co-packaged optics for next-gen switches. CRDO\'s AEC products are qualified in Microsoft, Meta, and Google hyperscaler networks. Small-cap with outsized exposure to the networking upgrade cycle that ANET is leading.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'AI networking rotation trade; multiple hedge funds adding CRDO as leveraged ANET bet.',
    'buy_zone': '$65-$73',
    'price_target': '$100',
    'stop_loss': '$55',
    'thesis_hold_conditions': 'Hold as long as: AI networking upgrade cycle from 400G → 1.6T continuing; CRDO design wins at hyperscalers maintained; revenue growing >40% YoY',
    'thesis_break_triggers': 'EXIT if: ANET or major OEM develops competing SerDes in-house OR CRDO loses a top-2 hyperscaler design win OR revenue misses two consecutive quarters',
    'key_catalysts': 'AI networking upgrade supercycle, 1.6T adoption, ANET partnership deepening, hyperscaler design wins',
    'key_risks': 'High short interest (5.5%) = volatile. Small cap — liquidity risk. Customer concentration risk. Valuation rich at 60x PE.',
    'analyst_note': 'CRDO is the leveraged bet on ANET\'s networking supercycle. If ANET is shipping 1.6Tbps switches, CRDO supplies the SerDes and AEC technology inside them. Revenue growing >50% on AI networking demand. 5.5% short interest creates squeeze potential on positive catalysts. This is a smaller position (2-3% max) due to volatility and customer concentration, but the risk/reward from $72 to $100 target with AI networking acceleration is compelling.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'GEV', 'company': 'GE Vernova',
    'is_core': False, 'filter_status': 'PASSED',
    'ai_category': 'Energy',
    'close': 318.00, 'rs_vs_spy_20d': 0.038, 'pct_from_52w_high': -0.08, 'volume_ratio': 1.2,
    'quant_score': 72,
    'valuation': {'forwardPE': 45, 'peg': 1.6, 'vs_peers': 'FAIR'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'Insufficient data; no material open-market buys.',
    'short_interest_pct': 0.022, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-07-23', 'earnings_days_away': 14, 'earnings_risk': 'EARNINGS_NEAR',
    'options_flow': 'BULLISH_OPTIONS', 'options_detail': 'Call buying ahead of Q2 earnings July 23.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Grid modernization + AI power demand thesis driving upgrades.',
    'news_sentiment': 'BULLISH',
    'social_sentiment': 'NEUTRAL',
    'tech_impact': 'INDIRECT',
    'taiwan_signal': 'NEUTRAL', 'taiwan_exposure': 'NONE',
    'govt_catalyst': 'CONFIRMED',
    'pricing_power': 'STRONG_POSITION',
    'pricing_power_detail': 'Gas turbines for AI data center power and grid-scale gas peaking plants are 2-4 year backlog. Wind and grid equipment backlog growing. Only GE Vernova and Siemens Energy can supply large-frame gas turbines at AI data center scale — both are capacity-constrained. DOE grid modernization funding flows through GEV equipment.',
    'smart_money_13f': 'SMART_MONEY_ACCUMULATING',
    'smart_money_detail': 'Infrastructure and energy transition funds accumulating GEV on AI power demand thesis.',
    'buy_zone': '$295-$322',
    'price_target': '$420',
    'stop_loss': '$255',
    'thesis_hold_conditions': 'Hold as long as: AI data center power demand growing; gas turbine backlog expanding; grid modernization capex sustained; government energy infrastructure spending maintained',
    'thesis_break_triggers': 'EXIT if: AI capex pause reduces new data center power orders OR political reversal on grid modernization funding OR Q2 earnings significant miss July 23',
    'key_catalysts': 'Q2 earnings July 23 (14 days — near-term), AI data center power contract wins, DOE grid funding deployment',
    'key_risks': 'Q2 earnings in 14 days = HIGH_EVENT_RISK. HIGH_EVENT_RISK means binary outcome within 2 weeks.',
    'analyst_note': 'GEV is the infrastructure play for AI power that most equity analysts miss. AI data centers need gas turbines for backup/peaking power, and GEV has a 2-4 year backlog of turbine orders. The DOE is actively funding grid modernization ($73B+) and GEV equipment is the primary beneficiary. Q2 earnings July 23 are the near-term catalyst/risk — positive surprise = $350+ within weeks. PEG 1.6 is reasonable for 25%+ revenue growth. Size this at 2-3% with intent to add after earnings confirmation.',
    'sector_rotation_impact': 'FAVORED',
  },

  {
    'symbol': 'MU', 'company': 'Micron Technology',
    'is_core': True, 'filter_status': 'PASSED',
    'ai_category': 'Memory',
    'close': 1032.00, 'rs_vs_spy_20d': -0.008, 'pct_from_52w_high': -0.13, 'volume_ratio': 0.9,
    'quant_score': 62,
    'valuation': {'forwardPE': 14, 'peg': 0.5, 'vs_peers': 'CHEAP'},
    'insider_activity': 'BEARISH_INSIDER',
    'insider_detail': '🚨 HIGHEST PRIORITY RED FLAG: Insiders selling at HIGHEST RATE SINCE 2010. CEO Sanjay Mehrotra sold ~$21M at $536 (May 1), ~$36M at $960 (May 29), ~$46M at $1,128-1,192 (June 26). EVP Arnzen sold $40M at $1,077-1,096 (July 1). Director Dugle sold 1,300 shares at $1,150 (June 30). TOTAL: $143M+ in insider sales since May 2026. CEO selling into every rally. Stock is now at $1,032 — BELOW where CEO sold in June at $1,128-1,192. TEXTBOOK DISTRIBUTION AT TOP.',
    'short_interest_pct': 0.031, 'squeeze_risk': 'LOW',
    'earnings_revision': 'REVISIONS_UP',
    'earnings_date': '2026-09-24', 'earnings_days_away': 77, 'earnings_risk': 'LOW',
    'options_flow': 'NEUTRAL', 'options_detail': 'Mixed flow; retail bullish but institutional hedging elevated.',
    'analyst_action': 'UPGRADED', 'analyst_detail': 'Buy consensus (29 analysts). PT range $1,264-$1,458. But analyst upgrades lag insider distribution.',
    'news_sentiment': 'NEUTRAL',
    'social_sentiment': 'BULLISH',
    'tech_impact': 'INDIRECT',
    'taiwan_signal': 'POSITIVE', 'taiwan_exposure': 'LOW',
    'govt_catalyst': 'PENDING',
    'pricing_power': 'COMPETITIVE',
    'pricing_power_detail': '⚠️ HBM4 SOLE-SOURCE THESIS IS DEAD: Jensen Huang confirmed ALL THREE suppliers (SK Hynix 60-70%, Samsung 25-30%, Micron ~10%) for Vera Rubin HBM4 on June 5, 2026. MU is the SMALLEST HBM4 allocatee. SK Hynix dominates. Memory is cyclically a commodity and MU does not have the pricing leverage previously assumed. HBM3E margins will compress as supply expands. Previous thesis of demand-driven pricing power is fundamentally weakened.',
    'smart_money_13f': 'SMART_MONEY_NEUTRAL',
    'smart_money_detail': 'Institutional ownership flat to slightly declining Q2 2026. No major new positions. Smart money watching insider distribution.',
    'buy_zone': 'NOT BUYING — AWAIT INSIDER SELLING EXHAUSTION',
    'price_target': '$1,264',
    'stop_loss': '$880',
    'thesis_hold_conditions': 'For existing holders only: Hold as long as HBM4 demand exceeds combined MU+SK Hynix supply AND CEO stops selling AND gross margins expanding',
    'thesis_break_triggers': 'SELL NOW if you own it: CEO is already selling $143M. Stock below CEO\'s June sale prices. HBM4 sole-source thesis dead. Wait for insider selling to exhaust before re-entering. DO NOT buy while CEO is distributing.',
    'key_catalysts': 'AI memory demand remains strong in absolute terms; HBM4 volume ramp; CHIPS Act grant pending',
    'key_risks': '🚨 INSIDER SELLING AT 14-YEAR HIGH. Stock trading BELOW CEO\'s June sale prices. HBM4 not sole-source — SK Hynix wins 60-70% of Vera Rubin allocation. Memory cyclical: DRAM spot prices can reverse. Samsung back in HBM4 qualification. Retail crowd still bullish = crowded long.',
    'analyst_note': 'CAUTION on MU despite strong analyst sentiment. The divergence between REVISIONS_UP and BEARISH_INSIDER (CEO selling $143M+ since May) is the loudest divergence signal on this board. Rule: when the CEO sells $143M in 8 weeks at progressively higher prices (peak $1,192 in June) and the stock is now at $1,032 — below his sale prices — the CEO is almost certainly right. The HBM4 catalyst is real but already priced: SK Hynix has 60-70% of Vera Rubin allocation, not MU. Retail bulls are right that AI memory demand is secular, but they are wrong that MU is the primary beneficiary. HOLD for existing investors; DO NOT initiate new positions until insider selling exhausts.',
    'sector_rotation_impact': 'DISFAVORED',
  },

  {
    'symbol': 'ORCL', 'company': 'Oracle Corporation',
    'is_core': True, 'filter_status': 'CORE_OVERRIDE',
    'ai_category': 'Cloud',
    'close': 140.49, 'rs_vs_spy_20d': -0.015, 'pct_from_52w_high': -0.22, 'volume_ratio': 0.8,
    'quant_score': 48,
    'valuation': {'forwardPE': 28, 'peg': 1.9, 'vs_peers': 'FAIR'},
    'insider_activity': 'NEUTRAL', 'insider_detail': 'Insufficient Form 4 data for recent period.',
    'short_interest_pct': 0.021, 'squeeze_risk': 'LOW',
    'earnings_revision': 'STABLE',
    'earnings_date': '2026-09-10', 'earnings_days_away': 63, 'earnings_risk': 'LOW',
    'options_flow': 'BEARISH_OPTIONS', 'options_detail': '🚨 50x NORMAL PUT VOLUME: 10,000 put contracts at $190 strike traded ahead of June 10 earnings — near-50x normal outstanding. Bearish options activity confirmed.',
    'options_detail': '50x normal put activity before Q3 FY26 earnings — $190 strike puts. Institutional hedging/shorting into earnings.',
    'analyst_action': 'NEUTRAL', 'analyst_detail': 'Mixed. Revenue +22% but FCF deeply negative ($24.7B trailing outflow). Stargate contractor status partially priced in.',
    'news_sentiment': 'NEUTRAL',
    'social_sentiment': 'NEUTRAL',
    'tech_impact': 'INDIRECT',
    'taiwan_signal': 'NEUTRAL', 'taiwan_exposure': 'NONE',
    'govt_catalyst': 'CONFIRMED',
    'pricing_power': 'STRONG_POSITION',
    'pricing_power_detail': 'Oracle database lock-in is real but legacy. OCI (Oracle Cloud Infrastructure) is building AI data centers (Stargate partner). However, FCF negative $24.7B trailing — massive capex burn with uncertain return timeline. Database customers cannot easily migrate, but new AI workloads prefer AWS/Azure.',
    'smart_money_13f': 'SMART_MONEY_NEUTRAL',
    'smart_money_detail': 'No significant new institutional adds. Smart money watching FCF recovery timeline.',
    'buy_zone': 'AVOID NEAR TERM',
    'price_target': '$170',
    'stop_loss': '$118',
    'thesis_hold_conditions': 'Hold only if: FCF turns positive by Q2 FY27; OCI AI revenue demonstrates hyperscaler-competitive growth rate; Stargate contract flow exceeds $10B annual run rate',
    'thesis_break_triggers': 'EXIT if: FCF remains negative for 4+ consecutive quarters OR OCI loses Stargate Phase 2 OR database migration to PostgreSQL/cloud-native accelerates beyond manageable pace',
    'key_catalysts': 'Stargate Phase 2 contracts, OCI AI revenue acceleration, FCF recovery',
    'key_risks': '🚨 AVOID: 50x normal put activity, FCF -$24.7B trailing, 22% below 52-week high, stock -0.78% today. The market is telling you something. Capex burn without demonstrated returns = value trap risk.',
    'analyst_note': 'AVOID near-term. ORCL is a CORE stock forced into analysis but the setup is poor: 50x normal put volume before earnings, FCF negative $24.7B trailing, stock 22% below 52-week high and trending lower today. Revenue growth +22% is real but the capex required to fund OCI build-out is destroying cash flow. Until FCF turns positive and OCI demonstrates it can compete with AWS/Azure at scale, ORCL is a HOLD for existing investors and an AVOID for new capital. Stargate partnership is a real catalyst but partially priced. The put activity is the loudest signal here — institutional money is hedging or shorting this into earnings. Respect it.',
    'sector_rotation_impact': 'NEUTRAL',
  },

]

# ── PHASE 7: COMPUTE FINAL SCORES ──────────────────────────────────────────────
for candidate in all_candidates:
    qs  = candidate.get('quant_score', 50)
    val = {'CHEAP':80,'FAIR':50,'EXPENSIVE':20}.get(candidate.get('valuation',{}).get('vs_peers','FAIR'),50)
    ins = {'BULLISH_INSIDER':100,'BULLISH':100,'NEUTRAL':50,'BEARISH_INSIDER':20,'BEARISH':20}.get(candidate.get('insider_activity','NEUTRAL'),50)
    rev = {'REVISIONS_UP':100,'STABLE':50,'REVISIONS_DOWN':20}.get(candidate.get('earnings_revision','STABLE'),50)
    opt = {'BULLISH_OPTIONS':80,'NEUTRAL':50,'BEARISH_OPTIONS':20}.get(candidate.get('options_flow','NEUTRAL'),50)
    ana = {'UPGRADED':90,'INITIATED':60,'NEUTRAL':50,'DOWNGRADED':20}.get(candidate.get('analyst_action','NEUTRAL'),50)
    nws = {'BULLISH':80,'NEUTRAL':50,'BEARISH':20}.get(candidate.get('news_sentiment','NEUTRAL'),50)
    soc = {'BULLISH':80,'NEUTRAL':50,'BEARISH':20}.get(candidate.get('social_sentiment','NEUTRAL'),50)
    tec = {'DIRECT_BENEFICIARY':100,'INDIRECT':50,'THREATENED':0}.get(candidate.get('tech_impact','INDIRECT'),50)
    twn = {'POSITIVE':100,'NEUTRAL':50,'RISK':20}.get(candidate.get('taiwan_signal','NEUTRAL'),50)
    gov = {'CONFIRMED':100,'PENDING':75,'NONE':50,'POLITICAL_RISK':25}.get(candidate.get('govt_catalyst','NONE'),50)
    mac = 100 if macro_summary.get('vix',25) < 20 else 50
    prc = {'PRICING_LEADER':100,'STRONG_POSITION':75,'COMPETITIVE':50,'COMMODITY_RISK':20}.get(candidate.get('pricing_power','COMPETITIVE'),50)
    smf = {'SMART_MONEY_ACCUMULATING':100,'SMART_MONEY_NEUTRAL':50,'SMART_MONEY_EXITING':20}.get(candidate.get('smart_money_13f','SMART_MONEY_NEUTRAL'),50)
    sym = candidate.get('symbol','')
    rot_favored = rotation_summary.get('rotation_favored', [])
    rot_disfavored = rotation_summary.get('rotation_disfavored', [])
    rot = 100 if sym in rot_favored else 20 if sym in rot_disfavored else 60
    candidate['sector_rotation_impact'] = 'FAVORED' if rot==100 else 'DISFAVORED' if rot==20 else 'NEUTRAL'
    candidate['final_score'] = round(
        qs*0.20 + val*0.03 + ins*0.10 + rev*0.10 + opt*0.03 + ana*0.03 +
        nws*0.05 + soc*0.03 + tec*0.10 + twn*0.10 + gov*0.10 + mac*0.03 +
        prc*0.08 + smf*0.07 + rot*0.05, 1)
    candidate['conviction'] = 'HIGH' if candidate['final_score'] >= 75 else 'MEDIUM' if candidate['final_score'] >= 55 else 'LOW'

# Filter, sort, rank
all_candidates = [c for c in all_candidates if c.get('final_score',0) >= 40 or c.get('is_core')]
all_candidates.sort(key=lambda x: x.get('final_score',0), reverse=True)
all_candidates = all_candidates[:30]
for i, c in enumerate(all_candidates, 1):
    c['rank'] = i

print(f"Phase 7 complete: {len(all_candidates)} candidates ranked")
for c in all_candidates:
    print(f"  #{c['rank']:2d} {c['symbol']:6s} score={c['final_score']:.1f} [{c['conviction']}]  {c.get('sector_rotation_impact','')}")

# ── PHASE 8A: WRITE watchlist.json ─────────────────────────────────────────────
watchlist_data = {
    'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'analyst_confidence': 'HIGH' if len([c for c in all_candidates if c.get('conviction')=='HIGH']) >= 5 else 'MEDIUM',
    'market_regime': macro_summary.get('market_regime','UNKNOWN'),
    'vix': macro_summary.get('vix',0),
    'treasury_10yr': macro_summary.get('treasury_10yr',0),
    'dxy': macro_summary.get('dxy',0),
    'copper_trend': macro_summary.get('copper_trend','UNKNOWN'),
    'etf_flows': etf_flow_dict,
    'sector_rotation_today': rotation_summary.get('sector_rotation_today','NO_CLEAR_ROTATION'),
    'rotation_favored': rotation_summary.get('rotation_favored',[]),
    'rotation_disfavored': rotation_summary.get('rotation_disfavored',[]),
    'macro_themes': macro_summary.get('macro_themes',[]),
    'emerging_tech_themes': macro_summary.get('emerging_tech_themes',[]),
    'taiwan_signals': macro_summary.get('taiwan_signals',[]),
    'govt_catalysts': macro_summary.get('govt_catalysts',[]),
    'cross_strait_risk': macro_summary.get('cross_strait_risk','MEDIUM'),
    'candidates': all_candidates,
}

try:
    with open('/home/user/watchlist.json', 'w', encoding='utf-8') as f:
        json.dump(watchlist_data, f, indent=2)
    print(f'watchlist.json written: {len(all_candidates)} candidates')
except Exception as e:
    print(f'ERROR writing watchlist.json: {e}')

# ── PHASE 8B: WRITE scan_log.md ────────────────────────────────────────────────
top5 = all_candidates[:5]
lines = [
    f'# Pre-Market Briefing — {date.today().isoformat()}',
    '',
    f'**Market:** {macro_summary["market_regime"]} | VIX {macro_summary["vix"]:.1f} ({("NORMAL" if macro_summary["vix"]<20 else "ELEVATED")}) | 10yr {macro_summary["treasury_10yr"]:.2f}% | DXY {macro_summary["dxy"]:.1f} | Copper: {macro_summary["copper_trend"]}',
    f'**S&P 500:** {macro_summary["sp500"]:,.0f} (SPY ${macro_summary["spy_price"]:.2f}) | YTD +7.7%',
    f'**Rotation:** {rotation_summary["sector_rotation_today"]}',
    f'**Cross-Strait Risk:** {macro_summary["cross_strait_risk"]} (CFR: 50%+ crisis probability 2026)',
    '',
    '## Macro Themes',
    '',
]
for t in macro_summary['macro_themes']:
    lines.append(f'- {t}')
lines += ['', '## Emerging Tech Intelligence', '']
for t in macro_summary['emerging_tech_themes']:
    lines.append(f'- {t}')
lines += ['', '---', '', '## Top 5 Candidates', '']

for c in top5:
    lines += [
        f'### #{c["rank"]} {c["symbol"]} — Score {c["final_score"]:.1f} [{c["conviction"]}]',
        f'*{c["company"]} | {c["ai_category"]} | Price: ${c["close"]:,.2f} | Pricing: {c["pricing_power"]} | Smart Money: {c["smart_money_13f"]} | Rotation: {c["sector_rotation_impact"]}*',
        '',
        c.get('analyst_note',''),
        '',
        f'**Catalysts:** {c["key_catalysts"]}',
        f'**Risks:** {c["key_risks"]}',
        f'**Buy Zone:** {c["buy_zone"]}  |  **Target:** {c["price_target"]}  |  **Stop:** {c["stop_loss"]}',
        f'**Insider:** {c["insider_activity"]} — {c["insider_detail"][:120]}...' if len(c.get("insider_detail",""))>120 else f'**Insider:** {c["insider_activity"]} — {c.get("insider_detail","")}',
        f'**Hold while:** {c["thesis_hold_conditions"]}',
        f'**Exit if:** {c["thesis_break_triggers"]}',
        '',
    ]

lines += ['---', '', '## Sector Rotation & Smart Money', '']
lines += [
    f'**Today\'s Rotation:** {rotation_summary["sector_rotation_today"]}',
    f'**Favored:** {", ".join(rotation_summary["rotation_favored"])}',
    f'**Disfavored:** {", ".join(rotation_summary["rotation_disfavored"])}',
    f'**Rationale:** {rotation_summary["rotation_rationale"]}',
    '',
    '**Smart Money Accumulating:**',
]
for c in all_candidates:
    if c.get('smart_money_13f') == 'SMART_MONEY_ACCUMULATING':
        lines.append(f'- {c["symbol"]}: {c.get("smart_money_detail","")}')

pricing_leaders = [c['symbol'] for c in all_candidates if c.get('pricing_power') in ('PRICING_LEADER','STRONG_POSITION')]
lines += ['', f'**Pricing Power Leaders:** {", ".join(pricing_leaders)}', '', '**⚠️ INSIDER ALERTS:**']
for c in all_candidates:
    if c.get('insider_activity') in ('BEARISH_INSIDER',):
        lines.append(f'- 🚨 {c["symbol"]} BEARISH: {c.get("insider_detail","")[:200]}')
    elif c.get('insider_activity') in ('BULLISH_INSIDER','BULLISH'):
        lines.append(f'- ✅ {c["symbol"]} BULLISH: {c.get("insider_detail","")[:150]}')

lines += [
    '',
    '---',
    '',
    '## Taiwan Signals',
    '',
]
for s in macro_summary.get('taiwan_signals', []):
    lines.append(f'- {s}')

lines += [
    '',
    '## Government Catalysts',
    '',
    '| Company | Type | Status | Priced-In | Key Risk |',
    '|---------|------|--------|-----------|----------|',
]
for g in macro_summary.get('govt_catalysts', []):
    lines.append(f'| {g["company"]} | {g["type"]} | {g["status"]} | {g["priced_in"]} | {g["risk"][:60]} |')

lines += [
    '',
    '---',
    '',
    '## All Candidates Ranked',
    '',
    '| Rank | Symbol | Score | Conv | Price | Buy Zone | Target | Stop | Insider | Rotation |',
    '|------|--------|-------|------|-------|----------|--------|------|---------|----------|',
]
for c in all_candidates:
    ins_flag = '🚨' if c.get('insider_activity') == 'BEARISH_INSIDER' else '✅' if c.get('insider_activity') in ('BULLISH_INSIDER','BULLISH') else '—'
    lines.append(
        f'| #{c["rank"]} | **{c["symbol"]}** | {c["final_score"]:.1f} | {c["conviction"]} | ${c["close"]:,.0f} | {c["buy_zone"]} | {c["price_target"]} | {c["stop_loss"]} | {ins_flag} {c["insider_activity"]} | {c["sector_rotation_impact"]} |'
    )

lines += [
    '',
    '---',
    '',
    '## AVOID List',
    '',
    '| Symbol | Reason | Specific Trigger |',
    '|--------|--------|-----------------|',
    '| MU | CEO sold $143M at $1,128-1,192; stock now $1,032 (below CEO sale price). HBM4 sole-source thesis dead — SK Hynix wins 60-70% Vera Rubin allocation. Insiders dumping at 14-year high rate. | Stop buying until CEO stops selling. |',
    '| ORCL | 50x normal PUT volume ahead of earnings. FCF -$24.7B trailing. 22% below 52-week high and declining. Value trap risk despite AI narrative. | Do not initiate until FCF turns positive. |',
    '| INTC | Not in universe — execution risk on 18A node, lost NVDA foundry bid, irrelevant to AI GPU market. CHIPS Act funds received but management credibility destroyed. | Structural avoid. |',
    '| SMCI | Accounting restatement risk, no proprietary silicon, commodity server assembler. Margin pressure from DELL, HPE, ODM alternatives. | Stay away until clean audit and margin expansion. |',
    '',
    '---',
    '',
    f'*Generated: {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")} | Analyst: Institutional Pre-Market AI Briefing System | Data: Web research + public filings*',
]

content = '\n'.join(lines) + '\n'
try:
    with open('/home/user/scan_log.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print('scan_log.md written')
except Exception as e:
    print(f'ERROR writing scan_log.md: {e}')
