from bs4 import BeautifulSoup

html = open("index.html", "r")
file = html.read()

s = BeautifulSoup(file, 'html.parser')
tables = s.findChildren('table')

table = tables[0]
rows = table.findChildren(['tr'])

grades = open('grades.csv', 'w+')

for i in range(1, len(rows)):
    kid = ''
    stars = 0
    cols = rows[i].findChildren('td')
    for i in range(0, len(cols)):
            if i == 0:
                kid += cols[i].text.strip() + ','
            if i == 1:
                kid += cols[i].text.strip() + ','
            if i == 2:
                game = cols[i].text.strip()
                pos = game.find('-')
                kid += game[pos+2:len(game)] +','
            if i == 3:
                kid += cols[i].text.strip() + ','
            if i == 4:
                kid += cols[i].text.strip() + ','
            if i == 5:
                    if cols[i].findAll('i',{'class':'fa fa-star'}):
                        stars = len(cols[i].findAll('i',{'class':'fa fa-star'}))
                        kid += str(stars) + ','  
                    else:
                         kid += cols[i].text.strip() + ','
            if i == 6:
                kid += cols[i].text.strip()
            
    grades.write(kid + '\n')



    #grades.write(kid + '\n')


#print(rows[10])
#stars = rows[10].findAll('i',{'class':'fa fa-star'})

#print(len(stars))