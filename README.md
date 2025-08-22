# pwgen
Простий генератор безпечних паролів на Python. Використовує `secrets`, гарантує хоча б по одному символу з вибраних наборів.

## Вимоги
- Python 3.10+

## Використання
```bash
# 16 символів за замовчуванням
python pwgen.py

# 24 символи
python pwgen.py -n 24

# Без символів
python pwgen.py --no-symbols

# Тільки нижній регістр + цифри
python pwgen.py --no-upper --no-symbols
