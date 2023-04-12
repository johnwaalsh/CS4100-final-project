from platformer import GameState, Platform
from algorithms import DepthFirstSearch
from main import get_item_location

if __name__ == "__main__":
    grid = \
    [["·", "·", "·", "·", "·", "·", "·", "·", "·", "·", "·", "·"],
    ["⚑", "·", "▦", "▦", "▦", "▦", "▦", "▦", "▦", "▦", "·", "·"],
    ["·", "·", "·", "·", "·", "·", "·", "·", "·", "·", "·", "·"],
    ["·", "·", "·", "·", "·", "·", "·", "·", "·", "·", "▦", "·"],
    ["·", "·", "·", "·", "·", "·", "·", "·", "·", "·", "·", "·"],
    ["☺", "·", "·", "·", "·", "·", "·", "·", "·", "·", "·", "·"],
    ["▦", "·", "▦", "·", "▦", "·", "▦", "·", "▦", "·", "·", "·"]]
    p_loc = get_item_location(grid, "☺")
    goal = get_item_location(grid, "⚑")
    plat_1 = Platform((3, 10), "up")

    game_state = GameState(grid, p_loc, [plat_1], goal)
    game_state.print_state()
    print(game_state.get_legal_moves())

    commands = ['stay', 'stay', 'stay', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_right', 'fall_right', 'stay', 'stay', 'stay', 'stay', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'fall_left']
    gs = game_state
    for command in commands:
        input()
        print(f"Chose {command}")
        gs = gs.get_successor_state(command)
        gs.print_state()
        print(gs.get_legal_moves())