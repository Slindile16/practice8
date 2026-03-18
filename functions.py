def separate_scores(scores):
    math_score = []
    science_score = []

    for math, science in scores:
        math_score.append(math)
        science_score.append(science)
    
    return math_score, science_score
# print(separate_scores(([(70, 80), (60, 90)])))


def split_coordinates(coords):
    x_val = []
    y_val = []

    for x, y in coords:
        x_val.append(x)
        y_val.append(y)

    return x_val, y_val
# print(split_coordinates([(1, 2), (3, 4)]))


def build_student_index(students):
    build = {}
    for i,student in enumerate(students):
        build[student] =i
    return build
# print(build_student_index(["Alice", "Bob"])

def map_items_to_position(items):
    return {item:index for index,item in enumerate(items)}
# print(map_items_to_position(["x", "y"]))


def normalize_tags(tags):
    return {i.lower() for i in tags}
# print(normalize_tags(["PYTHON", "python"]))


def clean_usernames(usernames):
    name = set()
    for i in usernames:
        name.add(i.lower())
    return name
# print(clean_usernames(["Admin", "admin"]))


def group_by_city(people):
    pass
    group = {}
    for person in people:
        title = person["name"]
        city = person["city"]
        if city not in group:
            group[city] = []
        group[city].append(title)
    return group
print(group_by_city([
                {"name": "Alice", "city": "Cape Town"},
                {"name": "Bob", "city": "Cape Town"}
            ]))


def categorize_books(books):
    grouped = {}
    for book in books:
        title = book["title"]
        genre = book["genre"]
        if genre not in grouped:
            grouped[genre] = []
        grouped[genre].append(title)
    return grouped
print(categorize_books([
                {"title": "Book1", "genre": "Fiction"},
                {"title": "Book2", "genre": "Fiction"}
            ]))
