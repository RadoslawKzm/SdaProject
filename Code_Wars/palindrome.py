def is_palindrome(word: str) -> bool:
    return word == word[::-1]


if __name__ == "__main__":
    print(is_palindrome("racecar"))
