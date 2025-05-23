# Скрипт по добавлению библиографии из ЭБС ЛАНЬ в Zotero

## Пердисловие

Данный скрипт позволяет добавить в библиографию zotero книги из ЛАНИ.

## Начало работы

Перед началом работы убедитесь, что вы установили пакетный
менеджер [uv](https://docs.astral.sh/uv/getting-started/installation/).

1. Клонируйте данный репозиторий
1. Введите команду для установки playwright

```bash 
uv run playwright install
```

4. Сделайте файл `main.py` исполняемым:
```bash
sudo chmod +x main.py
```
5. Добавьте свои данные для входа в аккаунт ZOTERO.

```bash
./main.py config -u <ИДЕНТИФИКАТОР_ПОЛЬЗОВАТЕЛЯ_ZOTERO> -k <API_КЛЮЧ_ZOTERO>
```

## Использование

Для добавления книги из лани в библиографию zotero необходимо ввести следующую команду:

```bash
./main.py add -l <ССЫЛКА_НА_КНИГУ_ИЗ_ЛАНИ>
```

### Пример
```bash
./main.py add -l https://e.lanbook.com/book/439523
```
Добавится книга: "Программирование на языке C#: учебное пособие"

---
При возникших вопросах обращаться 
- TG: https://t.me/ernestlitvinenko
- E-mail: [ernest@elitvinenko.tech](mailto:ernest@elitvinenko.tech)
