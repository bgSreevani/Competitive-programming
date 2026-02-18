#Auto-Complete Feature in a Search Engine Using Trie

# Trie Node Class
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


# Trie Class
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into Trie
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    # Search complete word
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    # Prefix Query (startsWith)
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# ----------------------------
# Example Test Case 1
# ----------------------------

keywords = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]

trie = Trie()

# Insert keywords
for word in keywords:
    trie.insert(word)

# Operations
print('Keyword "mouse" found →', trie.search("mouse"))
print('Keyword "monkey" not found →', trie.search("monkey"))
print('Prefix "mon" exists →', trie.startsWith("mon"))
print('Prefix "mou" exists →', trie.startsWith("mou"))


#✅ Output
Keyword "mouse" found → True
Keyword "monkey" not found → False
Prefix "mon" exists → True
Prefix "mou" exists → True




#City Name Search Using Trie
# Trie Node Class
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


# Trie Class
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert city name
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    # Search complete city
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    # Prefix Query
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# ----------------------------
# Example Test Case
# ----------------------------

cities = ["Delhi", "Dehradun", "Dharwad", "Mumbai", "Mysore"]

trie = Trie()

# Insert city names
for city in cities:
    trie.insert(city)

# Operations
print('City "Delhi" found →', trie.search("Delhi"))
print('City "Dublin" not found →', trie.search("Dublin"))
print('Prefix "Dh" exists →', trie.startsWith("Dh"))
print('Prefix "My" exists →', trie.startsWith("My"))


#✅ Output
City "Delhi" found → True
City "Dublin" not found → False
Prefix "Dh" exists → True
Prefix "My" exists → True
