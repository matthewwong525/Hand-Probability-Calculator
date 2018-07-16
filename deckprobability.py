from __future__ import division
import sys
import math

class HandCombo():
    def __init__(self, cardCombo = [], cardsInDeck = 40):
        self.cardCombo = cardCombo
        self.percDraw = self.finalProb(cardsInDeck, cardCombo)
        self.cardsInDeck = cardsInDeck
    def addCard(self, card):
        self.cardCombo.append(card)
        self.percDraw = self.finalProb(self.cardsInDeck, self.cardCombo)
    def binomialCoeff(self, x, y):
        if y == x:
            return 1
        elif y == 1:         # see georg's comment
            return x
        elif y > x:          # will be executed only if y != 1 and y != x
            return 0
        else:                # will be executed only if y != 1 and y != x and x <= y
            a = math.factorial(x)
            b = math.factorial(y)
            c = math.factorial(x-y)  # that appears to be useful to get the correct result
            div = a // (b * c)
            return div
    def hyper(self, popSize, numSuccess, numDraw, observedSuccess):
        return self.binomialCoeff(numSuccess, observedSuccess) * self.binomialCoeff(popSize - numSuccess, numDraw - observedSuccess) / self.binomialCoeff(popSize, numDraw)

    def multihyper(self, cardCombo, cardSequence):
        if len(cardSequence) != len(cardCombo):
            return 0
        numECardDeck = 0
        numECardHand = 0
        for idx, card in enumerate(cardCombo):
            numECardDeck += card['numCard']
            numECardHand += cardSequence[idx]
            
        numerator = 1
        for idx, card in enumerate(cardCombo):
            if card['numCard'] < cardSequence[idx]:
                return 0
            numerator = numerator * self.binomialCoeff(card['numCard'], cardSequence[idx])
        return numerator / self.binomialCoeff(numECardDeck, numECardHand)

    def finalProb(self, cardsInDeck, cardCombo):
        drawCardCombo = []
        notDrawCardPerc = 1
        for card in cardCombo:
            if card['notInclude']:
                notDrawCardPerc *= (1 - self.calcDrawProb(cardsInDeck, [card]))
            else:
                drawCardCombo.append(card)
        return self.calcDrawProb(cardsInDeck, drawCardCombo)*notDrawCardPerc

    # totalNumCard: total of all "non-garnet" cards in deck
    # cardCombo: list of garnet cards
    # cardsInDeck: number of cards in deck
    # CARDS_IN_HAND: number of cards drawn to hand
    # drawProbability: percentage chance for a certain draw combination
    def calcDrawProb(self, cardsInDeck, cardCombo):
        numDraw = len(cardCombo)
        CARDS_IN_HAND = 5
        drawProbability = 0
        totalNumCard = 0
        for card in cardCombo:
            totalNumCard += card['numCard']
        if numDraw == 0:
            return 0
        # one card
        elif numDraw == 1:
            cardSequences = [ [[1]], [[2]], [[3]], [[4]], [[5]] ]
        # two cards
        elif numDraw == 2:
            cardSequences = [ [[1,1]],
                              [[1,2], [2,1]],
                              [[1,3], [2,2], [3,1]],
                              [[1,4], [2,3], [3,2], [4,1]] ]
        # three cards
        elif numDraw == 3:
            cardSequences = [ [[1, 1, 1]],
                             [[2, 1, 1], [1, 2, 1], [1, 1, 2]],
                             [[2, 2, 1], [2, 1, 2], [1, 2, 2], [3, 1, 1], [1, 3, 1], [1, 1, 3]] ]
        # four cards
        elif numDraw == 4:
            cardSequences = [ [[1, 1, 1, 1]],
                             [[2, 1, 1, 1], [1, 2, 1, 1], [1, 1, 2, 1], [1, 1, 1, 2]] ]
        # five cards
        elif numDraw == 5:
            cardSequences = [[[1, 1, 1, 1, 1]]]
        # https://stats.stackexchange.com/questions/121101/multivariate-hypergeometric-distribution-in-r
        sigCardCount = 0
        for sequence in cardSequences:
            EDrawProb = self.hyper(cardsInDeck, totalNumCard, CARDS_IN_HAND, numDraw + sigCardCount)
            ECardsProb = 0
            for cardOrder in sequence:
                ECardsProb += self.multihyper(cardCombo, cardOrder)
            drawProbability += EDrawProb*ECardsProb
            sigCardCount += 1
                
        return drawProbability

class FieldCombo():
    #handCombos: list
    def __init__(self, comboName = "Unnamed Combo", handCombos = []):
        self.comboName = comboName
        self.handCombos = handCombos
        self.percDraw = self.calcPercDraw()

    def addHandCombo(self, handCombo):
        self.handCombos.append(handCombo)
        self.percDraw = self.calcPercDraw()

    def printHandCombo(self):
        for combo in self.handCombo:
            print combo

    def calcPercDraw(self):
        percDraw = 1
        for combo in self.handCombos:
            percDraw *= 1 - combo.percDraw
        return 1 - percDraw

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

aCombo = TotalCombo().readCombos()
aCombo.saveCombos()
