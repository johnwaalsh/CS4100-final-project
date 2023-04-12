from platformer import GameState, Platform
from algorithms import DepthFirstSearch

if __name__ == "__main__":
    test_game_grid_2 = [["V", "V", "V"],["V", "V", "V"],["V", "B", "G"],["P", "V", "V"],["B", "V", "B"]]
    test_game_grid_2_p_loc = (0, 3)
    test_game_grid_2_plat = Platform((2, 1), "up")
    test_game_grid_2_goal = (2, 2)

    game_state = GameState(test_game_grid_2, test_game_grid_2_p_loc, [test_game_grid_2_plat], test_game_grid_2_goal)
    game_state.print_state()

    dfs = DepthFirstSearch(game_state)
    dfs_sol = dfs.solve()
    print(dfs_sol)

