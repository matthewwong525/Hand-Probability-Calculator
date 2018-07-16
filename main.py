from __future__ import division
from HandCombo import HandCombo
from FieldCombo import FieldCombo
from TotalCombo import TotalCombo

from random import shuffle
def testDeck():
    deckList = []
    totalShuffles = 0
    numCardInHand = 0
    for shuffles in range(0,1000):
        intCount = 1;
        for card in range(0,39):
            deckList.append(intCount)
            intCount += 1
        shuffle(deckList)
        cardsInHand = deckList[:5]
        #print cardsInHand
        if (1 in cardsInHand or 2 in cardsInHand or 3 in cardsInHand) and not (4 in cardsInHand or 5 in cardsInHand or 6 in cardsInHand):
            numCardInHand += 1
        totalShuffles += 1
    return numCardInHand/totalShuffles


cardCombo1 = [{ "cardName" : "A", "numCard" : 3, "notInclude" : True }, { "cardName" : "B", "numCard" : 3, "notInclude" : False }, { "cardName" : "C", "numCard" : 3, "notInclude" : False }]
cardCombo2 = [{ "cardName" : "A", "numCard" : 3, "notInclude" : True }, { "cardName" : "B", "numCard" : 3, "notInclude" : False }, { "cardName" : "C", "numCard" : 3, "notInclude" : False }]
cardCombo3 = [{ "cardName" : "A", "numCard" : 3, "notInclude" : True }, { "cardName" : "B", "numCard" : 3, "notInclude" : False }, { "cardName" : "C", "numCard" : 3, "notInclude" : True }]
cardCombo4 = [{ "cardName" : "A", "numCard" : 3, "notInclude" : True }, { "cardName" : "B", "numCard" : 3, "notInclude" : False }, { "cardName" : "C", "numCard" : 3, "notInclude" : False }]
fieldCombo1 = FieldCombo("combo1", [HandCombo(cardCombo1, 40), HandCombo(cardCombo2, 40)])
fieldCombo2 = FieldCombo("combo2", [HandCombo(cardCombo3, 40), HandCombo(cardCombo4, 40)])
#TotalCombo([fieldCombo1, fieldCombo2]).saveCombos()
aCombo = TotalCombo().readCombos()
aCombo.saveCombos()
#print testDeck()