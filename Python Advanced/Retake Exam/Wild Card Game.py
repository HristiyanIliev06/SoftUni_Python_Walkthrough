def draw_cards(*args, **kwargs):    #85/100 Тъй като около 30 минути карах Judge системата да каже къв ѝ е дертът! Иначе целият изпит - завършен за около 2 часа от общо 4 часа!
    monster_cards = []
    spell_cards = []
    result = []
    
    for card_name, card_type in args:
        if card_type=='monster':
            monster_cards.append(card_name)
        else:
            spell_cards.append(card_name)
            
    for card_name, card_type in kwargs.items():
        if card_type=='monster':
            monster_cards.append(card_name)
        else:
            spell_cards.append(card_name)
            
    final_monster_cards = sorted(monster_cards, key = lambda x: (x[0], x[1]), reverse = True)
    final_spell_cards = sorted(spell_cards, key = lambda x: (x[0], x[1]))
            
    if final_monster_cards:
        result.append("Monster cards:")
        [result.append(f"  ***{monster_card}") for monster_card in final_monster_cards]
        
    if final_spell_cards:
        result.append("Spell cards:")
        [result.append(f"  $$${spell_card}") for spell_card in final_spell_cards]
        
    return '\n'.join(result)

#print(draw_cards(("cyber dragon", "monster"), freeze="spell",))

#print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))

print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))  