import string
import sys
import queue


def valid_variations(word, dictionary):

    variations = []
    for i in range(len(word)):
        for letter in string.ascii_lowercase:
            variation = word[:i] + letter + word[i+1:]
            if variation in dictionary:
                variations.append(variation)
    return variations


def solve_bfs(source, target, dictionary):
    """pass."""

    print(source, target)

    search_queue = queue.Queue()
    search_queue.put([source])
    visited = set()
    found = []

    while(not search_queue.empty()):

        chain = search_queue.get()
        current = chain[-1]

        if current == target:
            found = chain
            break

        variations = valid_variations(current, dictionary)
        for variation in variations:
            if variation not in visited:
                search_queue.put(chain + [variation])
            visited.add(variation)

    return found

# def legal(word):
#     for letter in word:
#         if letter not in string.ascii_lowercase:
#             return False
#     return True

def load_words(filename):
    f = open(filename, 'r')
    words = [line.lower().strip("\n\t's") for line in f]
    f.close()
    return words

# def save_words(filename, words):
#     f = open(filename, "a")
#     for word in words:
#         f.write(word + "\n")
#     f.close()


# filename = "dictionaries/british-english"
filename = "words.txt"
words = load_words(filename)
print(solve_bfs("python", "happy", words))

# clean_words = []
# for word in words:
#     if legal(word):
#         clean_words.append(word)
# clean_words = list(set(clean_words))
# save_words("dictionaries/cleaned", clean_words)

# len_dicts = {}
# for word in words:
#     l = len(word)
#     len_dict = len_dicts.get(str(l), [])
#     len_dict.append(word)
#     len_dicts[str(l)] = len_dict

# tried_combinations = {}

# for d in range(4, 4):
#     d = str(d)
#     chains = []
#     for i in range(len(len_dicts[d])):
#         word1 = len_dicts[d][i]
#         for j in range(len(len_dicts[d])):
#             word2 = len_dicts[d][j]

#             if word1 == word2:
#                 break
#             if word2 in tried_combinations.get(word1, []):
#                 break
#             if word1 in tried_combinations.get(word2, []):
#                 break

#             tried_combinations[word1] = tried_combinations.get(word[1], [word2])
#             tried_combinations[word2] = tried_combinations.get(word[1], [word1])

#             print(f"Trying {word1} -> {word2}")
#             solution = solve_bfs(word1, word2, words)

#             if solution:
#                 chains.append(solution)
#                 print(word1, word2, solution)

# # print(solve_bfs("cat", "dog", words))
