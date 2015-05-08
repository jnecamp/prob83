import Queue
import sys

TEST_FILES_AND_ANS = [('tests/simple_test_1.txt', 9),
                      ('tests/simple_test_2.txt', 15),
                      ('tests/simple_test_3.txt', 13),
                      ('tests/medium_test.txt', 2297)]

def load_matrix_from_file(filename):
    matrix = []
    min_val = float("inf")
    num_columns = 0
    with open(filename, 'r') as f:
        for line in f:
            row = map(int, line.rstrip('\n').split(','))
            if num_columns == 0:
                num_columns = len(row)
            else:
                assert num_columns == len(row), "Given matrix has irregular dimension"
            min_val = min(min(row),min_val)
            matrix.append(row)
    return matrix, min_val

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_min_possible_cost(p1, p2, heur_val):
    return manhattan_distance(p1, p2) * heur_val

def get_neighbor_points(point, max_row, max_col):
    neighbors = []
    up = (point[0] - 1, point[1])
    if up[0] >= 0: neighbors.append(up)
    down = (point[0] + 1, point[1])
    if down[0] <= max_row: neighbors.append(down)
    left = (point[0], point[1] - 1)
    if left[1] >= 0: neighbors.append(left)
    right = (point[0], point[1] + 1)
    if right[1] <= max_col: neighbors.append(right)
    return neighbors

def find_min_cost_path(matrix, heur_val):
    max_row = len(matrix) - 1
    max_col = len(matrix[0]) - 1
    start_point = (0,0)
    end_point = (max_row, max_col)
    explored = set()
    to_explore = Queue.PriorityQueue()
    this_cost = matrix[start_point[0]][start_point[1]]
    to_explore.put((get_min_possible_cost(start_point, end_point, heur_val) + this_cost, this_cost, start_point))
    while not to_explore.empty():
        min_pos_cost, cur_cost,  cur_point = to_explore.get()
        if cur_point == end_point:
            return cur_cost
        if cur_point in explored:
            continue
        for neighbor in get_neighbor_points(cur_point, max_row, max_col):
            if neighbor in explored:
                continue
            this_cost = matrix[neighbor[0]][neighbor[1]]
            to_explore.put((this_cost + cur_cost + get_min_possible_cost(neighbor, end_point, heur_val), this_cost + cur_cost, neighbor))
        else:
            explored.add(cur_point)
    raise Exception("A minimum path should be found")

if __name__ == "__main__":
    arg = sys.argv[1]
    if arg == "--test":
        for test_file, gold_ans in TEST_FILES_AND_ANS:
            matrix, min_val = load_matrix_from_file(test_file)
            calc_ans = find_min_cost_path(matrix, min_val)
            assert gold_ans == calc_ans, "%s --- Expected answer: %d, Your answer: %d" % (test_file, gold_ans, calc_ans)
    else:
        matrix_filename = sys.argv[1]
        matrix, min_val = load_matrix_from_file(matrix_filename)
        print find_min_cost_path(matrix, min_val)

