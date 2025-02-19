import random


def get_daily_challenge():
    challenges = [
        "Learn a new skill for 15 minutes.",
        "Reflect on a recent mistake and what you learned.",
        "Express gratitude to someone today.",
        "Set a small goal and take one step towards it.",
        "Try a new approach to a problem you're facing.",
        "Refactor a piece of legacy code to improve readability.",
        "Implement a common algorithm from scratch.",
        "Write unit tests for one of your existing projects.",
        "Contribute a pull request to an open-source project.",
        "Optimize an inefficient piece of code for better performance.",
    ]
    return random.choice(challenges)


def get_motivational_quote():
    quotes = [
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "The only way to do great work is to love what you do.",
        "Believe you can and you're halfway there.",
        "Every day is a new beginning. Take a deep breath and start again.",
    ]
    return random.choice(quotes)
