Monthly_Challenges = {
    "January": "Eat no meat for the entire month",
    "February": "Walk for at least 20 minutes every day!",
    "March": "Learn Django for at least 20 minutes every day!",
    "April": "Learn python for at least 1 hour every day!",
    "May": "Swim for at least 30 minutes every day!",
    "June": "Horse riding at least one hour every day!",
    "July": "Code every day for at least 40 mins",
    "August": "Practice Meditation Every day",
    "September": "Practice Yoga EVery day for atleast thirty minutes!",
    "October": "Learn Ethical Hacking every day!",
    "November": None,
    "December": "Wrap up all the projects for the year"
}
list_page_title = "Welcome to monthly challenges"
current_context_not_available = "Sorry the current context that you are looking for is not available please try again later"

def get_month_by_number(month):
     return list(Monthly_Challenges)[month - 1]

def get_monthly_context(month):
    current_context = [v for k, v in Monthly_Challenges.items() if month.capitalize() in k]
    return current_context[0]