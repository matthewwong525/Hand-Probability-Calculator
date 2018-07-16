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

