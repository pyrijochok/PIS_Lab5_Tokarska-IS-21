# PIS_Lab5_Tokarska-IS-21
Вправа 6.1: Обираємо зовнішній сервіс та описуємо сценарій його використання.

Сервіс: The Cat API

Опис сервісу: The Cat API - це безкоштовний API, який надає доступ до великої кількості зображень котів. Цей сервіс дозволяє отримувати випадкові зображення котів, список усіх порід котів, а також інші характеристики, такі як кольори, характер і т. д.

Сценарій використання:
Реєстрація на сайті The Cat API та отримання API ключа.
Створення програми, яка використовує The Cat API для отримання зображень котів.
Запит до API для отримання випадкового зображення кота.
Отримання відповіді в форматі JSON або XML.
Обробка та візуалізація отриманих зображень у власній програмі (наприклад, виведення зображення кота на екран користувача).

Вправа 6.2. Опис прикладу застосування API.
Код знаходиться в файлі awakeApi.py.

Опис прикладу застосування API:
Цей приклад демонструє використання The Cat API для отримання випадкового зображення кота та його відображення користувачу у веб-браузері.

Кроки використання:
1. Отримання випадкового зображення кота:
Функція get_random_cat_image() виконує GET-запит до API The Cat, який повертає випадкове зображення кота у форматі JSON. Після цього зображення отримуються з відповіді та повертаються у вигляді URL.
2. Відображення зображення кота:
Після отримання URL випадкового зображення кота, воно виводиться на екран користувачу за допомогою функції print(). Крім того, зображення автоматично відкривається у веб-браузері користувача за допомогою функції webbrowser.open().
