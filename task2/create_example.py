import json
from csv import DictReader


def create_file_with_empty_books(path):
    user_data = []
    with open(path) as users:
        users = json.load(users)
        for user in users:
            personal_data = {"name": user["name"],
                             "gender": user["gender"],
                             "address": user["address"],
                             "books": []}
            user_data.append(personal_data)
    return user_data, len(user_data)


def get_books(path):
    books_data = []
    with open(path) as books:
        reader = DictReader(books)
        for row in reader:
            book_info = {"title": row["Title"],
                         "author": row["Author"],
                         "height": row["Height"]}
            books_data.append(book_info)
    return books_data


def add_books_to_user(users, books):
    number_of_users = users[1] - 1
    count_for_users = 0
    count_for_books = 0
    while count_for_users <= number_of_users:
        user = users[0][count_for_users]
        user['books'].append(books[count_for_books])
        count_for_users += 1
        count_for_books += 1
    return json.dumps(users[0], indent=4)


def write_data_to_json(path, data):
    with open(path, "w") as example:
        example.write(data)


path_for_users = "../data/users"
path_for_books = "../data/books.csv"
path_for_example = "../data/example.json"
users_without_books = create_file_with_empty_books(path_for_users)
only_books = get_books(path_for_books)
data_for_writing = add_books_to_user(users_without_books, only_books)
write_data_to_json(path_for_example, data_for_writing)
