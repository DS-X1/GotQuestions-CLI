import sys

import gq

# Main loop
while True:
  gq.clear()
  print("== GotQuestions CLI Client == \n")
  
  print("""
       [1] Search for question
       [2] Load article from URL
       [3] Top 20 Questions
       [4] About
       [5] Exit \n""")
  
  choice = input("Enter a number to select from the menu: ")

  if choice == "1":
    gq.clear()
    query = input("Enter topic or query: ")

    #Check if search is empty or not
    if query:
      gq.clear()
      query_titles, query_urls = gq.search(query)
    else:
      continue

    print("== Search Results ==")
    
    # Print titles of search results
    for title in query_titles:
      print(title)

    title_index = int(input("Number of the article you want to read (0 to go back): "))

    # Check if input is 0 (to go back) or if it is outside the available number of titles
    if title_index == 0 or title_index not in range(1,len(query_titles)+1):
      continue
    else:
      url = query_urls[title_index-1]
      articleTitle, articleBodyText = gq.loadArticle(url)
      gq.formatArticle(articleTitle,articleBodyText)

  # Simply load a GotQuestions URL
  elif choice == "2":
    gq.clear()
    url = input("Enter the URL of the article: ")
    articleTitle, articleBodyText = gq.loadArticle(url)
    gq.formatArticle(articleTitle,articleBodyText)
    
  # Check out the frequently visited articles on GotQuestions
  elif choice == "3":
    gq.clear()
    print("""== Frequently visited articles == 
    
              [1] Top 20
              [2] Top 20 Monthly
              [3] Top 20 All-Time \n""")
    filter = input("> ")

    # Article loading gets a list of titles, then a separate one for URLs
    # The titles list is for visual purposes, simply to show the user search results
    # The actual URLs are stored in a separate URL list
    # Ideally, when you access index 1, it should give title #1 and URL #1 so they match
    # However, when accessing index 1, it accesses index1 of titles but probably index3 of URLs
    # So, I found the difference between the titles and URLs that each option below has
    # Then, add that deficit to fix it. That's what "increment" is for
    if filter == "1":
      gq.loadTop20Filter("top20.html",increment=1)
    elif filter == "2":
      gq.loadTop20Filter("top20-monthly.html",increment=-1)
    elif filter == "3":
      gq.loadTop20Filter("top20-all-time.html",increment=-1)
    else:
      continue
  # Credits
  elif choice == "4":
    gq.clear()
    print("Thanks for using this! All thanks and glory to Jesus that this was made. :)")
    input("\n ....")
    continue

  # Exit program
  elif choice == "5":
    
    sys.exit()

  else:
    continue
