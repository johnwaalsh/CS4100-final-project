class DepthFirstSearch:
    def __init__(self, game_state):
        self.game_state = game_state

    def convert_state_to_str(self, game_state):
        state_str = ""
        state_str += str(game_state.player_location)
        for platform in game_state.platforms:
            state_str += " " + str(platform.location)
            state_str += " " + str(platform.direction)
        return state_str

    def solve(self):
        # store state and path to state
        stack = [(self.convert_state_to_str(self.game_state), self.game_state, [])]
        analyzed = []
        while stack:
            curr_string, curr_state, curr_path = stack.pop(0)
            analyzed.append(curr_string)
            if curr_state.is_win_state():
                return curr_path
            legal_moves = curr_state.get_legal_moves()
            for move in legal_moves:
                successor_state = curr_state.get_successor_state(move[0])
                successor_string = self.convert_state_to_str(successor_state)
                successor_path = curr_path[:]
                successor_path.append(move[0])
                if successor_string not in [s[0] for s in stack] and successor_string not in analyzed:
                    stack.insert(0, (successor_string, successor_state, successor_path))
        print("No path found.")
        return []
