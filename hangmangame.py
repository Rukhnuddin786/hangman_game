import random

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                
'''
print(logo)
stages = [
  '''  +---+
  |   |
  O   |
 /|\  |
 / \  |
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
  |   |
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
      |
      |
      |
      |
========='''
]

word_list = [
  'abruptly',
  'absurd',
  'abyss',
  'affix',
  'askew',
  'avenue',
  'awkward',
  'axiom',
  'azure',
  'bagpipes',
  'bandwagon',
  'banjo',
  'bayou',
  'beekeeper',
  'bikini',
  'blitz',
  'blizzard',
  'boggle',
  'bookworm',
  'boxcar',
  'boxful',
  'buckaroo',
  'buffalo',
  'buffoon',
  'buxom',
  'buzzard',
  'buzzing',
  'buzzwords',
  'caliph',
  'cobweb',
  'cockiness',
  'croquet',
  'crypt',
  'curacao',
  'cycle',
  'daiquiri',
  'dirndl',
  'disavow',
  'dizzying',
  'duplex',
  'dwarves',
  'embezzle',
  'equip',
  'espionage',
  'euouae',
  'exodus',
  'faking',
  'fishhook',
  'fixable',
  'fjord',
  'flapjack',
  'flopping',
  'fluffiness',
  'flyby',
  'foxglove',
  'frazzled',
  'frizzled',
  'fuchsia',
  'funny',
  'gabby',
  'galaxy',
  'galvanize',
  'gazebo',
  'giaour',
  'gizmo',
  'glowworm',
  'glyph',
  'gnarly',
  'gnostic',
  'gossip',
  'grogginess',
  'haiku',
  'haphazard',
  'hyphen',
  'iatrogenic',
  'icebox',
  'injury',
  'ivory',
  'ivy',
  'jackpot',
  'jaundice',
  'jawbreaker',
  'jaywalk',
  'jazziest',
  'jazzy',
  'jelly',
  'jigsaw',
  'jinx',
  'jiujitsu',
  'jockey',
  'jogging',
  'joking',
  'jovial',
  'joyful',
  'juicy',
  'jukebox',
  'jumbo',
  'kayak',
  'kazoo',
  'keyhole',
  'khaki',
  'kilobyte',
  'kiosk',
  'kitsch',
  'kiwifruit',
  'klutz',
  'knapsack',
  'larynx',
  'lengths',
  'lucky',
  'luxury',
  'lymph',
  'marquis',
  'matrix',
  'megahertz',
  'microwave',
  'mnemonic',
  'mystify',
  'naphtha',
  'nightclub',
  'nowadays',
  'numbskull',
  'nymph',
  'onyx',
  'ovary',
  'oxidize',
  'oxygen',
  'pajama',
  'peekaboo',
  'phlegm',
  'pixel',
  'pizazz',
  'pneumonia',
  'polka',
  'pshaw',
  'psyche',
  'puppy',
  'puzzling',
  'quartz',
  'queue',
  'quips',
  'quixotic',
  'quiz',
  'quizzes',
  'quorum',
  'razzmatazz',
  'rhubarb',
  'rhythm',
  'rickshaw',
  'schnapps',
  'scratch',
  'shiv',
  'snazzy',
  'sphinx',
  'spritz',
  'squawk',
  'staff',
  'strength',
  'strengths',
  'stretch',
  'stronghold',
  'stymied',
  'subway',
  'swivel',
  'syndrome',
  'thriftless',
  'thumbscrew',
  'topaz',
  'transcript',
  'transgress',
  'transplant',
  'triphthong',
  'twelfth',
  'twelfths',
  'unknown',
  'unworthy',
  'unzip',
  'uptown',
  'vaporize',
  'vixen',
  'vodka',
  'voodoo',
  'vortex',
  'voyeurism',
  'walkway',
  'waltz',
  'wave',
  'wavy',
  'waxy',
  'wellspring',
  'wheezy',
  'whiskey',
  'whizzing',
  'whomever',
  'wimpy',
  'witchcraft',
  'wizard',
  'woozy',
  'wristwatch',
  'wyvern',
  'xylophone',
  'yachtsman',
  'yippee',
  'yoked',
  'youthful',
  'yummy',
  'zephyr',
  'zigzag',
  'zigzagging',
  'zilch',
  'zipper',
  'zodiac',
  'zombie',
]
choosen_word = random.choice(word_list)

print(f"the random word is:{choosen_word}\n")
display = []
for letter in range(len(choosen_word)):
  display += "_"

print(display)
print("\n")
lives = 6

end_game = False
while not end_game:

  guess = input("guess a letter ? ").lower()
  if guess in display:
    print(f"you have already guessed {guess}")
  for word in range(len(choosen_word)):
    letter = choosen_word[word]
    if guess == letter:
      display[word] = letter

  if guess not in choosen_word:
    lives -= 1
    if lives == 0:
      end_game = True
      print("you loose")
  print(f"{' '.join(display)}")
  if "_" not in display:
    end_game = True
    print("Congrats you have won")

  print(stages[lives])
  print("\n")
