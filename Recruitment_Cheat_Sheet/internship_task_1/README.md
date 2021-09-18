# Backend task
 
Api: http://www.omdbapi.com
CSV File: movies.csv
Database: movies.sqlite
 
The task consists of writing a script that fills example data source with data from OMDb API.
Given data source contains only titles of movies.
You need to chose one data source and populate empty columns in it.
You need to generate your own API key here http://www.omdbapi.com/apikey.aspx
 
Command line interface of your program should be capable of:
 
1) Sorting Movies by every column (bonus points for sorting by multiple columns)
 
Example input:
 
python movies.py --sort_by year
 
Example output:
 
|Title | Year|
|-----------|:-----------:|
|Boyhood         |2014|
|Seven Pounds|    2008|
|In Bruges    |  2008|
|Memento   |      2000|
 
2) Filtering by:
- Director
- Actor
- Movies that was nominated  for Oscar but did not win any.
- Movies that won more than 80% of nominations
- Movies that earned more than 100,000,000 $
- Only movies in certain Language
 
Example input:
 
python movies.py --filter_by language spanish

Example output:
 
|Title | Language|
|-----------|:-----------:|
| Seven Pounds  |English, Spanish  |
| Contratiempo  | Spanish |
| Vicky Cristina Barcelona   |English, Spanish  |

Title                       Languages  
Seven Pounds                English, Spanish  
Contratiempo                Spanish  
Vicky Cristina Barcelona    English, Spanish  
 
3) Comparing by:
- IMDb Rating
- Box office earnings
- Number of awards won
- Runtime
 
Example input:
 
python movies.py --compare runtime "Seven Pounds" "Memento"
 
Example output:
 
|Title | Runtime|
|-----------|:-----------:|
| Seven Pounds  |2h3m|
 
4) Adding movies to data source
 
python movies.py --add "Kac Wawa"
 
5) Showing current highscores in :
- Runtime
- Box office earnings
- Most awards won
- Most nominations
- Most Oscars
- Highest IMDB Rating
 
Example Input:
 
python movies.py --highscores

Example Output:

| Column | Movie | Value |  
|-----------|:-----------:|-----------:|
|Runtime   |  Lawrence Of Arabia     |     3h28m  |
|Box Office | Avengers:Endgame       |     $2,797.8  |
|Awards Won  |Boyhood                 |    171  |
|Nominations| Boyhood                  |   209  |
|Oscars      |Ben Hur                   |  11  |
|IMDB Rating |The Shawshank Redemption  |  9.3  |

 
Requirements:
- Python 3.7 +
- Object Oriented Programming
- Readme describing available commands.
- Unit Tests
 
Bonus Points for:
- Multithreading
- SQLite
- pytest
 
FAQ:
 
Available Third Party Packages:
- requests
- pytest
