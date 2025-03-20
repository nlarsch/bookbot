from typing import Dict, List


def count_words(contents: str) -> int:
    return len(contents.split())

def count_chars(contents: str) -> Dict[str, int]:
    result : Dict[str, int] = {}
    for c in contents.lower():
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result

def sort_char_map(char_map: Dict[str, int]) -> List[Dict[str, any]]:
    result : List[Dict[str, any]] = []
    for k, v in char_map.items():
        if str.isalpha(k):
            single_result : Dict[str, any] = {"char": k, "count": v}
            result.append(single_result)
    result.sort(reverse=True, key=lambda x: x["count"])
    return result
