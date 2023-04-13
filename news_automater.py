import requests


# Go to https://newsapi.org and create an account
# Then paste given API key inside below double quotes and run the program

API_KEY = ""

URL = ('https://newsapi.org/v2/top-headlines?')

def get_articles_by_category(category):
	query_params = {
	"category": category,
	"sortBy":"top",
	"country":"us",
	"apiKey":API_KEY
	}
	return _get_articles(query_params)

def get_articles_by_query(query):
    query_params = {
	"q`": query,
	"sortBy":"top",
	"country":"us",
	"apiKey":API_KEY
	}
    return _get_articles(query_params)

def _get_articles(params):
	response = requests.get(URL, params=params)
	articles = response.json()['articles']
	print(articles)
	print('hel no')
	results = []
	for article in articles:
		results.append({"title":article['title'], "url":article["url"]})
	for result in results:
		print(result['title'])
		print(result['url'])
		print('\n')



if __name__ == "__main__":
	print(f"Getting news")
	# get_articles_by_query("Donald Trumpt")
	get_articles_by_category("science")
