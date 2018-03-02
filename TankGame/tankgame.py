from tank import Tank

# Create tanks by adding items to the dictionary
tanks = {'a': Tank('Darragh'), 'b': Tank('Bob'), 'c': Tank('Dave')}

alive_tanks = len(tanks)

while alive_tanks > 1:
    print ()
    for tank_name in sorted(tanks.keys()):
        print (tank_name, tanks[tank_name])

    first = input('Who fires? ').lower()
    second = input('Who do they fire at? ').lower()

    try:
        first_tank = tanks[first]
        second_tank = tanks[second]
    except (KeyError, name):
        print ('No tank named ', name)
        continue

    if not first_tank.alive or not second_tank.alive:
        print ("One of those tanks are dead!")
        continue

    print ()
    print ("*" * 30)

    first_tank.fire_at(second_tank)
    if not second_tank.alive:
        alive_tanks -= 1

    print ('*' * 30)

for tank in tanks.values():
    if tank.alive:
        print (tank.name, 'is the winner!')
        break
