'''
Tests for my CISC108 final project.

Change log:
  - 0.0.2: Fixed typo with assert_equal
  - 0.0.1: Initial version
'''

__VERSION__ = '0.0.2'

from cisc108 import assert_equal
from cisc108_game import assert_type

################################################################################
# Game import
# Rename this to the name of your project file.
from tic_tac_toe import *

# world definition
world = {
    'turn': 'University of Delaware',
    'positions': [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],
    'box': None,
    'won': [False, ''],
    'count': 0
}
initial_world = {
    'turn': 'University of Delaware',
    'positions': [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],
    'box': None,
    'won': [False, ''],
    'count': 0
}
################################################################################
## Testing winning_screen

# Describe this test here, then run whatever code is necessary to
# perform the tests
world['won'] = [True, 'University of Delaware']
winning_screen(world)
assert_equal(world['turn'], 'University of Delaware Wins')

world['won'] = [True, 'Villanova']
winning_screen(world)
assert_equal(world['turn'], 'Villanova Wins')

world['count'] = 9
world['won'] = [False, '']
winning_screen(world)
assert_equal(world["turn"], "It's a Tie")
assert_equal(world['won'], [True, ''])

################################################################################
## Testing update_world

################################################################################
## Testing winning_horozontal
world['positions'] = [[1,1,1],[1,1,1],[1,1,1]]
winning_horizontal(world)
assert_equal(world['won'], [True, 'University of Delaware'])

world['positions'] = [[2,2,2],[2,2,2],[2,2,2]]
winning_horizontal(world)
assert_equal(world['won'], [True, 'Villanova'])

################################################################################
## Testing winning_vertical
world['positions'] = [[1,0,0],[1,0,0],[1,0,0]]
winning_vertical(world)
assert_equal(world['won'], [True, 'University of Delaware'])

world['positions'] = [[0,1,0],[0,1,0],[0,1,0]]
winning_vertical(world)
assert_equal(world['won'], [True, 'University of Delaware'])

world['positions'] = [[0,0,1],[0,0,1],[0,0,1]]
winning_vertical(world)
assert_equal(world['won'], [True, 'University of Delaware'])

world['positions'] = [[2,0,0],[2,0,0],[2,0,0]]
winning_vertical(world)
assert_equal(world['won'], [True, 'Villanova'])

world['positions'] = [[0,2,0],[0,2,0],[0,2,0]]
winning_vertical(world)
assert_equal(world['won'], [True, 'Villanova'])

world['positions'] = [[0,0,2],[0,0,2],[0,0,2]]
winning_vertical(world)
assert_equal(world['won'], [True, 'Villanova'])

################################################################################
## Testing winning_diag

world['positions'] = [[1,0,0],[0,1,0],[0,0,1]]
winning_diag(world)
assert_equal(world['won'], [True, 'University of Delaware'])

world['positions'] = [[2,0,0],[0,2,0],[0,0,2]]
winning_diag(world)
assert_equal(world['won'], [True, 'Villanova'])

world['positions'] = [[0,0,1],[0,1,0],[1,0,0]]
winning_diag(world)
assert_equal(world['won'], [True, 'University of Delaware'])

world['positions'] = [[0,0,2],[0,2,0],[2,0,0]]
winning_diag(world)
assert_equal(world['won'], [True, 'Villanova'])

################################################################################
## Testing handle_mouse
world['won'] = [False, '']
world['turn'] = 'University of Delaware'
handle_mouse(world,1,1,'left')
assert_equal(world['turn'], 'Villanova')

handle_mouse(world,100,350,'left')
assert_equal(world['box'], 1)

handle_mouse(world,180,350,'left')
assert_equal(world['box'], 2)

handle_mouse(world,350,350,'left')
assert_equal(world['box'], 3)

handle_mouse(world,100,200,'left')
assert_equal(world['box'], 4)

handle_mouse(world,200,200,'left')
assert_equal(world['box'], 5)

handle_mouse(world,350,200,'left')
assert_equal(world['box'], 6)

handle_mouse(world,1,1,'left')
assert_equal(world['box'], 7)

handle_mouse(world,180,100,'left')
assert_equal(world['box'], 8)

handle_mouse(world,350,100,'left')
assert_equal(world['box'], 9)
################################################################################
## Testing check_box

world['box'] = 1
world['positions'] = [[0,0,0],[0,0,0],[0,0,0]]
check_box(world, 'University of Delaware')
assert_equal(world['positions'], [[1,0,0],[0,0,0],[0,0,0]])

world['box'] = 2
check_box(world, 'Villanova')
assert_equal(world['positions'], [[1,2,0],[0,0,0],[0,0,0]])

world['box'] = 3
check_box(world, 'University of Delaware')
assert_equal(world['positions'], [[1,2,1],[0,0,0],[0,0,0]])

world['box'] = 4
check_box(world, 'Villanova')
assert_equal(world['positions'], [[1,2,1],[2,0,0],[0,0,0]])

world['box'] = 5
check_box(world, 'University of Delaware')
assert_equal(world['positions'], [[1,2,1],[2,1,0],[0,0,0]])

world['box'] = 6
check_box(world, 'Villanova')
assert_equal(world['positions'], [[1,2,1],[2,1,2],[0,0,0]])

world['box'] = 7
check_box(world, 'University of Delaware')
assert_equal(world['positions'], [[1,2,1],[2,1,2],[1,0,0]])

world['box'] = 8
check_box(world, 'Villanova')
assert_equal(world['positions'], [[1,2,1],[2,1,2],[1,2,0]])

world['box'] = 9
check_box(world, 'University of Delaware')
assert_equal(world['positions'], [[1,2,1],[2,1,2],[1,2,1]])
