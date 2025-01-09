

import pyperclip
import time

# Sample text with 20 points (each point on a new line)
text = """
Point 1: Example
Point 2: Example
Point 3: Example
...
Point 20: Example
"""

# Split into lines
points = text.strip().split("\n")

# Copy each point to clipboard one by one
for point in points:
    pyperclip.copy(point)
    print(f"Copied to clipboard: {point}")
    time.sleep(1)  # Delay to handle clipboard changes

