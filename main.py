import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "D4T1DV37ZYG2JEG3"
NEWS_API_KEY = "cd31363c0b034402a834a9932e197d03"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


day_before_yesterday_data = data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_data_closing_price)

abs_difference = abs(difference)


diff_percent = (abs_difference / float(yesterday_closing_price)) * 100

# print(diff_percent)

if diff_percent > 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }


    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    if difference > 0:
        print(f"{STOCK_NAME}: 🔺{round(diff_percent, 2)}%")
    else:
        print(f"{STOCK_NAME}: 🔻{round(diff_percent, 2)}%")

    for article in formatted_articles:
        print(article)
        print()





