# Owoifier

## Overview

This Python script automatically converts any highlighted text into "owo" speak. The script listens for a specific keyboard trigger (the backslash key, "\\") to activate the conversion. After activation, it modifies the copied text in the clipboard and replaces it with an "owoified" version, then pastes the transformed text back.

## Prerequisites

- **Python 3**: Make sure Python 3 is installed on your system.
- **pynput**: A Python library to control and monitor the keyboard.
- **pyperclip**: A cross-platform Python module for copy and paste clipboard functions.

You can install the required packages using pip:

```bash
pip install pynput pyperclip
```

## Usage

1. **Start the Script**: Run the script in your terminal or command prompt.

```bash
python winowoifier.py
```

2. **Activate Conversion**: Highlight any text you want to convert, then press the backslash key "\\" to trigger the transformation. The script will replace the highlighted text with its "owoified" version instantly.

3. **Stop the Script**: Press the "ESC" key to exit the script.

## Customization

- **Emoticons List**: Modify the `faces` list to add or remove emoticons used after punctuation marks.
- **Text Transformations**: Adjust the `transform_word` function to change how words are transformed.

## Running the Mac Version

Running a script that can monitor keyboard input on Mac is a challange.

1. Navigate to Privacy and Security in System Settings.
 - Under accessability add your terminal app.
 - Under input monitoring add pythonn and your terminal app.

## Future improvments

For the windows version I plan on switching to using the keyboard package, so that we can have text owoified instantly on pressing enter instead of needing to press a keybind.

## License

This script is released under the MIT License. See the LICENSE file for more details.



things to change.

make windows version use keyboard instead of pynput, with option to instantly convert on enter press.

create a readme with tutorial for mac and windows.