import requests
from twilio.rest import Client

TWILIO_SID = "ENTER_SID"
TWILIO_TOKEN = "ENTER_TOKEN"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

NOTIFY_RATE = 5.00

STOCKS_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://api.newscatcherapi.com/v2/search"

# STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STOCKS_API_KEY = "ENTER_API_KEY"
# NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_KEY = "ENTER_API_KEY"

STOCKS_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCKS_API_KEY,
}

NEWS_PARAMS = {
    "q": COMPANY_NAME,
    "lang": "en",
    "search_in": "title",
    "countries": "us",
    "topic": "business",
    "ranked_only": True,
    "from_rank": 100,
    "sort_by": "date",
    "from": "2023-07-18",
    "to": "2023-07-20",
}

NEWS_HEADERS = {
    "x-api-key": NEWS_API_KEY,
}

stocks_response = requests.get(STOCKS_ENDPOINT, params=STOCKS_PARAMS)
stocks_response.raise_for_status()
stocks_data = stocks_response.json()["Time Series (Daily)"]
# print(stocks_data)

daily_stocks_data = [value for (key, value) in stocks_data.items()]
new_price = float(daily_stocks_data[0]["4. close"])
old_price = float(daily_stocks_data[1]["4. close"])

price_change = new_price - old_price
price_up_down = None
if price_change > 0:
    price_up_down = "📈"
else:
    price_up_down = "📉"
percentage_change = round(price_change / new_price * 100, 3)

print(
    f"${new_price}, ${old_price}, ${price_change}, {price_up_down} {percentage_change}%"
)

if abs(percentage_change > NOTIFY_RATE):
    news_response = requests.get(
        NEWS_ENDPOINT, headers=NEWS_HEADERS, params=NEWS_PARAMS
    )
    news_response.raise_for_status()
    news_articles = news_response.json()

    recent_news = news_articles["articles"][:3]

    formatted_articles = [
        f"{STOCK_NAME}:  {price_up_down} {percentage_change}%\nHeadline: {article['title']}. "
        f"\nSummary: {article['summary']}.\n"
        for article in recent_news
    ]

    client = Client(TWILIO_SID, TWILIO_TOKEN)

else:
    print(f"{STOCK_NAME} stock changed by: {percentage_change}% {price_up_down}")
