feedback_a = {
    1: {'rating': 5, 'comments': 'Great service'},
    2: {'rating': 3, 'comments': 'Good'},
    3: {'rating': 4, 'comments': 'Satisfactory'}
}
feedback_b = {
    2: {'rating': 4, 'comments': 'Improved'},
    4: {'rating': 2, 'comments': 'Bad experience'},
    5: {'rating': 5, 'comments': 'Excellent'}
}

def high_raters(feedback):
    return {k: v['rating'] for k, v in feedback.items() if v['rating'] >= 4}

def merge_feedbacks(fb_a, fb_b):
    merged = fb_a.copy()
    for user, details in fb_b.items():
        if user in merged:
            merged[user]['rating'] = max(merged[user]['rating'], details['rating'])
            merged[user]['comments'] += "; " + details['comments']
        else:
            merged[user] = details
    return merged

def top_ratings(feedback):
    return sorted(feedback.items(), key=lambda x: x[1]['rating'], reverse=True)[:5]

print("High Raters:", high_raters(feedback_a))
merged_feedback = merge_feedbacks(feedback_a, feedback_b)
print("Merged Feedback:", merged_feedback)
print("Top 5 Ratings:", top_ratings(merged_feedback))
