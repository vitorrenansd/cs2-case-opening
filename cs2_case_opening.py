from random import randint

# ANSI color codes by rarity
rarityColors = {
    0: '\033[90m',   # Grey
    1: '\033[94m',   # Light blue
    2: '\033[34m',   # Dark blue
    3: '\033[35m',   # Purple
    4: '\033[95m',   # Pink
    5: '\033[91m',   # Red
    6: '\033[93m',   # Yellow
}
resetColor = '\033[0m'

CS2Case = [
    ('Huntsman Knife | Doppler Phase 1 FN', 5, 800.89, 0.256),
    ('USP-S | Torque FT', 2, 3.50, 25.0),
    ('Glock-18 | Bunsen Burner MW', 2, 2.20, 30.0),
    ('MP7 | Armor Core FN', 1, 0.80, 44.744),
]

def drawSkin(itemsList):
    drawNumber = randint(1, 100000)
    currentRange = 0

    for item in itemsList:
        name, rarity, price, chance = item
        itemRange = int(chance * 1000)
        currentRange += itemRange
        if drawNumber <= currentRange:
            color = rarityColors.get(rarity, '')
            print(f"{color}You won a {name} | Price: US${price:.2f} | Probability: {chance}%{resetColor}")
            return  

drawSkin(CS2Case)
