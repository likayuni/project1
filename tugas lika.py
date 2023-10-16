from collections import deque

# Definisi status awal dan status tujuan
initial_state = (1, 1, 1, 1)  # (peternak, sayuran, kambing, serigala)
goal_state = (0, 0, 0, 0)

# Fungsi untuk memeriksa apakah status saat ini valid
def is_valid_state(state):
    peternak, sayuran, kambing, serigala = state
    # Pengecualian jika kambing dimakan oleh serigala atau sayuran dimakan oleh kambing
    if (sayuran == 0 and kambing == 1) or (kambing == 0 and serigala == 1):
        return False
    return True

# Fungsi untuk menghasilkan langkah-langkah berikutnya
def generate_next_states(current_state):
    possible_moves = []
    peternak, sayuran, kambing, serigala = current_state
    for delta_p, delta_s, delta_k, delta_g in [(1, 0, 0, 0), (-1, 0, 0, 0), (1, 1, 0, 0), (-1, -1, 0, 0), (1, 0, 1, 0), (-1, 0, -1, 0), (1, 0, 0, 1), (-1, 0, 0, -1)]:
        new_state = (peternak + delta_p, sayuran + delta_s, kambing + delta_k, serigala + delta_g)
        if 0 <= new_state[0] <= 1 and 0 <= new_state[1] <= 1 and 0 <= new_state[2] <= 1 and 0 <= new_state[3] <= 1 and is_valid_state(new_state):
            possible_moves.append(new_state)
    return possible_moves

# Fungsi untuk mencari solusi dengan BFS
def breadth_first_search(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path + [current_state]
        if current_state not in visited:
            visited.add(current_state)
            for next_state in generate_next_states(current_state):
                queue.append((next_state, path + [current_state]))

    return None

# Jalankan algoritma BFS dan cetak langkah-langkahnya
solution = breadth_first_search(initial_state, goal_state)
if solution:
    for i, state in enumerate(solution):
        print(f"Langkah {i}: {state}")
else:
    print("Tidak ada solusi yang ditemukan.")
