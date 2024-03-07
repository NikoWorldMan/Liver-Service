# CODE!!!!!

Velkommen til min **dokumentasjon.**

Imports:
Note: Not all imports will be used but in my current code. 
However they can be used to build upon it further.
```python
import requests

from bs4 import BeautifulSoup


#other
import json

import pandas as pd
```

___

Step 1 the quest for request
```python
#requests makes a request for the webpage's Html and turns it into text

html_text = requests.get("https://store.steampowered.com/search/?supportedlang=norwegian%2Cenglish&specials=1&hidef2p=1&ndl=1")
```

___

PLACEHOLDER
```python
#requests makes a request for the webpage's Html and turns it into text

soup = BeautifulSoup(html_text, 'lxml')



#from the html that BeautifulSoup shoved into the lxml's library

games = soup.find_all('a', class_ = 'search_result_row ds_collapse_flag')
```

PLACEHOLDER
```python
#prints the html that was found from games

print(games)
```
