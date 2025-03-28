from collections import Counter
import os
import re

def get_common_words(text: str, n: int = 1) -> list[tuple[str, int]]:
    words = re.findall(r'[a-zA-Z0-9]+', text.lower())
    word_counts = Counter(w for w in words if len(w) > 2)
    return word_counts.most_common(n)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    text_file_path = os.path.join(current_dir, "sample_text.txt")
    
    with open(text_file_path, 'r') as file:
        text = file.read()
    
    print(get_common_words(text, 3))
