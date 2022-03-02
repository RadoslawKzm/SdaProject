from typing import List
import re


def spliter(word: str, sep: str) -> List[str]:
    start = 0
    output: List[str] = []
    matches = [match.start() for match in re.finditer(sep, word)] + [len(word)]

    for match in matches:
        if w := word[start:match]:
            output.append(w)
        start = match + len(sep)
    return output


print(spliter("dupa&&dupa&&", "&&"))
print(spliter("dupa&&dupa&&", "du"))
print(spliter("dupa&&dupa&&du", "du"))
