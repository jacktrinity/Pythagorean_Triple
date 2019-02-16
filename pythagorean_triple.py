def possible_triple(user_input):
    a = list(range(1, user_input - 2))
    b = list(range(1, user_input - 2))
    c = list(range(1, user_input - 2))

    possible_triple_list = []

    for i in a:
        for j in b:
            for k in c:
                if (i + j + k == user_input) and (k > i) and (k > j) and (i != j):
                    temp_list = [i, j, k]
                    possible_triple_list.append(temp_list)

    return possible_triple_list


def pythagorean_triple(possible_triple_list):
    for i in possible_triple_list:
        if (i[0] ** 2) + (i[1] ** 2) == (i[2] ** 2):
            return i
    return 0


def possible_input():
    try:
        possible_user_input = int(input("Please enter in a number: "))
        return possible_user_input
    except ValueError:
        print("Invalid Input")
        return possible_input()


# Main Body
print("Pythagorean Triple")
user_input = possible_input()

possible_triple_list = possible_triple(user_input)
triple = pythagorean_triple(possible_triple_list)

if triple == 0:
    print("No triple")
else:
    print("{0}, {1}, {2}".format(triple[0], triple[1], triple[2]))

