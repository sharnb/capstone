# Korean Drama Recommender System
>Author: Sharnique Beck

## Problem Statement

<p>There are hundreds if not thousands of great Korean tv series out there and I think everyone should experience at least one of them. I often find myself wondering which show to watch next and I also have many friends that look to me to recommend their next show to watch. After suggesting what I thought was a great show to a good friend, disaster struck... My friend hated (I dont use this word lightly) the show, did not finish the series, and would not accept a recommendation from me for YEARS to come. 
After this intense experience I was more hesitant on recommending anything until flash foward to General Assembly and Recommender Systems...</p>
<p>A great way to take pressure off of myself and give the people what they want would be to build a korean drama, user based recommender system. This system will be based on how users of a popular streaming website Viki.com rate shows and how the show ratings compare to each other.</p>
## Directory:
<ul>
<li> <strong>data:</strong>This folder contains a number of csvs collected and saved during the whole process, the main csvs for my current recommender are:<ul><li><strong>k_titles.csv</strong>: data set of show titles collected</li><li><strong>ratings_data</strong>: data set of the user rating collected</li></ul></li>
<li> <strong>notebook:</strong></li>
<ul>
<li><strong>01_show_scraper</strong>: In this notebook I perform my two main scrapes to collect show titles and user ratings</li>
<li><strong>02_Rating_Stats</strong>: This notebook looks at the show stats, such as number of shows, users, ratings, ratings per show.</li>
<li><strong>03_Recommender</strong>: This notebook is where I build the recommender system</li>
<li><strong>04_Content scraper</strong>: This notebook is where I scrape show content (title, director, writer, cast, user average rating, network, genre, # episodes) from viki.com and asianwiki.com for my content based recommender</li>
<li><strong>05_Visuals</strong>: This notebook is where I create visuals of the data I've collected for analysis.
</ul>
<li> <strong>images</strong>: Images used in technical report</li>
</ul>
## Data Dictionary
Information for data sets used in current recommender.

|variable|type|data|Description|
| --- | ---|---| --- |
|title| string|ratings_data / k\_title| Name of the show being rated|
|rating| float|k_title| Average user rating for the show |
|rating| int | ratings_data| Individual user rating for show.|
|user|string| ratings_data| User Name of individual writing show review.|
|user_id|int| ratings_dat| Unique Id number assigned to each user.|