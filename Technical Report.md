# Technical Report
>_Author: Sharnique Beck_ 

## Problem Statement

<p>There are hundreds if not thousands of great Korean tv series out there and I think everyone should experience at least one of them. I often find myself wondering which show to watch next and I also have many friends that look to me to recommend their next show to watch. After suggesting what I thought was a great show to a good friend, disaster struck... My friend hated (I dont use this word lightly) the show, did not finish the series, and would not accept a recommendation from me for YEARS to come. 
After this intense experience I was more hesitant on recommending anything until flash forward to General Assembly and Recommender Systems...</p>
<p>A great way to take pressure off of myself and give the people what they want would be to build a korean drama, user based recommender system. This system will be based on how users of a popular streaming website Viki.com rate shows and how the show ratings compare to each other.</p>

## Executive Summary
<p>I plan to create an item based collaborative recommender system, which will recommend the top 10 closest matching shows to the given title.
</p>
### The Data
The data was collected from a popular streaming website called [Viki.com](https://www.viki.com/) using a web scraper as well as the [Viki API](http://viki-org.github.io/) for 624 shows. There was a limitation to the data that I could collect because I did not have access to all user ratings for any given show, so I collected show ratings from users based on user reviews. On average about 30%-40% of users who rated a show also wrote a review for that show, this can be seen in the table below

| show | # ratings | # reviews <br> written | % ratings <br>with reviews |
| ----- | ----- | ----- | -----|
|show 1 | 7106| 2195| 30.9|
|show 2 | 1354| 516| 38.1|
|show 3 | 3683| 1545| 41.9|
|show 4 | 4850| 1818| 37.5|
|show 5 | 2123| 660| 31.1|

In addition to not being able to collect all of the user ratings there is a large descrepency between the number of shows each user rated as seen in the graph below. <br>
![Top users](https://github.com/sharnb/capstone/blob/master/images/Top50%20users.png)
<br>There are 183,650 users and 402,426 ratings collected from reviews, where more than 171,580 have written less than 6 show reviews.<br>
![show ratings](https://github.com/sharnb/capstone/blob/master/Capstone/images/Top50%20shows.png)<br>
As expected come shows are more popular than others and thus therefore more people watch and review these shows as seen above. The graph shows that of the top 50 shows most have between 2,000 and 3,000 reviews where as the top 5 shows have over 10,000 reviews.
### The Recommender System
I chose to start off building an item-based collaborative recommender system. I began by creating a pivot table which took in the titles as the index, the user Id's as the columns and the user ratings as the values. I then calculated the cosine similarities using pair wise distances to see how similarly users rated shows to one another. The table below shows the sparse matrix of the first 8 shows alphabetically compared to each other. In this matrix shows are compared on a scale of 0 to 1 where the closer to zero the more similar two shows ratings are and thus highly recommended.<br>
![sparsematrix](https://github.com/sharnb/capstone/blob/master/Capstone/images/sparse%20matrix.png)<br>
### The Results
The Recommender is able to search for a show given the full or partial title. The system then prints out the show information including: the title, average rating, and number of ratings. I then recommends the top 10 shows similarly rated by users.
<br>
**************
![Results](https://github.com/sharnb/capstone/blob/master/Capstone/images/Results.png)
**************
<br>
As a search term I put in the first k-drama I ever saw and the 1st show that was recommended was actually the second show I watched because of the first one. Also at least 4 of the shows recommended were the next shows I watched. Thus I think the recommender worked out well.

# Summary
The recommender system I built works well with the data available. Given the limitation of data collected I don't think it works as well as it could. I hope to build a hybrid system that is both item and content based recommenders so that I can recommend shows tailored to a users preferences.
I'm also looking into serendipity recommenders, that based on my preferences would  recommend a show that I would not normally consider watching.

## References
Websites scraped for information:

* viki.com
* http://asianwiki.com/index.php
* https://mydramalist.com/
* https://wiki.d-addicts.com
