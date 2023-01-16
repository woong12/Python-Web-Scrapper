# Dictionary key : value 
# 자바스크립트 오브젝트랑 비슷함
player = {
    'name': 'kim',
    'age': 12,
    'alive': True,
    'fav_food': ["🍞", "🌮"]
}

print(player)
print(player.get('age'))
print(player.get('name'))


print(player.get('fav_food'))
print(player['fav_food'])


print(player)
player.pop('age')
print(player)


player['xp'] = 1500
print(player)

player['fav_food'].append('🍕')
print(player.get('fav_food'))
print(player['fav_food'])