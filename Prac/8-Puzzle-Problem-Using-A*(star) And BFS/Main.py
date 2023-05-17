# Define a function to calculate the Manhattan distance between two cells
def manhattan_distance(cell1, cell2):
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

# Define a function to calculate the heuristic cost of a state
def heuristic_cost(state):
    cost = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_position = ((state[i][j]-1)//3, (state[i][j]-1)%3)
                cost += manhattan_distance((i, j), goal_position)
    return cost

# Define a function to generate the successors of a state
def generate_successors(state):
    successors = []
    i, j = find_empty(state)
    if i > 0:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        successors.append(new_state)
    if i < 2:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
        successors.append(new_state)
    if j > 0:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
        successors.append(new_state)
    if j < 2:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
        successors.append(new_state)
    return successors

# Define the A* search algorithm
def astar_search(initial_state, goal_state):
    frontier = [(heuristic_cost(initial_state), 0, initial_state)]
    visited = set()
    while frontier:
        _, depth, state = frontier.pop(0)
        if state == goal_state:
            print("Reached goal state with depth {} and F = {}".format(depth, heuristic_cost(state)))
            return True
        visited.add(str(state))
        for successor in generate_successors(state):
            if str(successor) not in visited:
                cost = heuristic_cost(successor)
                F = depth + cost
                frontier.append((F, depth+1, successor))
                print("Expanded node with depth {} and F = {}: ".format(depth+1, F))
                for row in successor:
                    print(row)
                print("")
        frontier.sort()
    return False

# Function to get user input for the initial state
def get_user_input():
    print("Enter the initial state of the puzzle (use 0 for the empty space):")
    initial_state = []
    for i in range(3):
        row = input("Enter numbers for row {} (separated by spaces): ".format(i+1))
        row = list(map(int, row.split()))
        initial_state.append(row)
    return initial_state

# Function to get user input for the goal state
def get_goal_state():
    print("Enter the goal state of the puzzle (use 0 for the empty space):")
    goal_state = []
    for i in range(3):
        row = input("Enter numbers for row {} (separated by spaces): ".format(i+1))
        row = list(map(int, row.split()))
        goal_state.append(row)
    return goal_state

# Function to get user input for the goal state
def get_goal_state():
    print("Enter the goal state of the puzzle (use 0 for the empty space):")
    goal_state = []
    for i in range(3):
        row = input("Enter numbers for row {} (separated by spaces): ".format(i+1))
        row = list(map(int, row.split()))
        goal_state.append(row)
    return goal_state

# Play the game
initial_state = get_user_input()
goal_state = get_goal_state()

print("\nThe goal state is:")
for row in goal_state:
    print(row)

# Search for the solution
solution_found = astar_search(initial_state, goal_state)

if solution_found:
    print("The puzzle has a solution!")
else:
    print("The puzzle does not have a solution.")
