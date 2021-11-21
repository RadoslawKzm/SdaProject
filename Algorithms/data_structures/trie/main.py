class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        active = self.trie
        for letter in word:
            active = active.setdefault(letter, {})
        active["*"] = "_end"

    def full_search(self, word: str) -> bool:
        return self._serch(word).get("*") == "_end" or False

    def partial_search(self, word: str) -> bool:
        return bool(self._serch(word))

    def _serch(self, word: str) -> dict:
        active = self.trie
        for letter in word:
            if not (active := active.get(letter)):
                return {}
        return active


if __name__ == '__main__':
    trie = Trie()
    trie.insert("ass")
    trie.insert("assumption")
    trie.insert("assertion")
    trie.insert("asap")
    # assert trie.search("ass") == True
    # assert trie.search("assumption") == True
