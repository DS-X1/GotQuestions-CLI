import os

import requests
from bs4 import BeautifulSoup


def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def loadArticle(url):
  try:
    response = requests.get(url)
    
    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, "html.parser")
  
    # Extract the title
    title = soup.find("span",itemprop="name headline").text.strip()
    rawArticleBody = soup.find("div",itemprop= "articleBody").text.strip()
    rawArticleBody = rawArticleBody[8:] # Removes "Answer" word from result
    articleBody = rawArticleBody.replace("\n", "\n\n ")
    
    return title, articleBody
  except Exception as e:
    clear()
    title = "An error occured when loading the URL"
    articleBody = e
    return title, articleBody
    

def search(query):
  url = "https://www.gotquestions.org/search.php?zoom_sort=0&zoom_query=" + query
  response = requests.get(url)
  
  # Create a BeautifulSoup object
  soup = BeautifulSoup(response.content, "html.parser")

  # Extract the search results
  rawResults = soup.find("div",class_="results").text.strip()

  query_titles = []
  query_urls = []
  
  for line in rawResults.split("\n"):
    if line.startswith("URL:"):
      query_urls.append(line[5:].strip())
    elif line.endswith("GotQuestions.org"):
      seperator_index = line.find("|")
      query_titles.append(line[:seperator_index].strip().replace("\xa0"," "))
  
  return query_titles, query_urls

def loadTop20(filter):
  url = "https://www.gotquestions.org/" + filter

  response = requests.get(url)
  soup = BeautifulSoup(response.content,"html.parser")

  rawResults = soup.find("div",class_="content")

  # Get Top20 Titles
  rawResults_txt = soup.find("div",class_="content").text.strip()

  first_char_index = rawResults_txt.find("1.")
  last_char_index = rawResults_txt.find("\n\n")
  top20_titles = rawResults_txt[first_char_index:last_char_index].split("\n")

  # Get Top20 URLs
  strong_tags = rawResults.find('strong')
  links = strong_tags.find_all('a')
  top20_urls = [i['href'] for i in links]

  return top20_titles, top20_urls

def formatArticle(title,body):
  clear()
  print("Title: ",title, "\n\n", body)
  input("\n (Press Enter to continue...)")

def loadTop20Filter(url,increment=0):
  top20_titles, top20_urls = loadTop20(url)

  for title in top20_titles:
    print(title)

  title_index = int(input("\nNumber of article: "))
  url = "https://gotquestions.org/" + top20_urls[title_index+increment]
  articleTitle, articleBodyText = loadArticle(url)
  formatArticle(articleTitle,articleBodyText)
