import random
caseName = 'Knife Case 50/50'

caseItems = [
    ('\033[1;31mGut Knife | Rust Coat BS\033[m', 834.72, 50),
    ('\033[1;31mBowie Knife | Tiger Tooth FN\033[m', 1785.18, 20),
    ('\033[1;31mFalchion Knife | Slaughter FT\033[m', 2315.94, 1.7),
    ('\033[1;31mFalchion Knife | Slaughter MW\033[m', 2160.42, 12),
    ('\033[1;31mFalchion Knife | Slaughter FN\033[m', 1890.78, 1),
    ('\033[1;31mTalon Knife | Ultraviolet BS\033[m', 2528.34, 2),
    ('\033[1;31mTalon Knife | Ultraviolet WW\033[m', 2836.14, 3),
    ('\033[1;31mTalon Knife | Ultraviolet FT\033[m', 3022.74, 2),
    ('\033[1;31mTalon Knife | Ultraviolet MW\033[m', 3809.34, 1),
    ('\033[1;31mHuntsman Knife | Doppler Phase 1 FN\033[m', 3515.16, 4),
    ('\033[1;31mButterfly Knife | Lore WW\033[m', 7623.12, 2.5),
    ('\033[1;31mButterfly Knife | Lore FT\033[m', 8999.28, 0.5),
    ('\033[1;31mButterfly Knife | Lore MW\033[m', 14199.90, 0.3),
]

def sortearSkin(itens):
    chances = [item[2] for item in itens]
    itemSorteado = random.choices(itens, weights=chances, k=1)[0]
    return itemSorteado

item = sortearSkin(caseItems)
print('Knife Case 50/50')
print(f"Você sorteou: {item[0]} | Valor: R${item[1]:.2f} | Chance: {item[2]}%")
