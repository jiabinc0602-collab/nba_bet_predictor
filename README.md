# NBA Spread Predictor (Legacy Research Project)

> **⚠️ Project Status: Archived / Legacy**
>
> This project represents a completed research initiative into quantitative sports modeling. All development has moved to a new repository focused on a real-time, low-latency inference engine for live NBA game prediction.

## 📋 Project Overview
This repository hosts a machine learning pipeline designed to predict NBA game outcomes against the spread (ATS). Unlike traditional models that rely on team-level aggregates, this project implements an **"Active Roster"** approach. It dynamically calculates team strength based solely on the specific players active for a given match, effectively filtering out "noise" from injured or resting star players (often referred to as "Ghost Data").

## 🧠 Quantitative Methodology

### The "Active Roster" Hypothesis
Standard rolling averages fail in the NBA due to high variance in player availability (load management, injuries). A team's season-long offensive rating is irrelevant if their primary scorer is inactive.
* **Solution:** The pipeline aggregates rolling statistics (Plus/Minus, Usage, Turnovers) *only* for players with `MIN > 0` in the target game.
* **Impact:** This dramatically increases signal-to-noise ratio by aligning statistical inputs with the actual lineup on the floor.

### Feature Engineering
Key features derived for the Random Forest Classifier:
* **Roster Impact Score:** Aggregate rolling Plus/Minus for the specific active 8-9 man rotation.
* **Chaos Mismatch:** Quantifying variance by comparing a roster's ability to force turnovers against the opponent's tendency to commit them (Steals + Opponent Turnovers).
* **Schedule Fatigue:** Automated detection of "Back-to-Back" games to account for rest disadvantages.

## 📊 Model Performance & Backtesting

The model was validated using a strict time-series split to prevent data leakage.

* **Training Period:** 2017-2018 Season through 2020-2021 Season (8,000+ games).
* **Testing Period:** 2021-2022 Season (Unseen data).

### Key Results (V3 Model)
| Metric | Value | Notes |
| :--- | :--- | :--- |
| **ROI (Return on Investment)** | **+6.87%** | On bets with >65% confidence |
| **Accuracy (High Confidence)** | **~56.5%** | On bets with >65% confidence |
| **Sample Size** | 418 Bets | Filtered for value threshold |

*Note: A standard betting strategy requires ~52.4% accuracy to break even at -110 odds. An ROI of >5% over a statistically significant sample size indicates legitimate alpha generation.*

## 🛠 Tech Stack & Data Architecture
* **Language:** Python 3.13
* **Data Sources:**
    * `nba_api` (Official League Endpoint) for granular player logs.
    * Historical Odds Data (Kaggle) for spread and moneyline targets.
* **ML Libraries:** Scikit-Learn (Random Forest), Pandas (Time-series manipulation).

## 🚀 Future Development
This research successfully validated the "Active Roster" hypothesis. The next iteration (currently in development) focuses on:
* **Real-time Inference:** integrating live "Projected Starter" feeds to predict lines before tip-off.
* **Micro-betting:** Expanding the feature set to predict quarter-level outcomes.
