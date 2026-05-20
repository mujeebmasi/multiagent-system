from langchain.tools import tool
import requests
from dotenv import load_dotenv
import os   
load_dotenv()
from bs4 import BeautifulSoup
from tavily import TavilyClient
from rich import print

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """Search the web for a query and return the results."""
    response = tavily.search(query,max_results=5)
    out = []
    for r in response['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content']}\n"
        )
    return "\n\n".join(out)
   
# print(web_search.invoke("May news about Y combinator"))

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        # Remove unwanted tags
        for tag in soup([
            "script","style","nav","footer","header","aside","noscript"
        ]):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)
        cleaned_text = " ".join(text.split())
        return cleaned_text[:5000]
    except requests.exceptions.RequestException as e:
        return f"Request error: {str(e)}"

    except Exception as e:
        return f"Could not scrape URL: {str(e)}"

res2 = scrape_url.invoke("https://news.ycombinator.com/news")
# print(res2)
