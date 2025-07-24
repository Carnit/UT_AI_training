# Financial Analysis Agent

This project showcases a sophisticated financial analysis agent built using the `agno` library, Google's Gemini model, and Yahoo Finance data. The agent is configured to act as a financial news reporter, delivering insightful and easy-to-read reports on various companies and market sectors.

## 🚀 Features

- **AI-Powered Analysis**: Leverages the power of Google's Gemini model for deep analysis and natural language report generation.
- **Real-time Financial Data**: Integrates `YFinanceTools` to fetch up-to-the-minute stock prices, company fundamentals, analyst recommendations, and news.
- **Engaging Report Format**: Generates reports in a news-style format, complete with headlines, TL;DR summaries, and expert commentary.
- **Customizable Persona**: The agent's personality and reporting style can be easily modified by changing the instructions in `app.py`.
- **Market Comparison**: Capable of analyzing and comparing multiple stocks within a specific sector (e.g., Semiconductors, Automotive).
- **Streaming Output**: Delivers analysis in a real-time stream for a more interactive experience.

## 🛠️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

- Python 3.8 or higher (I am using Python 3.13)
- A Google API key. You can get one from [Google AI Studio](https://aistudio.google.com/).

### 2. Project Setup

It's recommended to use a virtual environment to manage project dependencies.

```bash
# Navigate to the project directory
cd path/to/agno_project

# Create a virtual environment
python -m venv venv
```

or

```bash
uv init 
uv venv
```

```bash
# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

or

```bash
uv sync
# or
uv pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a file named `.env` in the `agno_project` directory and add your Google API key:

```env
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
```

## ▶️ How to Run

Once the setup is complete, you can run the agent directly from your terminal:

```bash
python app.py
```

The script will automatically execute two pre-configured analyses:

1. A deep dive into the semiconductor market.
2. An evaluation of the automotive industry.

The reports will be printed to your console in markdown format.

## 🔧 Customization

You can easily customize the analysis by modifying the `app.py` file.

### Analyze Different Stocks

To analyze different companies or sectors, simply change the text inside the `finance_agent.print_response()` calls at the bottom of the script.

like :

Evaluate the automotive industry's current state:

- Tesla (TSLA)
- Ford (F)
- General Motors (GM)
- Toyota (TM)
- Volkswagen (VWAGY)
- Honda (HMC)
Focus on their market shares, EV transition progress, and traditional auto metrics.
Include EV transition progress and traditional auto metrics.
