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
        for person in people:
            file.write(f"{person['Name']}÷×"


def parse(command):
    command = command.split()
    if command[0] == "new":
        return add_user(command[1:])


def add_user(command):
    global people
    people += {"Name": " ".join(command), "Age": "None", "City": "None", "Data": []}
    return "Added"


if __name__ == "__main__":
    people = init()
    print(people)
    while True:
        command = input("> ")
        result = parse(command)
        if result == -1:
            break
        print(result)

