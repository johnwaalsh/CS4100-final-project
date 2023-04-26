from queue import PriorityQueue
import random

class SearchAlgorithm:
    def __init__(self, game_state):
        self.game_state = game_state
        self.goal_location = game_state.goal_location

    def convert_state_to_str(self, game_state):
        state_str = ""
        state_str += str(game_state.player_location)
        for platform in game_state.platforms:
            state_str += " " + str(platform.location)
            state_str += " " + str(platform.direction)
        return state_str

class DepthFirstSearch(SearchAlgorithm):
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

class BreadthFirstSearch(SearchAlgorithm):
    def solve(self):
        # store state and path to state
        queue = [(self.convert_state_to_str(self.game_state), self.game_state, [])]
        analyzed = []
        while queue:
            curr_string, curr_state, curr_path = queue.pop()
            analyzed.append(curr_string)
            if curr_state.is_win_state():
                return curr_path
            legal_moves = curr_state.get_legal_moves()
            for move in legal_moves:
                successor_state = curr_state.get_successor_state(move[0])
                successor_string = self.convert_state_to_str(successor_state)
                successor_path = curr_path[:]
                successor_path.append(move[0])
                if successor_string not in [s[0] for s in queue] and successor_string not in analyzed:
                    queue.insert(0, (successor_string, successor_state, successor_path))
        print("No path found.")
        return []

class AStarSearch(SearchAlgorithm):
    def heuristic(self, successor_string):
        parsed = successor_string.split(")")[0].split("(")[1].replace(",", "").split(" ")
        parsed_tuple = (int(parsed[0]), int(parsed[1]))
        dist = abs(self.goal_location[0] - parsed_tuple[0]) + abs(self.goal_location[1] - parsed_tuple[1])
        return dist


    def solve(self):
        # store state and path to state
        queue = PriorityQueue()
        queue.put((0, (self.convert_state_to_str(self.game_state), self.game_state, [])))
        analyzed = []
        while queue:
            curr_string, curr_state, curr_path = queue.get()[1]
            analyzed.append(curr_string)
            if curr_state.is_win_state():
                return curr_path
            legal_moves = curr_state.get_legal_moves()
            for move in legal_moves:
                successor_state = curr_state.get_successor_state(move[0])
                successor_string = self.convert_state_to_str(successor_state)
                successor_path = curr_path[:]
                successor_path.append(move[0])
                if successor_string not in [s[1][0] for s in queue.queue] and successor_string not in analyzed:
                    queue.put((len(successor_path) + self.heuristic(successor_string), (successor_string, successor_state, successor_path)))
        print("No path found.")
        return []

class QLearner(SearchAlgorithm):
    def solve(self):
        learning_rate = 0.5
        gamma = 0.9

        # Initialize Q table
        Q_table = {}
        start_states = self.game_state.get_possible_states()
        for state in start_states:
            str_rep = self.convert_state_to_str(state)
            moves = state.get_legal_moves()
            move_dict = {}
            for move in moves:
                move_dict[move[0]] = 1
            if not moves:
                move_dict["anything"] = 0
            Q_table[str_rep] = move_dict

        selection_options = ["greedy", "random"]

        # Run training
        num_episodes = 10000
        num_steps = 10000
        for episode in range(num_episodes):
            start_state = random.choice(start_states)
            curr_state = start_state
            for step in range(num_steps):
                str_rep = self.convert_state_to_str(curr_state)
                curr_moves = curr_state.get_legal_moves()
                selection = random.choice(selection_options)
                if curr_state.is_lose_state() or curr_state.is_win_state():
                    break
                if selection == "random":
                    next_move = random.choice(curr_moves)[0]
                else:
                    q_details = Q_table[str_rep]
                    fixed_q_details = {move[0]: q_details[move[0]] for move in curr_moves}
                    next_move = max(q_details, key=fixed_q_details.get)
                next_state = curr_state.get_successor_state(next_move)
                if next_state.is_lose_state():
                    reward = -100
                elif next_state.is_win_state():
                    reward = 100
                else:
                    reward = 0
                next_str_rep = self.convert_state_to_str(next_state)
                next_q_details = Q_table[next_str_rep]
                Q_table[str_rep][next_move] = Q_table[str_rep][next_move] + (learning_rate * (reward + (gamma*(max(next_q_details.values()))) - Q_table[str_rep][next_move]))
                curr_state = next_state

        # Get solution
        curr_state = self.game_state
        path = []
        for i in range(1000):
            if curr_state.is_lose_state():
                print("Couldn't find optimal path")
                break
            elif curr_state.is_win_state():
                break
            str_rep = self.convert_state_to_str(curr_state)
            q_details = Q_table[str_rep]
            next_move = max(q_details, key=q_details.get)
            path.append(next_move)
            curr_state = curr_state.get_successor_state(next_move)
        return path
