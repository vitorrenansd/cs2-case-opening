from random import randint

# ANSI color codes by rarity
rarityColors = {
    0: '\033[90m',   # Grey
    1: '\033[94m',   # Light blue
    2: '\033[34m',   # Dark blue
    3: '\033[35m',   # Purple
    4: '\033[95m',   # Pink
    5: '\033[91m',   # Red
    6: '\033[93m'    # Yellow
}
resetColor = '\033[0m'

CS2Case = [
    ('AWP | Printstream', 5, 100.61, 0.320),
    ('FAMAS | Bad Trip', 5, 3.84, 0.320),
    ('UMP-45 | K.O. Factory', 4, 6.65, 1.066),
    ('Glock-18 | Shinobu', 4, 9.41, 1.066),
    ('AK-47 | Searing Rage', 4, 7.06, 1.066),
    ('Zeus x27 | Tosai', 3, 1.03, 3.197),
    ('P90 | Wave Breaker', 3, 0.85, 3.197),
    ('Nova | Rising Sun', 3, 0.76, 3.197),
    ('Galil AR | Control', 3, 0.96, 3.197),
    ('Desert Eagle | Serpent Strike', 3, 1.19, 3.197),
    ('XM1014 | Mockingbird', 2, 0.07, 11.418),
    ('USP-S | PC-GRN', 2, 0.09, 11.418),
    ('SSG 08 | Memorial', 2, 0.07, 11.418),
    ('P2000 | Sure Grip', 2, 0.07, 11.418),
    ('MP9 | Nexus', 2, 0.07, 11.418),
    ('MAG-7 | Resupply', 2, 0.07, 11.418),
    ('M4A4 | Choppa', 2, 0.07, 11.418)
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
