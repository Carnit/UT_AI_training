# Financial analysis agent example
import os
import sys
from textwrap import dedent
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools


def main():
    load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        print("Error: GOOGLE_API_KEY not found in .env file.")
        sys.exit(1)

    finance_agent = Agent(
        model=Gemini(id="gemini-1.5-flash", api_key=google_api_key),
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                stock_fundamentals=True,
                historical_prices=True,
                company_info=True,
                company_news=True,
            )
        ],
        instructions=dedent("""\
            You are a seasoned Wall Street analyst providing institutional-grade research for sophisticated investors. Your analysis must be rigorous, objective, and data-driven. Your goal is to produce a comprehensive investment research report.

            **Report Structure:**

            1.  **Executive Summary:**
                *   Start with a clear investment thesis (e.g., "BUY: Undervalued leader in a growing market").
                *   Provide 3-4 bullet points summarizing the core arguments.

            2.  **Company Overview:**
                *   Briefly describe the company's business, primary products/services, and its position in the market.

            3.  **Financial Analysis:**
                *   **Key Metrics:** Present vital statistics like Market Cap, P/E Ratio, P/S Ratio, and Dividend Yield.
                *   **Performance:** Analyze recent revenue and earnings performance. Is it accelerating or decelerating?
                *   **Health:** Comment on the balance sheet, particularly debt levels.

            4.  **Competitive Landscape & Industry Trends:**
                *   Who are the main competitors? How does the company stack up against them?
                *   What are the key trends affecting the industry? (e.g., technological shifts, regulatory changes).

            5.  **Analyst Consensus & Recent News:**
                *   Summarize the consensus from professional analysts. Provide the breakdown of Buy/Hold/Sell ratings if available.
                *   Highlight any major recent news and explain its potential impact on the company's outlook.

            6.  **Outlook & Valuation:**
                *   Provide a forward-looking statement on the company's prospects.
                *   Identify key catalysts that could drive the stock price up and risks that could drive it down.
                *   Comment on whether the stock appears overvalued, fairly valued, or undervalued based on the data.

            **Tone and Style:**
            -   **Professional & Objective:** Maintain a formal tone. Avoid hype and emotional language.
            -   **Quantitative:** Your claims must be supported by financial data and metrics from your tools.
            -   **Structured:** Use Markdown for clear headings, subheadings, and bullet points to ensure readability.
            -   **No Code Generation:** Your entire response must be a natural language report. Do NOT write or suggest any code. If data is unavailable from your tools, state that and continue the analysis with the information you have.

            **Disclaimer:**
            -   Conclude every report with a standard disclaimer: "This report is for informational purposes only and does not constitute financial or investment advice. Please conduct your own research before making any investment decisions."
        """),
        add_datetime_to_instructions=True,
        show_tool_calls=True,
        markdown=True,
    )

    print("\n--- Generating Semiconductor Market Analysis ---\n")
    finance_agent.print_response(
        dedent("""\
        Analyze the semiconductor market performance focusing on:
        - NVIDIA (NVDA)
        - AMD (AMD)
        - Intel (INTC)
        - Taiwan Semiconductor (TSM)
        - Qualcomm (QCOM)
        - Broadcom (AVGO)
        - Micron Technology (MU)
        - Texas Instruments (TXN)
        - Samsung Electronics (SSNLF)
        Provide insights on their recent earnings, market trends, and competitive landscape.
        Include their latest earnings reports, market trends, and competitive landscape.
        Compare their market positions, growth metrics, and future outlook."""),
        stream=True,
    )

    print("\n--- Generating Automotive Market Analysis ---\n")
    finance_agent.print_response(
        dedent("""\
        Evaluate the automotive industry's current state:
        - Tesla (TSLA)
        - Ford (F)
        - General Motors (GM)
        - Toyota (TM)
        - Volkswagen (VWAGY)
        - Honda (HMC)
        - BMW (BMWYY)
        - Mercedes-Benz (MBGYY)
        - Audi (AUDVF)
        - Porsche (POAHF)
        - Koenigsegg (KNSGF)
        - Ferrari NV (RACE)
        Focus on their market shares, EV transition progress, and traditional auto metrics.
        Include EV transition progress and traditional auto metrics."""),
        stream=True,
    )


if __name__ == "__main__":
    main()
