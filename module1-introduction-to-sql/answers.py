import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

query1 = 'SELECT COUNT(*) FROM charactercreator_character;'

curs = conn.cursor()
answer_1 = curs.execute(query1).fetchall()

query2 = 'SELECT COUNT(*) FROM charactercreator_character as ccc, charactercreator_mage as cc_mage WHERE ccc.character_id = cc_mage.character_ptr_id UNION SELECT COUNT(*) FROM charactercreator_character as ccc, charactercreator_thief as cc_thief WHERE ccc.character_id = cc_thief.character_ptr_id UNION SELECT COUNT(*) FROM charactercreator_character as ccc, charactercreator_cleric as cc_cleric WHERE ccc.character_id = cc_cleric.character_ptr_id UNION SELECT COUNT(*) FROM charactercreator_character as ccc, charactercreator_fighter as cc_fighter WHERE ccc.character_id = cc_fighter.character_ptr_id UNION SELECT COUNT(*) FROM charactercreator_character as ccc, charactercreator_necromancer as cc_necromancer WHERE ccc.character_id = cc_necromancer.mage_ptr_id'
answer_2 = curs.execute(query2).fetchall()

query3 = 'SELECT COUNT(*) FROM armory_item;'
answer_3 = curs.execute(query3).fetchall()

query4 = 'SELECT COUNT(*) FROM armory_item INNER JOIN armory_weapon ON armory_weapon.item_ptr_id = armory_item.item_id;'
answer_4 = curs.execute(query4).fetchall()

query5 = 'SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;'
answer_5 = curs.execute(query5).fetchall()

query6 = 'SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory as cci, armory_weapon as arm WHERE cci.item_id = arm.item_ptr_id GROUP BY character_id LIMIT 20;'
answer_6 = curs.execute(query6).fetchall()

query7 = 'SELECT CAST(COUNT(item_id) AS FLOAT) / COUNT(DISTINCT(character_id)) FROM charactercreator_character_inventory;'
answer_7 = curs.execute(query7).fetchall()

query8 = 'SELECT CAST(COUNT(item_id) AS FLOAT) / COUNT(DISTINCT(character_id)) FROM charactercreator_character_inventory as cci, armory_weapon as arm WHERE cci.item_id = arm.item_ptr_id;'
answer_8 = curs.execute(query8).fetchall()

print(answer_1, answer_2, answer_3, answer_4, answer_7, answer_8)
