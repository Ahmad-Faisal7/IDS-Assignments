page_a = {1, 2, 3, 5}
page_b = {2, 3, 6, 7}
page_c = {3, 5, 8, 9}

def common_visitors(a, b):
    return a & b

def exclusive_visitors(a, c):
    return (a | c) - (a & c)

def update_page_visitors(a, new_users):
    a.update(new_users)

def remove_page_b_visitors(b, users_to_remove):
    b.difference_update(users_to_remove)

print("Common Visitors:", common_visitors(page_a, page_b))
print("Exclusive Visitors:", exclusive_visitors(page_a, page_c))
update_page_visitors(page_a, {10, 11})
print("Updated Page A:", page_a)
remove_page_b_visitors(page_b, {6, 7})
print("Updated Page B:", page_b)
