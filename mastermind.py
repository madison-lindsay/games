import numpy as np

def generate_solution(size):
    sol = np.random.choice(range(size+2), size=size)
    return sol

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
        guess = input("Guess {0} digits between zero and {1}: ".format(size, size+1))
        guess = [int(x) for x in guess if x != " "]
        response, victory = evaluate_guess(guess, sol, size)
        tries += 1
        for symb in response:
            print(symb, end=" ")
        print("")
    print("VICTORY in {} tries".format(tries))

main()
