"""
For this game you play with another player and take turns clicking in boxes. THe first one to get three of their team's
logo in a row (either vertically, horizontally, or diagonally) wins, and the game resets instantly. IF neither player is
able to do this, the game is a tie and it will automatically reset for another game If you accidentally click in a box
that was already taken, you forfeit your turn and it becomes the next player's turn.

Change log:
  - 0.0.2: Added support for handle_release
  - 0.0.1: Initial version
  -.0.1.0: Added the ability for the game to run
"""
__VERSION__ = '0.1.0'
import arcade
from cisc108_game import Cisc108Game
'''
# TODO:
    Optimization
    Test the game
'''
################################################################################
## Game Constants

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "tic tac toe"
UD = arcade.load_texture('ud.png')
VN = arcade.load_texture('villa.png')

################################################################################
## Record definitions

World = {
    'turn': str,
    'positions': [[int]],
    'box': int,
    'won': list,
    'count': int
}
INITIAL_WORLD = {
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
# Drawing functions
def draw_logo(world: World):
    """
    Actually draws the logo of the school in the given x and y coordinate.

    Args:

        world (World): The current sate of the world.
    """
    y = 500
    for row in world['positions']:
        x = 0
        for num in row:
            if num == 1:
                arcade.draw_xywh_rectangle_textured((x * .75) + 50, (y * .8) - 50,
                                                    100, 100, UD)
            elif num == 2:
                arcade.draw_xywh_rectangle_textured((x * .75) + 50, (y * .8) - 50,
                                                    100, 100, VN)
            x += 200
        y -= 180

def winning_screen(world: World):
    if world['won'] == [True, 'University of Delaware']:
        world['turn'] = 'University of Delaware Wins'

    elif world['won'] == [True, 'Villanova']:
        world['turn'] = 'Villanova Wins'

    elif world['count'] == 9 and world['won'][0] == False:
        world['turn'] = "It's a Tie"
        world['won'][0] = True

def draw_world(world: World):
    """
    Draws the basic layout of the game, with the specific line drawn detailed below.
    
    Args:
        world (World): The current world to draw
    """
    # VERTICAL LEFT LINE
    arcade.draw_rectangle_filled(175, WINDOW_HEIGHT / 2, 15, 400, arcade.color.WHITE)
    # VERTICAL RIGHT LINE
    arcade.draw_rectangle_filled(325, WINDOW_HEIGHT / 2, 15, 400, arcade.color.WHITE)
    # HORIZONTAL TOP LINE
    arcade.draw_rectangle_filled(WINDOW_WIDTH / 2, 175, 400, 15, arcade.color.WHITE)
    # HORIZONTAL BOTTOM LINE
    arcade.draw_rectangle_filled(WINDOW_WIDTH / 2, 325, 400, 15, arcade.color.WHITE)

    # noinspection PyTypeChecker
    arcade.draw_text(world['turn'], 50, 475, arcade.color.WHITE, 20, 400, 'center')

    for row in world['positions']:
        for num in row:
            if num == 1:
                draw_logo(world)
            elif num == 2:
                draw_logo(world)

################################################################################
# World manipulating functions

def update_world(world: World):
    """
    Runs the winning condition checks every tic. If the game is over it resets the world to its initial state.
    
    Args:
        world (World): The current world to update.
    """
    winning_vertical(world)
    winning_horizontal(world)
    winning_diag(world)
    winning_screen(world)

    if world['won'][0]:
        world['positions'] = [[0, 0, 0, ], [0, 0, 0], [0, 0, 0]]
        world['won'] = [False, '']
        world['box'] = None
        world['count'] = 0

def winning_horizontal(world: World):
    """
    Tests the current list of lists of player positions against winning combinations.

    Args:
        world (World): The current world to update.

    """
    # Winning variables for less repetition.
    h_ud = [1, 1, 1]
    h_vn = [2, 2, 2]
    # Positional variables for less repetition.
    pos0 = world['positions'][0]
    pos1 = world['positions'][1]
    pos2 = world['positions'][2]

    # Horizontal winning conditions for UD
    if pos0 == h_ud or pos1 == h_ud or pos2 == h_ud:
        world['won'] = [True, 'University of Delaware']
    # Horizontal winning conditions for Villanova
    elif pos0 == h_vn or pos1 == h_vn or pos2 == h_vn:
        world['won'] = [True, 'Villanova']

def winning_vertical(world: World):
    """
    Calculates if there is a winner vertically based off of the current world grid.
    
    Args:
        world (World): The current world to update.
    """
    # Positional variables for less repitition

    pos0 = world['positions'][0]
    pos1 = world['positions'][1]
    pos2 = world['positions'][2]

    # First Columb UD win check
    if pos0[0] == 1 and pos1[0] == 1 and pos2[0] == 1:
        world['won'] = [True, 'University of Delaware']
    # Second Column UD win check
    elif pos0[1] == 1 and pos1[1] == 1 and pos2[1] == 1:
        world['won'] = [True, 'University of Delaware']
    # Last column UD win check
    elif pos0[2] == 1 and pos1[2] == 1 and pos2[2] == 1:
        world['won'] = [True, 'University of Delaware']

    # First column VN win check
    if pos0[0] == 2 and pos1[0] == 2 and pos2[0] == 2:
        world['won'] = [True, 'Villanova']
    # Second Column VN win check
    elif pos0[1] == 2 and pos1[1] == 2 and pos2[1] == 2:
        world['won'] = [True, 'Villanova']
    # Last column Vn win check
    elif pos0[2] == 2 and pos1[2] == 2 and pos2[2] == 2:
        world['won'] = [True, 'Villanova']

def winning_diag(world: World):
    '''
    Consumes the world dictionary and calculates if there is a winner diagonally.

    Args:
        world (World): The current state of the world.
    '''
    # Position Variables to reduce repitition.
    Up_Left = world['positions'][0][0]
    Mid = world['positions'][1][1]
    Down_Right = world['positions'][2][2]

    Up_Right = world['positions'][0][2]
    Down_Left = world['positions'][2][0]

    # Diagnonal from left to right
    if Up_Left == 1 and Mid == 1 and Down_Right == 1:
        world['won'] = [True, 'University of Delaware']
    elif Up_Left == 2 and Mid == 2 and Down_Right == 2:
        world['won'] = [True, 'Villanova']

    # DIagnonal from right to left.
    if Up_Right == 1 and Mid == 1 and Down_Left == 1:
        world['won'] = [True, 'University of Delaware']
    elif Up_Right == 2 and Mid == 2 and Down_Left == 2:
        world['won'] = [True, 'Villanova']

def handle_key(world: World, key: int):
    """
    Does not use keys.

    Args:
        world (World): Current state of the world.
        key (int): The ASCII value of the pressed keyboard key (use ord and chr).
    """

def handle_mouse(world: World, x: int, y: int, button: str):
    """
    On a click, there will either be a Blue Hen or Villanova V placed in the box where the cursor resides.

    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of the mouse when the button was clicked.
        y (int): The y-coordinate of the mouse when the button was clicked.
        button (str): The button that was clicked ('left', 'right', 'middle')
    """
    world['count'] += 1

    if world['won'][0] == False:
        if world['turn'] == 'University of Delaware':
            world['turn'] = 'Villanova'
            if x <= 175 and y >= 325:
                world['box'] = 1
                check_box(world, 'University of Delaware')
            elif 175 <= x <= 325 <= y:
                world['box'] = 2
                check_box(world, 'University of Delaware')
            elif x >= 325 and y >= 325:
                world['box'] = 3
                check_box(world, 'University of Delaware')
            ##########################
            elif x <= 175 <= y <= 325:
                world['box'] = 4
                check_box(world, 'University of Delaware')
            elif 175 <= x <= 325 and 175 <= y <= 325:
                world['box'] = 5
                check_box(world, 'University of Delaware')
            elif x >= 325 >= y >= 175:
                world['box'] = 6
                check_box(world, 'University of Delaware')
            ##########################
            elif x <= 175 and y <= 175:
                world['box'] = 7
                check_box(world, 'University of Delaware')
            elif y <= 175 <= x <= 325:
                world['box'] = 8
                check_box(world, 'University of Delaware')
            elif x >= 325 and y <= 175:
                world['box'] = 9
                check_box(world, 'University of Delaware')
        else:
            world['turn'] = 'University of Delaware'
            if x <= 175 and y >= 325:
                world['box'] = 1
                check_box(world, 'Villanova')
            elif 175 <= x <= 325 <= y:
                world['box'] = 2
                check_box(world, 'Villanova')
            elif x >= 325 and y >= 325:
                world['box'] = 3
                check_box(world, 'Villanova')
            ##########################
            elif x <= 175 <= y <= 325:
                world['box'] = 4
                check_box(world, 'Villanova')
            elif 175 <= x <= 325 and 175 <= y <= 325:
                world['box'] = 5
                check_box(world, 'Villanova')
            elif x >= 325 >= y >= 175:
                world['box'] = 6
                check_box(world, 'Villanova')
            ##########################
            elif x <= 175 and y <= 175:
                world['box'] = 7
                check_box(world, 'Villanova')
            elif y <= 175 <= x <= 325:
                world['box'] = 8
                check_box(world, 'Villanova')
            elif x >= 325 and y <= 175:
                world['box'] = 9
                check_box(world, 'Villanova')

def handle_motion(world: World, x: int, y: int):
    """
    Does not use.

    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of where the mouse was moved to.
        y (int): The x-coordinate of where the mouse was moved to.
    """

def handle_release(world: World, key: int):
    """
    Does not use.

    Args:
        world (World): Current state of the world.
        key (int): The ASCII value of the released keyboard key (use ord and chr).
    """

def check_box(world: World, team: str):
    '''
    Checks to see what box the cursor is in and checks to make sure the box is not already occupied by other team.
    If it is vacant, It makes the current team's number populate the area.

    Args:
        world (World): The current state of the world.
        team (str): The current team whos turn it is.
    '''
    if world['box'] == 1 and world['positions'][0][0] == 0:
        if team == 'University of Delaware':
            world['positions'][0][0] = 1
        else:
            world['positions'][0][0] = 2
    elif world['box'] == 2 and world['positions'][0][1] == 0:
        if team == 'University of Delaware':
            world['positions'][0][1] = 1
        else:
            world['positions'][0][1] = 2
    elif world['box'] == 3 and world['positions'][0][2] == 0:
        if team == 'University of Delaware':
            world['positions'][0][2] = 1
        else:
            world['positions'][0][2] = 2
    ###############################################################
    elif world['box'] == 4 and world['positions'][1][0] == 0:
        if team == 'University of Delaware':
            world['positions'][1][0] = 1
        else:
            world['positions'][1][0] = 2
    elif world['box'] == 5 and world['positions'][1][1] == 0:
        if team == 'University of Delaware':
            world['positions'][1][1] = 1
        else:
            world['positions'][1][1] = 2
    elif world['box'] == 6 and world['positions'][1][2] == 0:
        if team == 'University of Delaware':
            world['positions'][1][2] = 1
        else:
            world['positions'][1][2] = 2
    ###############################################################
    elif world['box'] == 7 and world['positions'][2][0] == 0:
        if team == 'University of Delaware':
            world['positions'][2][0] = 1
        else:
            world['positions'][2][0] = 2
    elif world['box'] == 8 and world['positions'][2][1] == 0:
        if team == 'University of Delaware':
            world['positions'][2][1] = 1
        else:
            world['positions'][2][1] = 2
    elif world['box'] == 9 and world['positions'][2][2] == 0:
        if team == 'University of Delaware':
            world['positions'][2][2] = 1
        else:
            world['positions'][2][2] = 2

############################################################################
# Set up the game
# Don't need to change any of this

if __name__ == '__main__':
    Cisc108Game(World, WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE, INITIAL_WORLD,
                draw_world, update_world, handle_key, handle_mouse,
                handle_motion, handle_release)
    arcade.set_background_color(BACKGROUND_COLOR)
    arcade.run()
