print('\n') 

from operator import itemgetter

import requests


# Make an API call and check the response. 
url = "https://hacker-news.firebaseio.com/v0/topstories.json" #this is where we are getting the submission ID's
r = requests.get(url) #this is taking the url infomation and adding it to the var r 
print(f"Status code: {r.status_code}") #200 is the code it will give for successfull connection

# Process info about each submission 
submission_ids = r.json() #by it being a json string, we can now read the info on this 

submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission 
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json" #submission ID is the data we got from line 9 url
    r = requests.get(url) 
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = { #this is the info we want to grab from the url
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants']
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True) #no clue

for submission_dict in submission_dicts: #this is outputting the info we grabbed from the url
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

print('\n')


# =========================== ChatGPT summary 

# Chat GPT Summary 
# It imports the necessary modules — one for making web requests and another for sorting data easily.
# It connects to the Hacker News API to get a list of the current top story IDs.
# It loops through the first five stories, and for each one, it makes another request to get detailed information like the title and number of comments.
# It extracts only the useful information (title, discussion link, and comment count) and stores these in a list of dictionaries.
# It sorts the stories so that the ones with the most comments appear first.
# It prints out the results, showing each story’s title, the link to its discussion page on Hacker News, and the number of comments it has.
# In short: the script fetches the top five Hacker News stories, sorts them by popularity, and displays their key details neatly.