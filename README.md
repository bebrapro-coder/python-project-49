# Игры разума (Python)

[![hexlet-check](https://github.com/bebrapro-coder/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/bebrapro-coder/python-project-49/actions)

Погрузитесь в экосистему Python и научитесь настраивать рабочее окружение. Подружитесь с менеджером зависимостей и линтером. Поймете, чем git отличается от GitHub, поработаете с внешними репозиториями. Получите опыт построения архитектуры полноценного приложения и написания чистого кода.

Учебный проект Хекслета: https://ru.hexlet.io/programs/python
Как это должно работать: https://asciinema.org/a/l40Lrk3midkLmNEOmgZErGnY7

## Стек

- Python 3.12+
- uv
- Ruff
- Make
- GitHub Actions
- random

## Установка

```bash
git clone https://github.com/bebrapro-coder/python-project-49.git
cd python-project-49
uv sync
make build/uv build
uv tool install --force dist/*.whl
```

## Использование

### Примеры запуска

uv run brain-games/brain-even/brain-calc/brain-gcd/brain-progression/brain-prime
make brain-games/brain-even/brain-calc/brain-gcd/brain-progression/brain-prime
brain-games/brain-even/brain-calc/brain-gcd/brain-progression/brain-prime

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме. Этот репозиторий — один из таких проектов.

## Демонстрация

### Brain-even

https://asciinema.org/a/EzwjxAwBgQE9GoOy

### Brain-calc

https://asciinema.org/a/9fOAv4zcqmjV7sFc 

### Brain-gcd

https://asciinema.org/a/TGFWroFxg6ntfVUo

### Brain-progression

https://asciinema.org/a/Nkdf0ENB619ILvSa

### Brain-prime

https://asciinema.org/a/ySiSDCHJXEAmmwS6
