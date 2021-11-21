class Trie:
    def insert(self, word: str) -> None:
        pass

    def has_item(self, word: str) -> bool:
        pass


if __name__ == '__main__':
    trie = Trie()
    trie.insert("duch")
    trie.insert("dupa")
    trie.insert("duda")
    trie.insert("duchowny")
    assert trie.has_item("duch") == True
    assert trie.has_item("duchowny") == True
