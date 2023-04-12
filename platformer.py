from copy import deepcopy

inverted_directions = {"left": "right", "right": "left", "up":"down", "down":"up"}

class Platform:
    def __init__(self, location, direction):
        # y, x
        self.location = location
        self.direction = direction

    def next_location(self):
        if self.direction == "left":
            return (self.location[0], self.location[1]-1)
        elif self.direction == "right":
            return (self.location[0], self.location[1]+1)
        elif self.direction == "up":
            return (self.location[0]-1, self.location[1])
        elif self.direction == "down":
            return (self.location[0]+1, self.location[1])

class GameState:
    def __init__(self, game_grid, player_location, platforms, goal_location):
        self.player_location = player_location
        self.game_grid = game_grid
        self.platforms = platforms
        self.goal_location = goal_location
        self.width = len(self.game_grid[0])
        self.height = len(self.game_grid)

    def print_state(self):
        for rn, row in enumerate(self.game_grid):
            for cn, col in enumerate(row):
                print(row[cn], end=" ")
            print("")

    def is_win_state(self):
        return self.player_location == self.goal_location

    def is_lose_state(self):
        return self.get_legal_moves() == []

    def validate_coord(self, coord):
        return coord[0] >= 0 and coord[0] < self.height and coord[1] >= 0 and coord[1] < self.width

    def update_platforms(self):
        next_grid = deepcopy(self.game_grid)
        next_platforms = []
        for platform in self.platforms:
            predicted_location = platform.next_location()
            if self.validate_coord(predicted_location) and self.game_grid[predicted_location[0]][predicted_location[1]] in ["V", "P"]:
                next_location = predicted_location
                next_platform = Platform(predicted_location, platform.direction)
            else:
                temp_platform = Platform(platform.location, inverted_directions[platform.direction])
                reverse_location = temp_platform.next_location()
                if self.validate_coord(reverse_location) and self.game_grid[reverse_location[0]][reverse_location[1]] in ["V", "P"]:
                    next_location = reverse_location
                    next_platform = Platform(reverse_location, temp_platform.direction)
                else:
                    next_location = platform.location
                    next_platform = platform
            next_grid[platform.location[0]][platform.location[1]] = "V"
            next_grid[next_location[0]][next_location[1]] = "B"
            next_platforms.append(next_platform)
        return next_grid, next_platforms

    def get_legal_moves(self):
        x_coord = self.player_location[0]
        y_coord = self.player_location[1]
        legal = []
        left = ("left", (y_coord, x_coord-1))
        right = ("right", (y_coord, x_coord+1))
        jump_1 = ("jump", (y_coord-1, x_coord))
        jump_2 = ("jump", (y_coord-2, x_coord))
        jump_3 = ("jump", (y_coord-3, x_coord))
        # Spaces that the player can move into
        accessible = ["V", "G"]

        # simulate platform movement
        # what are we currently standing on?
        if y_coord+1 >= self.height:
            return []
        else:
            curr_on = self.game_grid[y_coord+1][x_coord]
        next_grid, next_platforms = self.update_platforms()
        # if we were on a platform, and the platform will move away, you can still move with the platform
        if next_grid[y_coord+1][x_coord] in accessible and curr_on == "B":
            next_grid[y_coord+1][x_coord] = "B"

        # if we're falling, only valid options are straight down, down right, down left
        fall_down = ("fall_down", (y_coord+1, x_coord))
        fall_right = ("fall_right", (y_coord+1, x_coord+1))
        fall_left = ("fall_left", (y_coord+1, x_coord-1))
        if self.validate_coord(fall_down[1]) and next_grid[fall_down[1][0]][fall_down[1][1]] in accessible:
            legal.append(fall_down)
            if self.validate_coord(fall_right[1]) and next_grid[fall_right[1][0]][fall_right[1][1]] in accessible:
                legal.append(fall_right)
            if self.validate_coord(fall_left[1]) and next_grid[fall_left[1][0]][fall_left[1][1]] in accessible:
                legal.append(fall_left)
            return legal

        # are we on a platform moving up?
        if self.game_grid[y_coord+1][x_coord] == "B" and next_grid[y_coord][x_coord] == "B":
            stay_option = ("stay", (y_coord-1, x_coord))
            if self.validate_coord(stay_option[1]) and next_grid[stay_option[1][0]][stay_option[1][1]] in accessible:
                legal.append(stay_option)
        else:
            legal.append(("stay", (y_coord, x_coord)))

        # if we're not falling, we can move left or right
        for possible in [left, right]:
            if self.validate_coord(possible[1]) and next_grid[possible[1][0]][possible[1][1]] in accessible:
                    legal.append(possible)
        # or we can jump
        if self.validate_coord(jump_1[1]) and next_grid[jump_1[1][0]][jump_1[1][1]] in accessible:
            if self.validate_coord(jump_2[1]) and next_grid[jump_2[1][0]][jump_2[1][1]] in accessible:
                if self.validate_coord(jump_3[1]) and next_grid[jump_3[1][0]][jump_3[1][1]] in accessible:
                    legal.append(jump_3)

        return legal

    def get_successor_state(self, action):
        legal_moves = self.get_legal_moves()
        if action not in [move[0] for move in legal_moves]:
            raise ValueError(f"{action} is an invalid move")
        x_coord = self.player_location[0]
        y_coord = self.player_location[1]
        next_grid, next_platforms = self.update_platforms()
        left_behind = "V"
        accessible = ["V", "G"]

        if action == "stay":
            if self.game_grid[y_coord+1][x_coord] == "B" and next_grid[y_coord][x_coord] == "B":
                stay_coords = (y_coord-1, x_coord)
                if self.validate_coord(stay_coords) and next_grid[stay_coords[0]][stay_coords[1]] in accessible:
                    new_player_location = (stay_coords[1], stay_coords[0])
                    left_behind = "B"
            else:
                new_player_location = (self.player_location[0], self.player_location[1])
        elif action == "left":
            new_player_location = (self.player_location[0]-1, self.player_location[1])
        elif action == "right":
            new_player_location = (self.player_location[0]+1, self.player_location[1])
        elif action == "jump":
            new_player_location = (self.player_location[0], self.player_location[1]-3)
        elif action == "fall_down":
            new_player_location = (self.player_location[0], self.player_location[1]+1)
        elif action == "fall_right":
            new_player_location = (self.player_location[0]+1, self.player_location[1]+1)
        elif action == "fall_left":
            new_player_location = (self.player_location[0]-1, self.player_location[1]+1)
        else:
            raise ValueError(f"action {action} is invalid.")

        new_game_grid = deepcopy(next_grid)
        new_game_grid[self.player_location[1]][self.player_location[0]] = left_behind
        new_game_grid[new_player_location[1]][new_player_location[0]] = "P"

        return GameState(new_game_grid, new_player_location, next_platforms, self.goal_location)

if __name__ == "__main__":
    test_game_grid = [["V", "V", "V"],["V", "V", "V"],["V", "B", "V"],["P", "V", "V"],["B", "B", "B"]]
    test_game_grid_p_loc = (0, 3)
    test_game_grid_plat = Platform((2, 1), "right")

    test_game_grid_2 = [["V", "V", "V"],["V", "V", "V"],["V", "B", "G"],["P", "V", "V"],["B", "V", "B"]]
    test_game_grid_2_p_loc = (0, 3)
    test_game_grid_2_plat = Platform((2, 1), "up")
    test_game_grid_2_goal = (2, 2)

    game_state = GameState(test_game_grid_2, test_game_grid_2_p_loc, [test_game_grid_2_plat], test_game_grid_2_goal)
    game_state.print_state()
    print(game_state.get_legal_moves())

    commands = ["jump", "fall_right", "fall_right"]
    gs = game_state
    for command in commands:
        input()
        gs = gs.get_successor_state(command)
        gs.print_state()
        print(gs.is_win_state())
        print(gs.is_lose_state())
        print(gs.get_legal_moves())
