# food_recommender.py
import random

food_data = {
    "happy": ["Ice cream", "Sushi", "Bibimbap", "Pancakes", "Fruit salad"],
    "sad": ["Chicken soup", "Ramen", "Grilled cheese", "Hot porridge", "Chocolate cake"],
    "angry": ["Spicy ramen", "Korean fried chicken", "Tteokbokki", "Steak"],
    "neutral": ["Sandwich", "Rice bowl", "Salad", "Pasta"]
}

def recommend_food(mood, k=3):
    mood = mood.lower()
    options = food_data.get(mood, food_data["neutral"]).copy()
    random.shuffle(options)
    return options[:k]
