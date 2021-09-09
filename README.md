# Fampay-yt |Backend Assignment|

API to fetch the latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

**Requirements**
```
asgiref     3.4.1
Django      3.2.7
pip         21.2.4
pytz        2021.1
setuptools  57.4.0
sqlparse    0.4.1
wheel       0.37.0
```

**Use Case Diagram (UML)**
![Fam-yt (1)](https://user-images.githubusercontent.com/40488679/132178804-934d5074-b8e8-4e50-9ff3-a25f5b3bf3a3.png)



**Setup**

1. Clone/pull/download this repository

2. Change into project directory
cd <project_name>

3. Make virtual environment
mkvirtualenv <project_name>

4. Activate virtual environment
workon <project_name>

5. Install requirements
pip install -r requirements.txt

6. Setup (if necessary)
fab loc setup

7. Start the development server
python manage.py runserver


**Reference**

- YouTube data v3 API: [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)

- Search API reference: [https://developers.google.com/youtube/v3/docs/search/list](https://developers.google.com/youtube/v3/docs/search/list)
    - To fetch the latest videos you need to specify these: type=video, order=date, publishedAfter=<SOME_DATE_TIME>
    - Without publishedAfter, it will give you cached results which will be too old
