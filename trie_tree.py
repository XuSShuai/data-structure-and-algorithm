#  前缀树


class TrieNode:
    def __init__(self):
        self.path = 0  # number of prefix
        self.end = 0   # number of word
        self.next = [None] * 26


class TrieTree:
    def __init__(self):
        self.__root = TrieNode()

    def insert(self, word):
        word = list(word)
        node = self.__root
        for w in word:
            index = ord(w) - ord("a")
            if node.next[index] is None:
                node.next[index] = TrieNode()
            node = node.next[index]
            node.path += 1
        node.end += 1

    def word_count(self, word) -> int:
        if len(word.strip()) == 0:
            return 0
        word = list(word)
        node = self.__root
        for w in word:
            index = ord(w) - ord("a")
            if node.next[index] is None:
                return 0
            node = node.next[index]
        return node.end

    def delete(self, word):
        if self.word_count(word) == 0:
            return
        word = list(word)
        node = self.__root
        for w in word:
            index = ord(w) - ord("a")
            if node.next[index].path == 1:
                node.next[index] = None
                return
            node = node.next[index]
            node.path -= 1
        node.end -= 1

    def number_prefix_with(self, prefix) -> int:
        if len(prefix.strip()) == 0:
            return 0
        prefix = list(prefix)
        node = self.__root
        for w in prefix:
            index = ord(w) - ord("a")
            if node.next[index] is None:
                return 0
            node = node.next[index]
        return node.path

    def prefix_with(self, word):
        if len(word.strip()) == 0:
            return
        word_list = list(word)
        node = self.__root
        for w in word_list:
            index = ord(w) - ord("a")
            if node.next[index] is None:
                return
            node = node.next[index]
        self.__print_prefix_with(node, word)

    def __print_prefix_with(self, node, word):
        flag = 0
        for i in range(26):
            if not node.next[i] is None:
                self.__print_prefix_with(node.next[i],  word+chr(ord("a") + i))
            else:
                flag += 1
        if flag == 26:
            print(word)
            return

if __name__ == "__main__":
    trie_tree = TrieTree()

    trie_tree.insert("a")
    trie_tree.insert("ability")
    trie_tree.insert("abandon")
    trie_tree.insert("able")
    trie_tree.insert("able")
    trie_tree.insert("about")
    trie_tree.insert("above")
    trie_tree.insert("accept")
    trie_tree.insert("access")

    print("number of word 'able':", trie_tree.word_count("able"))
    print("number of word 'ability':", trie_tree.word_count("ability"))
    print("number of word 'abc':", trie_tree.word_count("abc"))
    print("-"*10)

    print("number of prefix with 'acce': ", trie_tree.number_prefix_with("acce"))
    print(trie_tree.prefix_with("acce"))
    print("-"*10)

    print("number of prefix with 'ab': ", trie_tree.number_prefix_with("ab"))
    print(trie_tree.prefix_with("ab"))
    print("-" * 10)

    trie_tree.delete("able")
    print("number of word 'able':", trie_tree.word_count("able"))

    print("-" * 10)
    print("number of prefix with 'ab': ", trie_tree.number_prefix_with("ab"))
    print(trie_tree.prefix_with("ab"))
    print("-" * 10)

    trie_tree.delete("able")
    print("number of word 'able':", trie_tree.word_count("able"))

    print("-" * 10)
    print("number of prefix with 'ab': ", trie_tree.number_prefix_with("ab"))
    print(trie_tree.prefix_with("ab"))
    print("-" * 10)
