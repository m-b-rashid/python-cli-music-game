import re


class AuthenticationError(Exception):
    pass


def main():
    file_name = "users.txt"
    try:
        registered_users = get_users(file_name)
    except FileNotFoundError as not_found:
        print("File " + not_found.filename + " not found" + "\nCreating File")
        registered_users = {}
        f = open(file_name, "x")
        f.close()
        print("\nFile created\n")

    print(registered_users)
    status = ""
    while status != "q":
        status = input("Are you registered user? y/n? Press q to quit \n")
        if status == "y":
            username = login(registered_users)
            start_quiz(username)
        elif status == "n":
            register(registered_users, "users.txt")
        elif status == "q":
            exit()
        else:
            print("Wrong Input")


def register(users, file_name):
    username = input("Input a Username: ")
    if username in users:
        print("\nUsername already exist! Please try again!\n")
    else:
        password = input("Input a password: ")
        users[username] = password
        f = open(file_name, "a+")
        f.write("\nusername: " + username + " password: " + password)
        f.close()
        print("\nUser created\n")
        return users


def login(users, max_tries=3):
    for i in range(max_tries):
        username = input("Please enter your username ")
        password = input("Please enter your password ")
        if username in users and users[username] == password:
            print("You are logged in as", username)
            return username
        else:
            print(f"Login failed. You have {max_tries - i - 1} tries left.")
    raise AuthenticationError(f"You have been locked out please restart to try again.")


def get_users(file_name):
    line_fmt = re.compile(r'username: (.*) password: (.*)')
    users = {}
    with open(file_name) as f:
        for line in f:
            try:
                name, password = line_fmt.match(line.strip()).groups()
                users[name] = password
            except AttributeError:
                print("Malformed line:", line)
        return users


def get_data(file_name):
    data = {}
    with open(file_name) as f:
        for line in f:
            try:
                song, artist = line.split(',')
                data[song] = artist
            except AttributeError:
                print("Malformed line:", line)
        return data


def start_quiz(username):
    print("####Starting new game####")
    print("\n####Loading Data####")
    data = {}
    try:
        data = get_data("data.txt")
    except FileNotFoundError as not_found:
        print("File " + not_found.filename + " not found")
        exit()

    if not data:
        print("Data List is empty")
        exit()
    else:
        print("\n####Data Loaded####")
        index = 1
        score = 0
        for song in data:
            print("Question NO. " + str(index))
            print("Artist: " + data[song])
            line = song
            words = line.split()
            letters = [word[0] for word in words]
            print("The first letter of each word in the song: ")
            print("".join(letters))
            guess = input("Try to guess the name of the song: ")
            count = 2
            while count > 0:
                if guess == song:
                    print("Well done! Adding some points")
                    #need to fix with if statement
                    score += count
                    break
                else:
                    print("Wrong :( Try again!")
                    count -= 1
            if count == 0:
                print("All chances gone. Calculating score..")
                print(username + " has scored " + score)
                add_score(score)
                top_five()
                score = 0
                print("Thanks for playing")
            index += 1


def add_score(score):
    print("empty")


def top_five():
    #sort here
    print("empty")


if __name__ == "__main__":
    main()
