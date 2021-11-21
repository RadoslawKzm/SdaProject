class Trie:
    def insert(self, word: str) -> None:
        pass

    def has_item(self, word: str) -> bool:
        pass


if __name__ == '__main__':
    trie = Trie()
    trie.insert("ass")
    trie.insert("assumption")
    trie.insert("assertion")
    trie.insert("asap")
    assert trie.has_item("ass") == True
    assert trie.has_item("assumption") == True
