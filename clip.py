import os
import time

# Updated text with 80 comments
text = """
1. Good morning! Wishing you a day full of positivity and success.
2. Rise and shine! Have a beautiful morning!
3. Morning vibes are the best vibes. Have a great day!
4. Waking up is the first blessing of the day. Good morning!
5. Good morning! Let’s make today amazing.
6. Sending you sunshine and good vibes this morning!
7. Have a cheerful morning and an even better day!
8. Good morning! Don’t forget to smile today.
9. A fresh start to a fresh day. Good morning!
10. Good morning! It’s a beautiful day to be alive.
# Add the rest of your text...
"""

# Split text into lines
points = text.strip().split("\n")

# Copy each line to clipboard sequentially
for point in points:
    if point.strip():  # Skip empty lines
        # Use Termux clipboard API
        os.system(f"termux-clipboard-set '{point.strip()}'")
        print(f"Copied to clipboard: {point.strip()}")
        time.sleep(1)  # Delay for clipboard processing
