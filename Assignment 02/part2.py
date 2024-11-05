transactions = [
    (1001, 1, 500, '2024-10-10'),
    (1002, 2, 1500, '2024-10-11'),
    (1003, 3, 700, '2024-10-12'),
    (1004, 1, 800, '2024-10-13'),
    (1005, 4, 400, '202-10-14'),
]

def find_unique_users(trans):
    unique_users = set([t[1] for t in trans])
    return len(unique_users)

def find_highest_transaction(trans):
    return max(trans, key=lambda x: x[2])

def split_transactions(trans):
    ids = [t[0] for t in trans]
    user_ids = [t[1] for t in trans]
    return ids, user_ids

print("Unique Users:", find_unique_users(transactions))
print("Highest Transaction:", find_highest_transaction(transactions))
ids_list, user_ids_list = split_transactions(transactions)
print("Transaction IDs:", ids_list)
print("User IDs:", user_ids_list)
