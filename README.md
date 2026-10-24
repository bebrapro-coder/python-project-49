# Игры разума (Python)

[![hexlet-check](https://github.com/bebrapro-coder/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/bebrapro-coder/python-project-49/actions)

Погрузитесь в экосистему Python и научитесь настраивать рабочее окружение. Подружитесь с менеджером зависимостей и линтером. Поймете, чем git отличается от GitHub, поработаете с внешними репозиториями. Получите опыт построения архитектуры полноценного приложения и написания чистого кода.

Учебный проект Хекслета: https://ru.hexlet.io/programs/python
Как это должно работать: https://asciinema.org/a/l40Lrk3midkLmNEOmgZErGnY7

## Описание проекта

«Игры разума» — набор из пяти консольных мини-игр на сообразительность.
Каждая игра задаёт три вопроса подряд: чтобы победить, нужно ответить
верно на все три. Первая же ошибка заканчивает игру.

| Команда | Задача игрока |
|---|---|
| `brain-even` | определить, чётное ли число |
| `brain-calc` | посчитать арифметическое выражение |
| `brain-gcd` | найти наибольший общий делитель двух чисел |
| `brain-progression` | найти пропущенное число в арифметической прогрессии |
| `brain-prime` | определить, простое ли число |

Проект выполнен в рамках курса Python от [Хекслета](https://ru.hexlet.io/programs/python).

## Минимальные требования

- Python 3.12+
- [uv] https://docs.astral.sh/uv/getting-started/installation/
- Git
- Make(опционально)
- Linux, macOS или Windows через WSL

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

### brain-games

[![asciicast](https://asciinema.org/a/gi8NqW46kawLRBg5.svg)](https://asciinema.org/a/gi8NqW46kawLRBg5)

### brain-even

[![asciicast](https://asciinema.org/a/EzwjxAwBgQE9GoOy.svg)](https://asciinema.org/a/EzwjxAwBgQE9GoOy)

### brain-calc

[![asciicast](https://asciinema.org/a/9fOAv4zcqmjV7sFc.svg)](https://asciinema.org/a/9fOAv4zcqmjV7sFc)

### brain-gcd

[![asciicast](https://asciinema.org/a/TGFWroFxg6ntfVUo.svg)](https://asciinema.org/a/TGFWroFxg6ntfVUo)

### brain-progression

[![asciicast](https://asciinema.org/a/Nkdf0ENB619ILvSa.svg)](https://asciinema.org/a/Nkdf0ENB619ILvSa)

### brain-prime

[![asciicast](https://asciinema.org/a/ySiSDCHJXEAmmwS6.svg)](https://asciinema.org/a/ySiSDCHJXEAmmwS6)
