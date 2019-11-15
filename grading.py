import csv

filename = 'grades.csv'

studentGrades = dict()

studentGrades.setdefault('Sam Cohen', {})

whiteBeltGames = ['Breakdancer', 'Music, Music, Music!', 'Monster Encounter', 'Learning to Draw', 'Telling a Story', 
'Painting Your Own Sprites' , 'High or Low', 'Bounce Around', 'Attack of the Clones', 'Digital Pet', 'Dragon Racing',
'Space Ninjas', 'Platform Ninja', 'Coin Catch', 'Dojo Invaders', 'Pick a Picture', 'Crystal Ball', 'Collect the Keys', 'Fast Food'
,'Downhill Ski', 'Run and Jump', 'Apple Picking', 'Mail Truck']

yellowBeltGames = ['Getting Started', 'Spin a Star', 'Multiple Stars', 'Spin All Objects' 
, 'Spin Counter Clockwise', 'Spin the Scene', 'Coordinate Collector', 'Follow the Pointer'
, 'Star Spinner', 'ide Wall Bounce', 'Laser Beam Pointer', 'Basic Shooter', 'Rain Catcher Part 1'
, 'Pong', 'Rain Catcher Part 2', 'Basic Pong with Keyboard', 'Two Player Pong', 'Measurements'
, 'Ninja Puzzle', 'Space Shooter', 'Rain Catcher Part 3', 'Shooting Stars', 'Meteors Part 1'
, 'Rain Catcher Part 4', 'Meteors Part 2', 'Rain Catcher Part 5', 'Rain Catcher Part 6', 'Hiding Ninja'
, 'What a Ninja', 'Ninja Supplies', 'Bumper Car', 'Balloon Protect', 'Starscape', 'Zapper Part 1', 'Ninja Snacks'
, 'Shuriken Toss Part 1', 'Space Tour', 'Shuriken Toss Part 2', 'Ninja Battle', 'Zapper Part 2'
, 'Wall Blaster', 'Meteors Deluxe', 'Color Change', 'What\'s Inside', 'Lift Off', 'Rolling Dice'
, 'Rolling Dice', 'Bubbles', 'Robot Builder', 'Rock Paper Scissors', 'Bug Invaders', 'Candy Sort'
, 'Coconut Catch']

orangeBeltGames = ['Introduction', 'Dojo Invaders', 'Dojo Practice', 'Shuriken Dodge', 'Ninja Race'
, 'Ball Toss', 'Dungeon Escape', 'Scramble', 'Ninja Puzzle', 'Wall Blaster', 'Flying Ninja', 'Shut the Box'
, 'Code Breaker', 'Hangman', 'The Sky is Falling', 'Endless Run', 'War', 'Word Scramble', 'Server'
, 'Oddball', 'Circus Bounce', 'Tower of Hanoi']

whiteBeltGamesString = 'Student,'
yellowBeltGamesString = 'Student,'
orangeBeltGamesString = 'Student,'

for game in whiteBeltGames:
    if game == 'Music, Music, Music!':
        whiteBeltGamesString += 'Music Music Music!' +','
    else:
        whiteBeltGamesString += game + ','

for game in yellowBeltGames:
    yellowBeltGamesString += game + ','

for game in orangeBeltGames:
    orangeBeltGamesString += game + ','

with open('grades.csv', 'r') as readCSV:
    csvReader = csv.reader(readCSV)

    for row in csvReader:
        if row[0] in studentGrades:
            studentGrades[row[0]][row[2]] = row[5]               
        else:
            studentGrades[row[0]] = {}
            studentGrades[row[0]][row[2]] = row[5]

whiteBeltGrades = open('whiteBeltGames.csv', "w+")
whiteBeltGrades.write(whiteBeltGamesString[:len(whiteBeltGamesString)-1] + '\n')


for student, values in studentGrades.items():
    grades = student + ','
    for game in whiteBeltGames:
        if game in values:
            grades += values[game] + ','
        else:
            grades += '0,'
    whiteBeltGrades.write(grades[:len(grades)-1] + '\n')
    grades = ''

whiteBeltGrades.close()

yellowBeltGrades = open('yellowBeltGrades.csv', 'w+')
yellowBeltGrades.write(yellowBeltGamesString[:len(yellowBeltGamesString)-1] + '\n')

for student, values in studentGrades.items():
    grades = student + ','
    for game in yellowBeltGames:
        if game in values:
            grades += values[game] + ','
        else:
            grades += '0,'
    yellowBeltGrades.write(grades[:len(grades)-1] + '\n')
    grades = ''

yellowBeltGrades.close()


orangeBeltGrades = open('orangeBeltGames.csv', 'w+')
orangeBeltGrades.write(orangeBeltGamesString[:len(orangeBeltGamesString)-1] + '\n')

for student, values in studentGrades.items():
    grades = student + ','
    for game in orangeBeltGames:
        if game in values:
            grades += values[game] + ','
        else:
            grades += '0,'
    orangeBeltGrades.write(grades[:len(grades)-1] + '\n')
    grades = ''

orangeBeltGrades.close()