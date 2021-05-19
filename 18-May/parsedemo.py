import bs4

f = open("example.html")
soup = bs4.BeautifulSoup(f)
lis= soup.find_all("li", {"class" : "x"})
for i in lis:
    print (i)


f.close()
