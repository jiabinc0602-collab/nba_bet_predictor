# NBA Betting Analyzer (V2)

A machine learning pipeline that identifies statistical edges in NBA betting lines.

**Current Status:** Phase 2 Complete (Model Validation & Strategy Pivot) ✅

## 📉 Project Findings & Strategy
During backtesting on the 2021-2022 NBA season, the Random Forest model exhibited a **strong negative correlation** (44.5% accuracy) on high-confidence bets (>60% probability).

**Root Cause Analysis:**
* **Data Drift:** The model was trained on the "Bubble Era" (2017-2021), where Home Court advantage was statistically negligible due to COVID-19 protocols.
* **Regime Change:** When crowds returned in 2021-22, the model continued to identify "Road Underdogs" as value bets, failing to account for the restored Home Court penalty.

**The "Fade" Strategy:**
Instead of discarding the signal, I inverted it. The model is now deployed as a **Contrarian Indicator**.
* **Signal:** High Confidence (>60%) on Road Underdogs.
* **Action:** Fade the model (Bet Home Favorites).
* **Result:** This inversion yielded a **6.0% ROI** over 371 bets in the test set.

## 🛠 Tech Stack
* **Data Engineering:** `nba_api`, Pandas (Rolling Time-Series Windows)
* **Modeling:** Scikit-Learn (Random Forest Classifier)
* **Feature Engineering:** Four Factors (Rebounding/Turnover Mismatches), "Chaos" Metrics.

**Data**
* **NBA API:** https://github.com/swar/nba_api
* **Kaggle:** Used for betting lines: https://www.kaggle.com/datasets/thedevastator/uncovering-hidden-trends-in-nba-betting-lines-20
