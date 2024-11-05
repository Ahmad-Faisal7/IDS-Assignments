user_data = [
    (1, "John", 35, "USA"),
    (2, "Emma", 22, "Canada"),
    (3, "Oliver", 45, "UK"),
    (4, "Liam", 32, "USA"),
    (5, "Sophia", 29, "Australia"),
    (6, "James", 28, "Canada"),
    (7, "Ava", 31, "USA"),
    (8, "Mia", 33, "Canada"),
    (9, "Lucas", 37, "Canada"),
    (10, "Charlotte", 24, "USA"),
    (11, "John", 40, "Canada"),
]

def filter_and_extract(users):
    selected_names = [u[1] for u in users if u[2] > 30 and u[3] in ('USA', 'Canada')]
    return selected_names

def find_oldest_and_duplicates(users):
    sorted_users = sorted(users, key=lambda x: x[2], reverse=True)[:10]
    names = [u[1] for u in users]
    duplicate_names = [name for name in set(names) if names.count(name) > 1]
    return sorted_users, duplicate_names


print("Filtered Names:", filter_and_extract(user_data))
top_oldest, duplicates = find_oldest_and_duplicates(user_data)
print("Top 10 Oldest Users:", top_oldest)
print("Duplicate Names:", duplicates)
