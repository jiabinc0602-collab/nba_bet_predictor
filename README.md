# NBA Betting Analyzer (V3): Active Roster & Matchup Engine

A machine learning pipeline that predicts NBA game outcomes against the spread by analyzing the specific impact of **active players** on a roster rather than generic team averages.

**Current Status:** Phase 3 Complete (Feature Engineering & Profitability Validation) ✅

## 📈 Performance & Evolution

### 🔻 Phase 2: The "Fade" Discovery
* **Approach:** Trained Random Forest on generic team rolling averages (2017-2021).
* **Result:** 44.5% Accuracy on high-confidence bets.
* **Insight:** The model failed to account for "Ghost Data" (injured stars). It would bet on the Lakers even if LeBron was out, leading to confident losses.
* **Pivot:** We briefly deployed a **"Fade Strategy"** (Betting against the model), which yielded a **6.0% ROI**.

### 🚀 Phase 3: The "Active Roster" Solution
* **Approach:** Re-architected the data pipeline to aggregate rolling statistics *only* for players active in the specific game (`MIN > 0`).
* **New Features:**
    * **Roster Impact Score:** Sum of rolling Plus/Minus for active players only.
    * **Chaos Mismatch:** (Active Steals + Opponent Turnovers) vs. (Active Turnovers + Opponent Steals).
    * **Schedule Fatigue:** Automated "Back-to-Back" detection.
* **Result:** Accuracy jumped to **~56.5%** on high-confidence bets (>65% prob), which yields a **6.8% ROI**.
* **Verdict:** The model is now a **Value Predictor** (betting *with* the signal) rather than a contrarian indicator.



## 🛠 Methodology
1.  **Data Ingestion:**
    * `nba_api` for granular player-level game logs (2017-Present).
    * Kaggle dataset for historical betting odds (Spread, Moneyline).
2.  **Feature Engineering:**
    * **Time-Series Shifts:** strict `.shift(1)` logic to prevent data leakage (no future peeking).
    * **Mirror Strategy:** Self-merging the dataframe to align Opponent Stats vs. Team Stats in a single row.
    * **Z-Score Normalization:** (In Progress) Adjusting for league-wide pace inflation.
3.  **Modeling:**
    * **Algorithm:** Random Forest Classifier (Scikit-Learn).
    * **Validation:** Train on Historical Era (2017-2021) -> Test on Unseen "Modern" Era (2021-22).

## 🔮 Next Steps (Phase 4)
* **Live Automation:** Build a scraper to fetch "Projected Starters" for tonight's games to feed the Active Roster engine in real-time.
* **Injury Veto:** Implement a final filter to skip bets where "Game Time Decision" players create too much variance.
