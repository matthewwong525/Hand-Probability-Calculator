from HandCombo import HandCombo
from FieldCombo import FieldCombo
class TotalCombo():
    def __init__(self, fieldCombos = [], cardsInDeck = 40):
        self.fieldCombos = fieldCombos
        self.brickPerc = self.calcPercBrick()
        self.cardsInDeck = cardsInDeck

    def calcPercBrick(self):
        percBrick = 1
        for combo in self.fieldCombos:
            percBrick *= (1 - combo.percDraw)
        return 1 - percBrick

    def addCombo(self, fieldCombo):
        self.fieldCombos.append(fieldCombo)
        self.brickPerc = self.calcPercBrick()

    def saveCombos(self):
        with open('combos.txt', 'w') as comboFile:
            comboFile.write('Non-Brick Perc --> ' + str(self.brickPerc*100) + '%\n\n')
            comboFile.write('Cards in deck: ' + str(self.cardsInDeck) + "\n")
            for fieldCombo in self.fieldCombos:
                comboFile.write("\n--" + fieldCombo.comboName + " --> "+ str(fieldCombo.percDraw*100) + "%" + "\n")
                for handCombo in fieldCombo.handCombos:
                    for card in handCombo.cardCombo:
                        comboFile.write("----" + str(card['numCard']) +
                            " | " + card['cardName'] +
                            " | " + str(not card['notInclude']) + "\n")
                    comboFile.write("------> " + str(handCombo.percDraw*100) + "%" + "\n")

    def readCombos(self):
        allCombos = []
        cardsInDeck = 0
        with open('combos.txt', 'r') as comboFile:
            while cardsInDeck == 0:
                for line in comboFile:
                    if (line[:14]).lower() == "cards in deck:":
                        cardsInDeck = int(line.split(':')[1])
        with open('combos.txt', 'r') as comboFile:            
            handCombo = HandCombo([], cardsInDeck)
            fieldCombo = FieldCombo("", [])
            for line in comboFile:
                if line[:6] == "------":
                    fieldCombo.addHandCombo(handCombo)
                    handCombo = HandCombo([], cardsInDeck)
                elif line[:4] == "----":
                    cardInfo = line[4:].split("|")
                    cardName = cardInfo[1].strip()
                    numCard = int(cardInfo[0].strip())
                    notInclude = cardInfo[2].strip() == "False"
                    cardCombo = { "cardName" : cardName, "numCard" : numCard, "notInclude" : notInclude }
                    handCombo.addCard(cardCombo)
                elif line[:2] == "--":
                    if fieldCombo.comboName != "":
                        allCombos.append(fieldCombo)
                    comboName = (line[2:].split("-->")[0]).strip()
                    fieldCombo = FieldCombo(comboName, [])
            allCombos.append(fieldCombo)
        self.fieldCombos = allCombos
        self.brickPerc = self.calcPercBrick()
        return self

