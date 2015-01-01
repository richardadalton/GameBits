# -*- coding: utf-8 -*-
# A simple text adventure
# Implemented using global varibles and functions
# There is no GameLoop, use the Python REPL to call functions
# Messy, but simple and it works
# Gets complicated very quickly, doesn't scale up to bigger games
# Highly likely to contain bugs

boxIsOpen = False
doorIsLocked = True

inventory = [];
here = ['box', 'door']

# Commands
# ------------
# here              List items that are lying around
# inventory         List items you are holding
# pickup(item)      Pick up an item that is lying around
# open(item)        Open an item if possible
# unlock(item)      Unlock an item if possible

def pickup(item):
    if item == 'door':
        print 'Come on, you can\'t pick up a door'
    else:    
        tryPickup(item)
    
def open(item):
    if item == 'door':
        tryOpenDoor()
        return
    
    if item == 'box':
        tryOpenBox()
        return
    
    if exists(item):
        print 'You can\'t open a {0}'.format(item)
    else:
        print 'There is no {0} here'.format(item)

def unlock(item):
    if item == 'door':
        tryUnlockDoor()
    else:
        print 'You can\'t unlock a {0}'.format(item)


# Support Functions
# These should not be called directly

def tryPickup(item):
    if item in here:
        here.remove(item)
        inventory.append(item)
        print 'You have picked up the {0}'.format(item)
    else:
        print 'There is no {0} here'.format(item)


def tryOpenDoor():
    global doorIsLocked
    if doorIsLocked:
        print "It\'s locked"
    else:
        print "You opened the door, that's it, you win"

def tryOpenBox():
    global boxIsOpen
    if boxIsOpen:
        print 'You have already opened the box'
    else:            
        find('key')
        boxIsOpen = True

def tryUnlockDoor():
    global doorIsLocked
    if doorIsLocked:
        if 'key' in inventory:
            print "You have unlocked the door with the key"
            doorIsLocked = False
        else:
            print "You need a key to unlock the door"                
    else:
        print "The door is already unlocked"


def find(item):
    here.append(item)
    print 'You have found a {0}'.format(item)

def exists(item):
    return (item in here) or (item in inventory)
