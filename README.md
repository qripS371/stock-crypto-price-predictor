# 📈 Stock & Crypto Price Predictor

Predict the future of stocks and cryptocurrencies using Machine Learning!  
This project uses historical financial data from Yahoo Finance to forecast prices over different timeframes — **next day, week, month, and year**.

---

## 🚀 What Does This Project Do?

This ML-powered forecasting system:

- 🧠 **Collects historical stock and crypto data** (e.g., `BTC-USD`, `ETH-USD`, `TSLA`, `GOOGL`, `MSFT`, `NVDA`, etc.)
- 🔧 **Generates technical features** like returns, volatility, and momentum
- 🏗 **Trains regression models** to predict the closing price across 4 time horizons:
  - Next Day
  - Next 7 Days
  - Next 30 Days
  - Next 365 Days
- 📤 **Saves trained models and future price predictions** for analysis or deployment

---

## 🔍 Currently Analysed Assets

### 📊 Stocks:
- Tesla (`TSLA`)
- Alphabet (`GOOGL`)
- Microsoft (`MSFT`)
- NVIDIA (`NVDA`)
- BYD Company (`BYDDY`)

### 💱 Cryptocurrencies:
- Bitcoin (`BTC-USD`)
- Ethereum (`ETH-USD`)
- Solana (`SOL-USD`)
- Binance Coin (`BNB-USD`)
- Ripple (`XRP-USD`)

---

## 🧩 Project Structure


---

## 📈 How the Prediction Works

1. **Download** historical price data (Open, High, Low, Close, Volume)
2. **Generate Features**:
   - Daily Returns
   - Volatility (5-day rolling standard deviation)
   - Momentum (5-day price difference)
3. **Train Linear Regression Models**
4. **Forecast** closing prices for:
   - 1 Day Ahead
   - 7 Days Ahead
   - 30 Days Ahead
   - 365 Days Ahead

---

## 🛠 Next Goals

🔄 Upgrade ML Models:
- 🪵 Random Forest
- ⚡ XGBoost
- 🧠 LSTM (Deep Learning)

📊 Add Features:
- Technical Indicators: MACD, RSI, Bollinger Bands
- Interactive Dashboards / Charts
- Strategy Backtesting Tools

---

## 💡 Why Use This?

Whether you're a:

- 📚 **Data science learner**
- 📉📈 **Stock or crypto enthusiast**
- 🤖 **Quant trader or ML hobbyist**

This project offers a powerful and educational foundation for exploring real-world **financial forecasting** using Machine Learning.

---

## 📬 Contributions Welcome!

Fork it. Tweak it. Extend it.  
Contributions of all kinds are welcome — from bug fixes and documentation to feature improvements and model upgrades.

---

## 📄 License

This project is licensed under the MIT License.
