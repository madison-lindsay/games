# games
* Mastermind
  * Premise: a random set of (size = 4, unless otherwise specified) integers between 0 and 5 (5 = size + 1) is generated - this is the unknown solution. Your job is to guess those numbers in as few tries as possible. After each guess, you receive feedback: the number of instances where you have the right number in the right place, the number of instances where you have the right number in the wrong place, and the number of wrong numbers. For example, if the solution is "2 4 5 1" and you guess "2 1 4 0", your response will be "😍 😏 😏 ❌" since the 2 is in the right place, 1 and 4 are in the wrong places, and 5 was not guessed at all.
  * Make guesses, separating integers with spaces, like this: 0 0 1 1
  * 😍 = right number, right place; 😏 = right number, wrong place; ❌ = wrong number
