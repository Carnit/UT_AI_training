import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")

agent = Agent(
    model=Gemini(api_key=api_key),
    tools=[YFinanceTools(stock_price=True)],
    instructions="Use tables to display data. Don't include any other text.",
    markdown=True,
)
agent.print_response("What is the stock price of Apple?", stream=True)
