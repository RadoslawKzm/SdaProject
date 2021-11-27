from typing import Optional, Hashable, Any, Generator


class NewDictionary:
    def __init__(self, size: Optional[int] = 10) -> None:
        """
        use list as storage, each element is also a list which is used
        to solve hash conflict
        """
        self.storage: list[list[Any]] = [[] for _ in range(size)]
        self.size: int = size
        self._length: int = 0

    def __len__(self) -> int:
        return self._length

    def __setitem__(self, key: Hashable, value: Any):
        """
        set key value, if conflict, append to the sub list
        """
        storage_index: int = hash(key) % self.size
        for element in self.storage[storage_index]:
            if key == element[0]:  # already exist, update it
                element[1] = value
                return None
        self.storage[storage_index].append([key, value])
        self._length += 1

    def _key_error(self):
        raise KeyError

    def _get(self, key: Hashable) -> Any:
        """
        get by key, if not found, raise key error
        :raise: KeyError
        :return: value
        """
        storage_index: int = hash(key) % self.size
        for storage_key, storage_value in self.storage[storage_index]:
            if storage_key == key:
                return storage_value

    def __getitem__(self, key: Hashable) -> Any:
        return self._get(key) or self._key_error()

    def __contains__(self, key) -> bool:
        storage_index: int = hash(key) % self.size
        return any([storage_key == key for storage_key, _ in self.storage[storage_index]])

    def __str__(self) -> str:
        dictio = {k: v for lst in self.storage for k, v in lst}
        return f"{dictio}"

    def __repr__(self) -> str:
        return self.__str__()

    def get(self, key: Hashable, default: Optional[Any] = None):
        """
        get value by key, optional default value
        :param key: str
        :param default: Any
        :return: value
        """
        return self._get(key) or default

    def __iter__(self) -> Generator:
        return (key for slot in self.storage for key, _ in slot)

    def keys(self):
        return {key for slot in self.storage for key, _ in slot}

    def values(self):
        return {value for slot in self.storage for _, value in slot if slot}

    def items(self):
        return {k:v for k,v in zip(self.keys(), self.values())}


if __name__ == '__main__':
    dictio = NewDictionary()
    dictio[1] = "dupa1"
    dictio[11] = "dupa11"
    dictio[111] = "dupa111"
    dictio[112] = "dupa112"
    assert dictio[1] == "dupa1"
    assert 111 in dictio
    print(dictio)
