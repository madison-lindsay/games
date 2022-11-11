import numpy as np
import sys


def generate_solution(size):
    sol = np.random.choice(range(size+2), size=size)
    return sol


def validate_guess(guess, size):
    return_true = True
    user_input = [x for x in guess.split(" ") if x != ""]
    if len(user_input) > size:
        print(f'You have entered {len(user_input)} values! Only {size} are permitted. Try again.')
        return_true = False

    return_guess = []
    for x in user_input:
        try:
            to_append = int(x)
            if (to_append > size + 1) or (to_append < 0):
                print(f'Input {x} is not in the specified range! Try again.')
                return_true = False
            else:
                return_guess.append(to_append)
        except:
            print(f'Input {x} is not an integer! Try again.')
            return_true = False
        if not return_true:
            return False

    return return_guess


def evaluate_guess(guess, sol, size):
    response = []
    to_remove = []
    x = 0
    # correct
    while x < len(guess):
        if guess[x] == sol[x]:
            response.append("😍")
            to_remove.append(x)
        x += 1
    # wrong spot
    guess = [guess[x] for x in range(len(guess)) if x not in to_remove]
    sol = [sol[x] for x in range(len(sol)) if x not in to_remove]
    for x in range(len(guess)):
        for y in range(len(sol)):
            if guess[x] == sol[y]:
                sol = [sol[z] if z != y else -1 for z in range(len(sol))]
                response.append("😏")
                break
    # wrong number
    for x in range(size-len(response)):
        response.append("❌")
    return response, len(guess) == 0


def main(size=4):
    sol = list(generate_solution(size))
    tries = 0
    victory = False
    while not victory:
        guess = input("Guess {0} integers from zero to {1}: ".format(size, size+1))
        guess = validate_guess(guess, size)
        if not guess:
            continue
        response, victory = evaluate_guess(guess, sol, size)
        tries += 1
        for symb in response:
            print(symb, end=" ")
        print("")
    print("VICTORY in {} tries".format(tries))


if len(sys.argv) > 1:
    size = int(sys.argv[1])
    main(size=size)
else:
    main()
