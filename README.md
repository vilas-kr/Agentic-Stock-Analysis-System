# 📈 AI-Powered Multi-Agent Trading Intelligence System

## Overview

AI Trading Assistant is a Multi-Agent AI system that analyzes stocks using market data, technical indicators, financial metrics, news sentiment, risk assessment, and recommendation engines.

The system combines multiple specialized AI agents to generate a comprehensive stock analysis report and investment recommendation.

## Features

### Stock Identification Agent

* Extracts stock/company names from user queries
* Resolves valid stock symbols

### Company Overview Agent

* Retrieves company profile
* Sector and industry information
* Business description

### Current Metrics Agent

* Current Price
* Market Capitalization
* PE Ratio
* EPS
* Dividend Yield
* Revenue Growth
* Profit Margin
* Debt-to-Equity Ratio

### Technical Analysis Agent

* RSI Analysis
* MACD Analysis
* Moving Averages (50 DMA, 200 DMA)
* Volume Trend
* Momentum Detection
* Bullish/Bearish/Neutral Trend Analysis

### News Analysis Agent

* Retrieves latest company news
* Identifies positive and negative news events
* Calculates overall news sentiment

### Sentiment Analysis Agent

* Evaluates:

  * Fundamentals
  * Technical Signals
  * News Sentiment
* Generates confidence scores

### Risk Analysis Agent

* Financial Risk
* Technical Risk
* News Risk
* Market Risk
* Overall Risk Score (0-10)

### Recommendation Agent

Generates:

* BUY
* HOLD
* SELL

Along with:

* Confidence Score
* Investment Horizon
* Key Reasons

## Architecture
## Multi-Agent Pipeline

```text
User Query
    │
    ▼
Stock Identification Agent
    │
    ▼
Ticker Resolution
    │
    ▼

┌───────────────────────────────┐
│ Parallel Analysis Stage       │
├───────────────────────────────┤
│ Company Overview              │
│ Current Metrics               │
│ Technical Analysis            │
│ News Analysis                 │
└───────────────────────────────┘

    │
    ▼
Sentiment Analysis
    │
    ▼
Risk Assessment
    │
    ▼
Investment Recommendation
    │
    ▼
Final AI Trading Report
```


## Tech Stack

### AI & LLM

* PydanticAI
* Groq
* Llama 3.3 70B Versatile

### Backend

* FastAPI
* Python

### Frontend

* Streamlit

### Financial Data

* Yahoo Finance (yfinance)

### Technical Indicators

* pandas-ta

### Data Models

* Pydantic

### Environment Management

* Python Virtual Environment
* python-dotenv


## Guardrails Implemented

### Agent-Level Guardrails

* Low temperature configuration
* Structured Pydantic outputs
* Schema validation
* No hallucinated financial values
* Restricted recommendation rules

### Frontend Guardrails

* User input validation
* Disclaimer acknowledgement
* API timeout handling
* Missing data validation
* Confidence score warnings
* Risk alerts
* Recommendation consistency checks

## Installation

Clone Repository

```bash
git clone https://github.com/vilas-kr/Agentic-Stock-Analysis-System.git
cd Agentic-Stock-Analysis-System
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Create .env File

```env
GROQ_API_KEY=your_groq_api_key
```


## Running Backend

```bash
uvicorn api.main:app --reload
```

Backend URL

```text
http://127.0.0.1:8000
```


## Running Frontend

```bash
streamlit run frontend.py
```

## Example Query

```text
Analyze TCS
```

```text
Should I buy Infosys?
```

```text
Give me a report on Reliance Industries
```


## Sample Output

* Company Overview
* Financial Metrics
* Technical Analysis
* News Analysis
* Sentiment Analysis
* Risk Assessment
* BUY/HOLD/SELL Recommendation


## Future Enhancements

* Multi-Stock Comparison
* Trading Strategy Generation
* Price Prediction Models


## Project Goals

* Automate stock research
* Reduce manual analysis effort
* Improve investment decision support
* Combine AI with financial analytics
* Demonstrate Multi-Agent AI architecture

## Author
```
Name: Vilas K R
GitHub: https://github.com/vilas-kr
```