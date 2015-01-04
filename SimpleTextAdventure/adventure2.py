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

    def Drop(self, itemKey):
        if self.Items.has_key(itemKey):
            item = self.Items[itemKey]
            self.Location.Put(item)
            del self.Items[itemKey]
            print 'You dropped the {0}'.format(itemKey)
        else:
            print 'You don\'t have the {0}'.format(itemKey)

    def PickUp(self, itemKey):
        pickedUp = self.Location.TryPickUp(itemKey)
        if pickedUp is not None:
            print 'You picked up the {0}'.format(itemKey)
            self.Items[itemKey] = pickedUp

    def Open(self, itemKey):
        if self.Items.has_key(itemKey):
            item  = self.Items[itemKey]
            item.OpenIn(self.Location)
        else:
            self.Location.TryOpen(itemKey)

        

# A location within the game, e.g. a Room
# We can pick up items from a location
class Location:
    def __init__(self, description, items):
        self.Description = description
        self.Items = items

    def TryPickUp(self, itemKey):
        if self.Items.has_key(itemKey):
            return self.Items[itemKey].TryPickUpFrom(self)
        else:
            print 'There is no {0} here'.format(itemKey)
            return None

    def TryOpen(self, itemKey):
        if self.Items.has_key(itemKey):
            item = self.Items[itemKey]
            item.OpenIn(self)
        else:
            print 'There is no {0} here'.format(itemKey)

    def Put(self, item):
        self.Items[item.Description] = item

    def Take(self, item):
        del self.Items[item.Description]
        return item

# An item within the game that we can find, pick up and use
class Item:
    def __init__(self, description):
        self.Description = description
        self.Held = False

    def __str__(self):
        return self.Description

    def TryPickUpFrom(self, location):
        self.Held = True
        return location.Take(self)

    def OpenIn(self, location):
        print 'You can\'t open the {0}'.format(self.Description)


# A Box is a special kind of item that can contain other items
# Opening the box reveals the items it contains
# A box can be picked up and opened later
class Box(Item):
    def __init__(self, items):
        Item.__init__(self,'box')
        self.IsOpen = False
        self.Items = items

    def OpenIn(self, location):
        if self.IsOpen:
            print 'It\'s already open'
        elif not self.Held:
            print 'You don\'t have the box'
        else:
            for item in self.Items:
                location.Put(item)

# A Door is a special kind of item that can be closed and locked
# You can not pick up a door
class Door(Item):    
    def __init__(self):
        Item.__init__(self,'door')
        self.IsLocked = True
        self.IsOpen = False

    def TryPickUpFrom(self, location):
        print 'You can\'t pick up a door'
        return None
    
    def OpenIn(self, location):
        if self.IsLocked == True:
            print 'It\'s Locked'
        else:
            self.IsOpen = True
            print 'You\'ve opened the door, you win.'


# Create the Initial starting position for the game
door = Door()
box = Box([Item('key')])
room = Location('A shed', {'door': door, 'box': box})
inventory = dict()

character = Character(room, inventory)




