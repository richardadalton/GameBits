# -*- coding: utf-8 -*-

# The character we are playing as
# Provides functions for the actions we can perform
class Character:
    def __init__(self, location, items):
        self.Location = location
        self.Items = items

    def Inventory(self):
        print map(str,self.Items)

    def Look(self):
        print map(str,self.Location.Items)

    def PickUp(self, item):
        pickedUp = self.Location.Take(item)
        if pickedUp is not None:
            print 'You picked up the {0}'.format(item)
            self.Items[item] = pickedUp

    def Open(self, item):
        if self.Items.has_key(item):
            item.Open()
        else:
            print 'You don\'t have a {0}'.format(item)

# A location within the game, e.g. a Room
# We can pick up items from a location
class Location:
    def __init__(self, description, items):
        self.Description = description
        self.Items = items

    def Take(self, item):
        if self.Items.has_key(item):
            found = self.Items[item]
            if found.CanBePickedUp():
                del self.Items[item]
                return found
            else:
                print 'You can\'t pick up the {0}'.format(item)
                return None
        else:
            print 'There is no {0} here'.format(item)
            return None

# An item within the game that we can find, pick up and use
class Item:
    def __init__(self, description):
        self.Description = description

    def __str__(self):
        return self.Description

    def CanBePickedUp(self):
        return True

# A Box is a special kind of item that can contain other items
# Opening the box reveals the items it contains
# A box can be picked up and opened later
class Box(Item):
    isOpen = False

    def __init__(self, items):
        Item.__init__(self,'box')
        self.Items = items

# A Door is a special kind of item that can be closed and locked
# You can not pick up a door
class Door(Item):
    isLocked = True
    isOpen = False

    def __init__(self):
        Item.__init__(self,'door')

    def CanBePickedUp(self):
        return False


# Create the Initial starting position for the game
door = Door()
box = Box({'key': Item('key')})
room = Location('A shed', {'door': door, 'box': box})
inventory = dict()

character = Character(room, inventory)




