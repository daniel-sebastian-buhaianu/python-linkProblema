import sys
import requests
from bs4 import BeautifulSoup

def linkProblema(numeProblema):
  url = "http://campion.edu.ro/arhiva/index.php?page=search&action=searched&filtercriteria=all&query=" + numeProblema + "&x=0&y=0&overall_all=yes&problems_keyword=yes&papers_keyword=yes&seds_keyword=yes&locations_name=yes&authors_first_name=yes&teachers_first_name=yes&competitors_first_name=yes&problems_name=yes&papers_name=yes&seds_name=yes&locations_year=yes&authors_last_name=yes&teachers_last_name=yes&competitors_last_name=yes&problems_author=yes&papers_author=yes&seds_author=yes&competitors_school=yes&problems_teacher=yes&papers_teacher=yes&seds_teacher=yes&competitors_city=yes"
  response = requests.get(url);
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    atag = soup.find('a', string=numeProblema)
    if atag and atag.has_attr("href"):
      return "https://campion.edu.ro/arhiva/" + atag.get("href")
  return None

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Folosire: python link.py [numeProblema]")
    sys.exit(1)
  link = linkProblema(sys.argv[1])
  if link is None:
    print("Din pacate ceva nu a functionat, te rog sa incerci din nou.")
  else:
    print(link)

