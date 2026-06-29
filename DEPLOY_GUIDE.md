# Telegram Bio Animation - Docker + Railway

## 🚀 Как это работает

Скрипт будет работать **24/7 в облаке** на **Railway.app** (бесплатно!)

---

## 📋 Шаг 1: Получи API ключи Telegram

1. Открой https://my.telegram.org/apps
2. Залогинься в свой Telegram аккаунт
3. Нажми "Create new application"
4. Заполни форму (название, описание - что угодно)
5. Получишь:
   - **API_ID** (число)
   - **API_HASH** (строка)
6. **Сохрани эти два значения!** 📝

---

## 🐳 Шаг 2: Подготовка файлов

Тебе нужны **4 файла** (уже готовы выше):

```
📁 telegram-bio-animation/
├── telegram_bio_animation.py
├── requirements.txt
├── Dockerfile
└── .gitignore (создашь)
```

### Создай файл `.gitignore`:
```
session_name.session
session_name.session-journal
__pycache__/
*.pyc
.env
```

---

## 🌐 Шаг 3: GitHub репозиторий

1. **Создай GitHub аккаунт** (если нет): https://github.com/signup

2. **Создай новый репозиторий:**
   - Кнопка "+" в правом углу → "New repository"
   - Имя: `telegram-bio-animation`
   - Выбери "Public"
   - Нажми "Create repository"

3. **Загрузи файлы:**
   ```bash
   # Или используй GitHub Desktop (проще)
   # Или просто drag-n-drop файлы в веб-интерфейс GitHub
   ```

---

## 🚀 Шаг 4: Развёртывание на Railway

1. **Открой https://railway.app**

2. **Зарегистрируйся через GitHub**
   - Нажми "Deploy Now"
   - Авторизуйся через GitHub

3. **Выбери репозиторий:**
   - Выбери `telegram-bio-animation`
   - Нажми "Deploy"

4. **Установи переменные окружения:**
   - В Railway перейди в проект
   - Вкладка "Variables"
   - Добавь три переменные:
     ```
     API_ID = (твой API_ID с my.telegram.org)
     API_HASH = (твой API_HASH с my.telegram.org)
     PHONE = +79xxxxxxxxx (твой номер в формате +7...)
     ```

5. **Нажми Deploy**
   - Railway автоматически загрузит Docker контейнер
   - Скрипт запустится

6. **Первая авторизация:**
   - Откроется логирование в Railway
   - Скрипт попросит ввести код подтверждения
   - Открой Telegram, найди сообщение от Telegram
   - Введи код в логи Railway
   - Готово! ✅

---

## 📱 Что дальше?

После первой авторизации скрипт будет:
- ✅ Работать 24/7 в облаке
- ✅ Автоматически обновлять твою биографию
- ✅ Запускать анимацию каждые N секунд
- ✅ Не требует твой ноут включённым

---

## ⚙️ Как изменить настройки

Если хочешь изменить текст анимации (Lewis/Hamilton/KZT):

1. **Открой файл** `telegram_bio_animation.py`
2. **Найди строки:**
   ```python
   PREFIX = 'Lewis'
   ANIMATE = 'Hamilton'
   SUFFIX = '| KZT'
   ERROR_CHARS = 'nnn'
   SPEED = 0.08  # скорость печати
   CYCLE_PAUSE = 3  # пауза между циклами
   ```
3. **Измени на свои значения**
4. **Commit → Push в GitHub**
5. **Railway автоматически перезагрузит бота** ✅

---

## 🆘 Решение проблем

### "Authorization failed"
- Проверь что **PHONE** в формате **+7xxxxxxxxx** (с плюсом)
- Проверь что вводишь **правильный код** из Telegram

### "No module named telethon"
- Railway автоматически установит всё из requirements.txt
- Просто подожди минуту после deploy

### "Bio not updating"
- Телеграм иногда ограничивает частоту обновлений
- Увеличь **CYCLE_PAUSE = 5** (пауза между циклами)

---

## 💚 Готово!

Теперь твой бот работает **24/7 в облаке**! 🚀

**Любые вопросы - пиши!**
