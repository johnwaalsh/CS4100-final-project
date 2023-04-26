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

    commands_bfs = ['stay', 'stay', 'stay', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_right', 'fall_right', 'stay', 'stay', 'stay', 'stay', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'fall_left']
    commands_as = ['stay', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_right', 'fall_right', 'jump', 'fall_left', 'fall_right', 'jump', 'fall_down', 'stay', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'fall_left']
    commands_dfs = ['jump', 'fall_right', 'fall_left', 'fall_down', 'jump', 'fall_right', 'fall_left', 'fall_down', 'jump', 'fall_right', 'fall_right', 'fall_down', 'jump', 'fall_right', 'fall_right', 'fall_down', 'jump', 'fall_left', 'fall_right', 'fall_down', 'jump', 'fall_left', 'fall_right', 'fall_down', 'jump', 'fall_right', 'fall_right', 'fall_down', 'jump', 'fall_right', 'fall_left', 'fall_down', 'jump', 'fall_right', 'fall_left', 'fall_down', 'jump', 'fall_right', 'fall_right', 'fall_down', 'jump', 'fall_right', 'fall_down', 'fall_left', 'jump', 'fall_right', 'fall_down', 'fall_left', 'stay', 'stay', 'jump', 'fall_left', 'fall_left', 'fall_down', 'jump', 'fall_left', 'fall_left', 'fall_down', 'jump', 'fall_left', 'fall_left', 'fall_down', 'jump', 'fall_left', 'fall_left', 'fall_down', 'jump', 'fall_right', 'fall_left', 'fall_down', 'jump', 'fall_right', 'fall_left', 'fall_down', 'stay', 'jump', 'fall_right', 'fall_right', 'fall_down', 'jump', 'fall_left', 'fall_right', 'fall_down', 'jump', 'fall_right', 'fall_right', 'fall_down', 'jump', 'fall_left', 'fall_right', 'fall_down', 'jump', 'fall_right', 'fall_right', 'fall_down', 'jump', 'fall_left', 'fall_right', 'fall_down', 'jump', 'fall_right', 'fall_right', 'fall_down', 'jump', 'fall_right', 'fall_right', 'jump', 'fall_down', 'stay', 'stay', 'left', 'right', 'left', 'left', 'right', 'left', 'right', 'left','right', 'left', 'right', 'left', 'left', 'left', 'right', 'left', 'left', 'right', 'left', 'right', 'left', 'right', 'left', 'right', 'left', 'left', 'left', 'right', 'left', 'left', 'right', 'left', 'right', 'left', 'right', 'left', 'right', 'left', 'left', 'fall_left']
    commands_q = ['jump', 'fall_right', 'fall_down', 'fall_right', 'stay', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_down', 'fall_right', 'fall_right', 'jump', 'fall_right', 'fall_down', 'fall_right', 'stay', 'jump', 'fall_right', 'fall_right', 'stay', 'stay', 'stay', 'stay', 'stay', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'fall_left']
    gs = game_state
    for command in commands_q:
        input()
        print(f"Chose {command}")
        gs = gs.get_successor_state(command)
        gs.print_state()
        print(gs.get_legal_moves())