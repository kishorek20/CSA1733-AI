from collections import deque

start = tuple(map(int, input("Enter 9 numbers (use 0 for blank): ").split()))
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input")
else:
    numbers = [n for n in start if n != 0]
    inversions = sum(
        numbers[i] > numbers[j]
        for i in range(8) for j in range(i + 1, 8)
    )

    if inversions % 2 != 0:
        print("Puzzle cannot be solved")
    else:
        queue = deque([start])
        parent = {start: None}

        while queue:
            state = queue.popleft()

            if state == goal:
                path = []
                while state is not None:
                    path.append(state)
                    state = parent[state]

                path.reverse()

                for step, board in enumerate(path):
                    print("\nStep", step)
                    for i in range(0, 9, 3):
                        print(*board[i:i + 3])

                print("Total moves:", len(path) - 1)
                break

            zero = state.index(0)
            row, col = divmod(zero, 3)

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = row + dr, col + dc

                if 0 <= r < 3 and 0 <= c < 3:
                    pos = r * 3 + c
                    new = list(state)
                    new[zero], new[pos] = new[pos], new[zero]
                    new = tuple(new)

                    if new not in parent:
                        parent[new] = state
                        queue.append(new)
        else:
            print("No solution found")
