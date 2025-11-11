# print('\n') 

# import requests
# import plotly.express as px

# # =============================================== 
# # Make an API call and check the response for all the info. 
# # Output into a graph
# # Interact with the graph using hover text for more info

# url = "https://api.github.com/search/repositories"
# url += "?q=language:python+sort:stars+stars:>10000"

# headers = {"Accept": 'application/vnd.github.v3.json'}
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}") #the 200 means succesfull connection, like 404 means nope 

# # Process overall results
# response_dict = r.json()
# print(f"Complete results: {not response_dict['incomplete_results']}")

# # Process repository information.
# repo_dicts = response_dict['items']
# repo_names, stars, hover_texts = [], [], []
# for repo_dict in repo_dicts:
#     repo_names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])

#     # Build hover texts. 
#     owner = repo_dict['owner']['login']
#     description = repo_dict['description']
#     hover_text = f'{owner}<br />{description}' #we are adding a break 
#     hover_texts.append(hover_text)


# # Make visualization.
# title = "Most-Starred Python Projects on GitHub"
# labels = {'x': 'Repository', 'y': 'Stars'}
# fig = px.bar(x=repo_names, y=stars, title=title, labels=labels, hover_name=hover_texts)

# fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

# fig.show()


#======================= adding clickable links to the graph 

print('\n') 

import requests
import plotly.express as px

# Make an API call and check the response 

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": 'application/vnd.github.v3.json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}") #the 200 means succesfull connection, like 404 means nope 

# Process overall results
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repository information.
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    #Turn repo names into active links
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)


    stars.append(repo_dict['stargazers_count'])

    # Build hover texts. 
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f'{owner}<br />{description}' #we are adding a break 
    hover_texts.append(hover_text)


# Make visualization.
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)

fig.show()


#====================== ChatGPT summary 

# Most-Starred Python Repositories Visualization Summary

# Imports & Setup:
# Uses requests to fetch data from the GitHub API and plotly.express to visualize it interactively.

# API Call:
# Sends a request to GitHub’s search API for repositories written in Python with over 10,000 stars, sorted by star count.
#   Checks the status code (200 = success).
#   Converts the JSON response into a Python dictionary.

# Data Extraction:
# From the API results ('items'), it gathers:
#   Repository names (turned into clickable HTML links)
#   Star counts
#    Hover text combining the repo owner and its description

# Visualization:
#   Creates an interactive bar chart with Plotly Express:
#   X-axis: repository names (clickable links)
#   Y-axis: star counts
#   Hover info: repo owner + description
#   Custom layout and a soft SteelBlue color scheme for bars

# Purpose:
# To display the most popular Python projects on GitHub in a visually engaging, interactive chart with hover details and clickable links.