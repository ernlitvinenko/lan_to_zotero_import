#!/usr/bin/env -S uv run
import json

from pyzotero import zotero
from playwright.sync_api import sync_playwright

userId = ""
apiKey = ""


def add_book(lan_url: str):
    zot = zotero.Zotero(userId, "user", apiKey)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(lan_url)
        h1 = page.locator("h1")

        title = h1.text_content()
        authors = page.locator(".authors").all()[0].text_content().split(", ")
        keys = [x.text_content() for x in page.locator("dl.main-props>dt").all()]
        values = [x.text_content() for x in page.locator("dl.main-props>dd").all()]

        props = {x: y for x, y in zip(keys, values)}

        book = zot.item_template("book")
        book["title"] = title

        book["creators"] = [{'creatorType': 'author', 'name': author} for author in authors]

        if "ISBN" in props:
            book["ISBN"] = props["ISBN"]
        if "Год" in props:
            book['date'] = props["Год"]
        if "Страниц" in props:
            book["numPages"] = props["Страниц"]
        if "Издательство" in props:
            book["publisher"] = props["Издательство"]
        book["url"] = lan_url
        book["accessDate"] = "CURRENT_TIMESTAMP"
        resp = zot.create_items([book])
        print(resp)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Добавление источника из ЛАНИ в zotero')
    parser.add_argument("mode", type=str, help="Выбор функции: config - Для сохранения настроек / add - Для добавления в библиотеку")

    parser.add_argument('-l', "--link", type=str, help='Ссылка на лань')
    parser.add_argument("-u", "--user", type=str, help="Идентификатор пользователя Zotero.")
    parser.add_argument("-k", "--api_key", type=str, help="API ключ Zotero.")

    args = parser.parse_args()

    if args.mode == "config":
        with open("settings.json", "w") as file:
            userId = args.user
            apiKey = args.api_key

            d = {"userId": userId, "apiKey": apiKey}
            json.dump(d, file)
            print("Данные успешно сохранены")
    elif args.mode == "add":
        try:
            with open("settings.json") as file:
                d = json.load(file)
                userId = d["userId"]
                apiKey = d["apiKey"]
            add_book(args.link)
        except:
            print("Нет данных аутентификации в zotero")
    else:
        print("Не выбрана функция")
