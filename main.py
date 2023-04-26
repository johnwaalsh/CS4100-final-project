from platformer import GameState, Platform
from algorithms import DepthFirstSearch, BreadthFirstSearch, AStarSearch, QLearner

def get_item_location(game_grid, item):
    for rn, r in enumerate(game_grid):
        for cn, c in enumerate(r):
            if r[cn] == item:
                return (cn, rn)

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

    print("\nDFS")
    dfs = DepthFirstSearch(game_state)
    dfs_sol = dfs.solve()
    print(dfs_sol)
    print(len(dfs_sol))


    print("\nBFS")
    bfs = BreadthFirstSearch(game_state)
    bfs_sol = bfs.solve()
    print(bfs_sol)
    print(len(bfs_sol))


    print("\nA*S")
    astar = AStarSearch(game_state)
    astar_sol = astar.solve()
    print(astar_sol)
    print(len(astar_sol))

    print("\nQ-Learning")
    qlearn = QLearner(game_state)
    qlearn_sol = qlearn.solve()
    print(qlearn_sol)
    print(len(qlearn_sol))


