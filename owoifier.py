import re
import random
from pynput.keyboard import Key, Listener, Controller, KeyCode
import pyperclip
import time

DELAY_TIME = 0.05

faces = [
    "(・`ω´・)", ";;w;;", "owo", "UwU", ">w<", "^w^", "(* ^ ω ^)", "(⌒ω⌒)", "ヽ(*・ω・)ﾉ",
    "(o´∀`o)", "(o･ω･o)", "＼(＾▽＾)／"
]

def random_face():
    return random.choice(faces)

def transform_word(word):
    word = re.sub(r"o", lambda _: 'owo' if random.random() < 0.5 else 'o', word)
    word = re.sub(r"ew", "uwu", word)
    word = re.sub(r"([Hh])ey", r"\1ay", word)
    word = re.sub(r"Dead", "Ded", word)
    word = re.sub(r"dead", "ded", word)
    word = re.sub(r"n[aeiou]*t", "nd", word)
    word = re.sub(r"Read", "Wead", word)
    word = re.sub(r"read", "wead", word)
    word = re.sub(r"[Tt]h", "f", word)
    word = re.sub(r"ve", "we", word)
    word = re.sub(r"Ve", "We", word)
    word = re.sub(r"ry", "wwy", word)
    word = re.sub(r"[rl]", "w", word)
    word = re.sub(r"[RL]", "W", word)
    word = re.sub(r"ll", "ww", word)
    word = re.sub(r"[aeiur]l$", "wl", word)
    word = re.sub(r"([Oo])ld", r"\1wld", word)
    word = re.sub(r"([Oo])l", r"\1wl", word)
    word = re.sub(r"[lr]o", "wo", word)
    word = re.sub(r"[LR]o", "Wo", word)
    return word

def owoify(text):
    # Split text into words and non-words (like spaces and punctuation)
    text = str(text)
    tokens = re.findall(r'\w+|[^\w\s]|[\s]+', text, re.UNICODE)
    
    # Transform each token that is a word, leave non-words as is
    transformed_tokens = [transform_word(token) if token.strip() else token for token in tokens]
    
    # Reassemble the text
    owoified_text = ''.join(transformed_tokens)

    # Apply transformations that aren't word-specific
    owoified_text = re.sub(r"[({<]", "｡･:*:･ﾟ★,｡･:*:･ﾟ☆", owoified_text)
    owoified_text = re.sub(r"[)}>]", "☆ﾟ･:*:･｡,★ﾟ･:*:･｡", owoified_text)
    owoified_text = re.sub(r"[.,;!]", lambda _: ' ' + random_face(), owoified_text)

    return owoified_text

keyboard = Controller()



def on_press(key):
    if key == KeyCode(char='\\'):

        keyboard.press(Key.cmd)
        keyboard.press('a')
        keyboard.release('a')
        time.sleep(DELAY_TIME)  # short delay to ensure the action completes

        
        keyboard.press('x')
        keyboard.release('x')
        time.sleep(DELAY_TIME)
        keyboard.release(Key.cmd)

        # modify clipboard content
        current_clipboard = pyperclip.paste()
        modified_text = owoify(current_clipboard)
        pyperclip.copy(modified_text)
        
        keyboard.press(Key.cmd)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.cmd)
        time.sleep(DELAY_TIME/5)

        #delete the \
        keyboard.tap(Key.backspace)



def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Listening for text to owoify...")
    listener.join()

