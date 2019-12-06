---------- INSTALLATION ----------
===================================
1. Install python `https://www.python.org/downloads/release/python-2715/`
2. Download the `deckprobability` file
3. Create a `combos.txt` file in the same folder as the deckprobability file and configure
   it according to the example below. (or just try copy pasting the copy-pastable eg into `combos.txt`)
4. Right click on `deckprobability` and go to `Open With` and then select Python
5. Your combos.txt file should be updated with new probability values


---------- DEFINITIONS ----------
===================================
Non-Brick Perc:
Chance of any of the combos inputted occur

Cards In deck:
the cards you have in your deck

when there are '--':
This is the start of your combo and you put your combo name here
	notes:
	- Right after the two dashes is your combo name
	- You NEED the '-->' at the end of your combo name

when there are '----':
This is the part where you fill in the cards in your hand that make up a
particular combo. Info of the card is seperated by a pipe '|'.

	{number of card in your deck} | {card name} | {do you want the card in your hand}

	notes:
	- If you want the card in your hand put 'True' else, 'False'. (CASE SENSITIVE)

when there are '------':
This is where the percentage chance of that particular hand is printed and is used
as a seperator for the next hand that can produce the same final combo

	notes:
	- changing any part after the dashes don't really matter but you probably should leave it


---------- EXAMPLES ----------
===============================
eg.
```
Non-Brick Perc --> 30.361965024% #aggregated chance of getting any of the combos below

Cards in deck: 40

--"NAME OF YOUR FINAL COMBO ON BOARD" --> 8.16784258388% #percentage of final combo
----1 | "CARD 1" | False
----2 | "CARD 2" | True
----3 | "CARD 3" | True
------> 5.95750735553%                                   #Percentage that you will get above hand
----3 | "CARD 1" | False
----1 | "CARD 2" | True
------> 2.35035797776%                                   #Note: these hands should be able to produce the final combo
```

	notes: 
	- you can have MORE than 1 final Combo 
	- when updating your combos.txt file, you don't have to worry about the percentage numbers
	- maintain the formatting if you want the thing to work
	- you DO NOT need the ""


copy pastable eg.
```
Non-Brick Perc --> 30.361965024%

Cards in deck: 40

--combination 1 --> 8.16784258388%
----1 | A | False
----2 | B | True
----3 | C | True
------> 5.95750735553%
----3 | A | False
----1 | B | True
----3 | C | True
------> 2.35035797776%

--combination 2 --> 24.1681378992%
----3 | A | False
----3 | B | True
----2 | C | False
------> 17.0574443475%
----1 | A | False
----3 | B | True
----3 | C | True
------> 8.57303406646%```
