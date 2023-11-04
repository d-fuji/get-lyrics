import requests, bs4

url = 'https://genius.com/Gi-dle-latata-lyrics'

def getLyric(url):
  res = requests.get(url)
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  lyrics = soup.find_all(attrs={'data-lyrics-container':'true'})

  result = ""
  for lyric in lyrics:
    result += lyric.text

  return result

lyric = getLyric(url)
lyric_list = lyric.replace('[', '*[').replace(']', ']*').split('*')

print(*lyric_list, sep='\n')
