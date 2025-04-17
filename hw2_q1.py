from collections import namedtuple
import string

MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }

# Create a named tuple to hold the Morse code and the original word
MorseWord = namedtuple("MorseWord", ("morse", "word"))

def is_valid_word(word: str) -> bool:
    return len(word) > 0 and all(char in MORSE_CODE for char in word)

def word_to_morse(word: str) -> MorseWord:
    """
    Translate a single word to Morse code and wrap it in a MorseWord object.
    - Converts each character in the word to Morse.
    - Ignores any character not in the MORSE_CODE dictionary.

    Parameters
    ----------
    word : str
        The word to be converted to Morse code.
        It is assumed that the word contains only uppercase letters and digits.

    Returns
    -------
    MorseWord
        A named tuple containing the Morse code representation of the word and the
        original word.
    """
    # Filter out characters not in the MORSE_CODE dictionary
    cleaned = ''.join(filter(lambda c: c in MORSE_CODE, word))

    # If the cleaned word is valid, convert it to Morse code
    if is_valid_word(cleaned):
        morse = ''.join(map(lambda c: MORSE_CODE[c], cleaned))
        return MorseWord(morse, cleaned)
    # If the cleaned word is not valid, return None
    return None

def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.
    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """
    # Read the input file
    try:
        with open(input_file, "r") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        return

    # Covert text to uppercase
    text = text.upper()

    # Split text into words
    words = text.split()

    # Convert words to Morse code
    morse_words = list(filter(None, map(word_to_morse, words)))

    # Write to output file
    with open(output_file, "w", newline='\n') as file:
        for word in morse_words:
            file.write(f"{word.word} {word.morse}\n")
    
    print(f"Converted text to Morse code and saved to {output_file}.")

if __name__ == "__main__":
    english_to_morse()
