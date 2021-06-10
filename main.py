from app import TikiProvider, write_json

providers = [TikiProvider]


def get_users(save):
    items = {}
    for cls in providers:
        provider = cls()
        for user in provider.users:
            print(len(items.keys()), user)
            items.setdefault(user.id, user)

            try:
                save(list(items.values()))
            except KeyboardInterrupt:
                break
        save(list(items.values()))


def get_categories(save):
    items = {}
    for cls in providers:
        provider = cls()
        for category in provider.categories:
            print(len(items.keys()), category)
            items.setdefault(category.id, category)

            try:
                save(list(items.values()))
            except KeyboardInterrupt:
                break
        save(list(items.values()))


def get_books(save):
    items = {}
    for cls in providers:
        provider = cls()
        for book_summary in provider.books:
            book_detail = provider.detail_book_of(book_summary)
            print(len(items.keys()), book_detail)
            items.setdefault(book_detail.id, book_detail)

            try:
                save(list(items.values()))
            except KeyboardInterrupt:
                break
        save(list(items.values()))


if __name__ == '__main__':
    # get_users(lambda x: len(x) % 1 == 0 and write_json('users.json', x))
    # get_categories(lambda x: len(x) % 1 == 0 and write_json('categories.json', x))
    get_books(lambda x: len(x) % 1 == 0 and write_json('books.json', x))
