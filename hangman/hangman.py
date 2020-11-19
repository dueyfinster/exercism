# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guesses = []
        self.masked_word = ""
        for i in range(len(word)):
            self.masked_word += "_"

    def guess(self, char):
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
            raise ValueError("Too many guesses!")

        if self.status == STATUS_WIN:
            raise ValueError("You've already won!")

        if char in self.guesses:
            self.remaining_guesses = self.remaining_guesses - 1
            if self.remaining_guesses == 0:
                self.status = STATUS_LOSE
            return
        else:
            self.guesses.append(char)

        try:
            self.word.index(char)
        except ValueError:
            self.remaining_guesses = self.remaining_guesses - 1
            if self.remaining_guesses == 0:
                self.status = STATUS_LOSE
            return

        for i, cur_char in enumerate(self.word):
            if char == cur_char:
                self.masked_word = (
                    self.masked_word[:i] + char + self.masked_word[i + 1 :]
                )

        try:
            self.masked_word.index("_")
        except ValueError:
            self.status = STATUS_WIN
            return

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status
