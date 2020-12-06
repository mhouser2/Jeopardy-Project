# Jeopardy-Project
Data scraping, cleaning, and analysis of over 250,000 Jeopardy questions in over 4000 games

## Scraping
I used the Scrapy python package to scrape 4,280 games (all regularly formatted games since point values were doubled) of Jeopardy from http://www.j-archive.com/. The scripts for these spiders are found in the Scrapy folder.
Since I am new to web scraping, I used four different spiders and different Scrapy methods to scrape all the necessary data. 

Every game on the j-archive.com is organized into a questions and responses page. It is possible to see the correct response from questions page, but that requires mousing over the clue, which is not so easy to program, so instead I scraped both pages together. 

The primary spider is Clues_Spider.py, which scraped the game id, clue value, clue order number, clue id, and clue from the game's question page, and then clue responses from the game's responses page. This data is organized in a weird way, in that each line of the JSON file is a separate game, and the entries are lists. While an odd format, what's most important is that it works and is consistent.

Responses_Spider.py is also an odd spider, in that it first scrapes the game's question page to find the responses page and then records the game id, correct response, value, order_number, and the contestants that answered right and wrong. We first scrape the question page because that allows us to find a link to the next game, which does not exist on the responses page.

Game_Summaries_Spider.py scrapes summary information from each game, such as the contestants names, biographies, the returning champion's winning streak and winnings, as well as each contestant's scores after the Jeopardy and Double Jeopardy rounds, and their final scores.

Finally there is the Categories_Spider, which scrapes the categories from each game. 

## Cleaning
All the scraped data is found in categories.json, clues.json, games.json, and responses.json. Clues Cleaning.ipynb cleans clues.json, responses.json, and categories.json and merges them into clues.csv.

In order to clean clues.json, we first had to make sure every list in the JSON was of equal length, which meant multiplying the game_id list by the number of clues. We then had to check for tiebreakers. In non-tiebreaker games, every list is of equal length and pandas allows us to easily create a dataframe. However, when a game ends in a tiebreaker the value and order_number columns have a length one less than clues. In order to fix this, we create a function that tests if all lists are of equal length, and if they are not, we append "Tiebreaker" to the value and order_number lists. All in all, there are only 7 tiebreakers in our dataset.

After fixing this, we use a for loop to create a dataframe from every line of the JSON, and then append the each dataframe to a base dataframe. We then take this dataframe of all games and add a show number, data, round (Jeopardy, Double Jeopardy, Final Jeopardy), row(1 through 5), and column (1 through 6, for categories) columns. 

We clean responses.json by creating columns for number of contestants that answered correctly, incorrectly, and didnt know. In order to merge this dataframe to our existing one, we had to create a value column in the existing dataframe that omitted the 'DD: ' found in daily doubles and also had to add 'tiebreaker' to the value and order_number columns in the responses dataframe. After this we merge both dataframes and end up adding the correct, incorrect columns which consists of strings of contestant names, and n_correct, n_incorrect and n_didnt_know of integers. 

Categories.json also took a lot of cleaning. Each category was stored in a list, so we first had to remove the list and then the '' surrounding each string. After this, we created a show number column, melted the data so instead of 13 columns of categories we had 1 column of all categories, and then modified the round and column columns so they could merge. 

After merging the categories to the main dataframe, we reorganized the column order so they made more sense, and then wrote the data to csv. 

We also cleaned games.json in Games Cleaning.ipynb, and we document the cleaning process there.

## Analysis

My analysis of this data involves a combination of understanding the history of Jeopardy contestants and preparation/practicing for Jeopardy. 

Contestants EDA explores the occuptions, locations, earning and winning streaks of returning Jeopardy champions. 

Clues and Categories EDA explores the most common correct responses and most common categories. Future work could involve NLP of the clues and broader categorization of correct responses.

Clue Probabilities.ipynb plots the probability that each clue is correctly answered by at least one contestant. We create heatmaps of the Jeopardy and Double Jeopardy rounds, as well as group this data column and row wise. Finally we look at the probability of answering Final Jeopardy correctly, which is approximately 50%, and look at the distribution of how many contestants correctly answer.

Coryat Scores.ipynb analyzes the coryat scores of each contestant. A coryat score is a player's score if all wagering is disregarded. What this allows is for us the rank episodes of Jeopardy but how well the contestants play. 

Expected Values.ipynb finds the expected value of each clue by round and by row, as well as the expected value of daily doubles by location.

Jeopardy Daily Doubles.ipynb creates a heatmap of the probability of the daily double's location for the Jeopardy and Double Jeopardy rounds. 

Jeopardy Practice.ipynb is a series of functions that give a random Jeopardy clue and records the number of correct responses, as well as the time it takes to respond per question. The function also allows you to filter the data by round (if you want just Final Jeopardy questions) or by category.

Time Series.ipynb plots the time series of player scores throughout the game. 




