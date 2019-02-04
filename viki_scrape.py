import pandas as pd
import requests
import time
from bs4 import BeautifulSoup

headers = {'User-agent': 'Sharnb 1.0'}

k_titles = pd.read_csv('./data/k_titles.csv')

ratings = []
shows_comp= 0 # count of the number of shows completed

# Loop through each show
for s_row in range(len(k_titles['container'])):

    pg_nums =1
    
    # Loop through each review page 
    while True:
        url1='https://api.viki.io/v4/containers/%s/reviews.json?sort=review_rank&direction=desc&per_page=10&page=%s&app=100000a' %(k_titles['container'][s_row], pg_nums)
        res = requests.get(url1, headers= headers)
        json_pg = res.json()
        
        next_pg = json_pg['more']    # indicates if there is another page of reviews
        
        # Break loop if show has no reviews
        if pg_nums ==1 and json_pg['response'] == []:
            print("%s has no reviews" %(k_titles['title'][s_row]))
            shows_comp+=1
            break
        
        # Break loop after last page of reviews
        if next_pg != True and json_pg['response'] == []:
            shows_comp+=1
            print('%s shows completed' %shows_comp)
            break
            
        # Loop through each user review on review pg
        for row in json_pg['response']:
            rating = {}
            rating['title'] = k_titles['title'][s_row]
            rating['user'] = row['user']['username']
            rating['rating'] = row['user_content_rating']
            ratings.append(rating)
            
        pg_nums += 1
        
        time.sleep(1)
        
    time.sleep(2)
    
    # save data to csv after every 10 shows
    if shows_comp % 10 == 0:
        show_rates = pd.DataFrame(ratings)
        show_rates.to_csv('./data/ratings2.csv', index=False)

# save entire data set to csv after scraping all shows is complete
show_rates = pd.DataFrame(ratings)
show_rates.to_csv('./data/k_ratings_total.csv', index=False)
