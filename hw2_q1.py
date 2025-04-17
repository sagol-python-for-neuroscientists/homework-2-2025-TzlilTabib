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
    # Read the input file if found, convert to uppercase, and split into words
    try: 
        text = open(input_file).read().upper().split()
    except FileNotFoundError:
        return print(f"File {input_file} not found.")
    
    # Convert each word to Morse code
    morse_words = map(
        lambda w: ''.join(map(MORSE_CODE.get, w)),
        # Filter out None values from the map to avoid joining None characters
        filter(None, map(lambda w: ''.join(filter(MORSE_CODE.get, w)), text)))  
    
    # Join the Morse code words with spaces and write to the output file
    open(output_file, "w").write('\n'.join(morse_words))
    print(f"Converted text to Morse code and saved to {output_file}.")

english_to_morse()