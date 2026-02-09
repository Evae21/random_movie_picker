# random_movie_picker.py (оновлена версія)
import random
import json
import os

MOVIES = {
    "Класика": ["Втеча з Шоушенка", "Хрещений батько", "Бійцівський клуб", "Матриця"],
    "Наукова фантастика": ["Інтерстеллар", "Початок", "Дюна: Частина друга", "Блейд Раннер 2049"],
    "Драми": ["Зелена миля", "Форрест Гамп", "Паразити", "Оппенгеймер"],
    "Комедії": ["Все скрізь і одразу", "Великий Лебовскі", "Суперсімейка"]
}

HISTORY_FILE = "movie_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_history(movie):
    history = load_history()
    history.append(movie)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history[-20:], f, ensure_ascii=False, indent=2)  # останні 20

def pick_movie():
    print("Вибери категорію:")
    for i, cat in enumerate(MOVIES, 1):
        print(f"{i}. {cat}")
    print("0. Випадкова з усіх")

    try:
        choice = int(input("→ ") or "0")
        if choice == 0:
            all_movies = [m for movies in MOVIES.values() for m in movies]
            movie = random.choice(all_movies)
            category = "Випадкова"
        else:
            cat_name = list(MOVIES.keys())[choice - 1]
            movie = random.choice(MOVIES[cat_name])
            category = cat_name
    except:
        print("Невірний вибір → випадковий з усіх")
        all_movies = [m for movies in MOVIES.values() for m in movies]
        movie = random.choice(all_movies)
        category = "Випадкова"

    save_history(f"{movie} ({category})")
    print("\n" + "═" * 50)
    print(f"Сьогодні дивимося: {movie}")
    print(f"Категорія: {category}")
    print("Приємного перегляду! 🍿")
    print("═" * 50)


if __name__ == "__main__":
    input("Натисни Enter, щоб дізнатись, що дивитись сьогодні...\n")
    pick_movie()
