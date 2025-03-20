import sys

from typing import Dict, List

from stats import count_words, count_chars, sort_char_map


def get_book_text(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()

def print_report(path: str, word_count: int, char__map: List[Dict[str, any]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for single_map in char__map:
        char = single_map['char']
        count = single_map['count']
        print(f"{char}: {count}")
    print("============= END ===============")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    contents : str = get_book_text(path)
    num_words = count_words(contents)
    sorted_chars = sort_char_map(count_chars(contents))
    print_report(path, num_words, sorted_chars)

if __name__ == '__main__':
    main()
