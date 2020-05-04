import random
import sys

class Hangman_game:
    def __init__(self, word=""):
        self.word = word
        self.correct_letters = []
        self.wrong_letters = []
        self.guessed_letters = []
        self.level_index = 0
        self.show_letters = []
        self.hided = 0
        # Interface principal
        self.hangman_levels = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

    # Retorna uma palavra de forma randomica
    def word_randomizer(self):
        words_file = open("words.txt", "r").readlines()  # Abre o arquivo para leitura e separa cada linha do arquivo em uma lista
        self.word = random.choice(list(map(lambda x: "".join(x.split()), words_file)))  # Retira os espaços das Strings e retorna um dos indices de forma aleatoria
        return self.word

    # Comeca o jogo
    def starts_game(self):
        self.word_randomizer()
        print(self.hangman_levels[self.level_index])
        return self.ask_letter()

    def ask_letter(self):
        if self.hided == 0:
            self.hide_letters()
            print('Palavra:', ''.join(self.show_letters))
        guessed_letter = input("Digite uma letra: ")
        # Checa se a letra ja foi digitada antes
        while list(map(lambda x: x in self.guessed_letters, guessed_letter)) == [True]:
            guessed_letter = input("Voce ja digitou essa letra, por favor tente outra: ")

        return self.guesses(guessed_letter)

    # Checa se a letra existe ou nao na palavra do jogo
    def guesses(self, letter):
        self.guessed_letters.append(letter)
        if list(map(lambda x: x in self.word, letter)) == [True]:
            self.correct_letters.append(letter)
            return self.display_letters()
        else:
            self.wrong_letters.append(letter)
            return self.update_game_level()

    # Mostra as letras acertadas ate o momento
    def show_correct_guesses(self):
        correct_guesses = ', '.join(self.correct_letters)
        print("Letras acertadas ate o momento: %s" %correct_guesses)

    # Mostra as letras erradas ate o momento
    def show_wrong_guesses(self):
        wrong_guesses = ', '.join(self.wrong_letters)
        print("Letras erradas ate o momento: %s" %wrong_guesses)

    # Esconde as letras que ainda nao foram acertadas
    def hide_letters(self):
        if self.hided == 0:
            self.hided = 1
            for letter in self.word:
                self.show_letters.append("_")
        return self.show_letters

    # Mostra as letras
    def display_letters(self):
        # Preenche as letras acertadas na palavra
        for letter in self.correct_letters:
            for index, l in enumerate(self.word):
                if letter == l:
                    self.show_letters[index] = self.word[index]

        # Chama a proxima fase
        return self.next_level(self.level_index)

    # Altera o nivel do jogo
    def update_game_level(self):
        self.level_index += 1
        return self.next_level(self.level_index)

    # Passa para a proxima fase
    def next_level(self, level):
        if (''.join(self.show_letters)).strip("_") == self.word:
            print("\nVoce acertou!! Parabens!! A palavra era %s!!" %self.word.upper())
            return self.end_game()
        elif level < len(self.hangman_levels):
            print(self.hangman_levels[level])
            # Imprime as letras na tela
            print('Palavra:', ''.join(self.show_letters))
            self.show_correct_guesses()
            self.show_wrong_guesses()
            return self.ask_letter()
        else:
            print("\nVoce perdeu!! A palavra era %s!!" %self.word.upper())
            return self.end_game()

    # Acaba o jogo
    def end_game(self):
        print("\nO jogo acabou!")
        return sys.exit()