import os


def init():
    if "data.ini" not in os.listdir("."):
        open("data.ini", "w")
    with open("data.ini", "r") as file:
        people = []
        for line in file.read().split("\n"):
            line = line.strip().split("÷×")
            if line == [""]:
                continue
            people += [{"Name": line[0], "Age": line[1], "City": line[2], "Data": line[3:]}]
        return people


def exit():
    with open("data.ini", "w") as file:
        data = ""
        for person in people:
            data += f"{person['Name']}÷×{person['Age']}÷×{person['City']}÷×" + "÷×".join(person["Data"]) + "\n"
        file.write(data)


def parse(command):
    command = command.strip().split()
    if command[0] == "new":
        return add_user(command[1:])
    elif command[0] == "exit":
        exit()
        return -1
    elif " ".join(command) == "print all":
        for person in people:
            print("-------------------------------------------------")
            print(f"Name: {person['Name']}")
            print(f"Age: {person['Age']}")
            print(f"City: {person['City']}")
            for num, fact in enumerate(person["Data"]):
                if len(fact) == 0:
                    continue
                print(num + 1, end=". ")
                i = 0
                while True:
                    print(fact[i], end="")
                    i += 1
                    if i == 49:
                        print()
                    if i == len(fact):
                        print()
                        break
            print("-------------------------------------------------")
        print(f"Total: {len(people)}")
    elif command[0] == "add":
        if len(command) < 2:
            return "Мало аргументов"
        person = people.index(list(filter(lambda x: x["Name"] == command[1], people))[0])
        return add_fact(person)
    elif command[0] == "set":
        if len(command) < 4:
            return "Мало аргументов"
        person = people.index(list(filter(lambda x: x["Name"] == command[2], people))[0])
        if command[1] == "age":
            people[person]["Age"] = command[3]
        elif command[1] == "name":
            people[person]["Name"] = command[3]
        elif command[1] == "city":
            people[person]["City"] = command[3]
        else:
            return "Пункт не найден"
        return "Edited"
    elif command[0] == "del":
        if len(command) < 3:
            return "Мало аргументов"
        if command[1] == "user":
            del people[people.index(list(filter(lambda x: x["Name"] == command[2], people))[0])]
        if command[1] == "fact":
            if len(command) < 4:
                return "Мало аргументов"
            person = people.index(list(filter(lambda x: x["Name"] == command[2], people))[0])
            try:
                fact = int(command[3])
            except ValueError:
                return "Неверно указано число"
            if fact >= len(people[person]["Data"]):
                return "Нет такого факта"
            del people[person]["Data"][fact - 1]
            return "Deleted"
    elif command[0] == "search":
        age, name, city = False, False, False
        if "age" in command:
            age = command.index("age")
        if "name" in command:
            name = command.index("name")
        if "city" in command:
            city = command.index("city")
        got = people.copy()
        if age:
            got = list(filter(lambda x: x["Age"] == command[age + 1], got))
        if name:
            got = list(filter(lambda x: x["Name"] == command[name + 1], got))
        if city:
            got = list(filter(lambda x: x["City"] == command[city + 1], got))
        for person in got:
            print("-------------------------------------------------")
            print(f"Name: {person['Name']}")
            print(f"Age: {person['Age']}")
            print(f"City: {person['City']}")
            for num, fact in enumerate(person["Data"]):
                if len(fact) == 0:
                    continue
                print(num + 1, end=". ")
                i = 0
                while True:
                    print(fact[i], end="")
                    i += 1
                    if i == 49:
                        print()
                    if i == len(fact):
                        print()
                        break
            print("-------------------------------------------------")
        print(f"Total: {len(got)}")
    else:
        return "Команда не найдена"


def add_fact(person):
    data = input("Enter: > ")
    global people
    people[person]["Data"] += [data]
    return "Added"


def add_user(command):
    global people
    people += [{"Name": " ".join(command), "Age": "None", "City": "None", "Data": []}]
    return "Added"


if __name__ == "__main__":
    people = init()
    while True:
        command = input("> ")
        result = parse(command)
        if result == -1:
            break
        if result is not None:
            print(result)

