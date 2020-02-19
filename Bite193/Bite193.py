import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    questions = soup.find_all('div', {'class': 'question-summary'})
    result = []
    filtered_result = []
    for q in questions:
        try:
            result.append((int(q.find('div', {'class': 'votes'}).span.find('strong').text),
                           q.find('a', {'class': 'question-hyperlink'}).text,
                           q.find('div', {'class': 'views supernova'}).text.strip('\r\n').strip()
                           ))
        except AttributeError:
            pass

    for r in result:
        if 'm views' in r[2]:
            filtered_result.append((r[1], r[0]))

    filtered_result = sorted(filtered_result, key=lambda x: x[1], reverse=True)

    return filtered_result

t = top_python_questions(cached_so_url)
print(t)