# Given two words (begin_word and end_word), and a dictionary's word list, 
# return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.
# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None


f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())


def get_neighbors(word):
    # a neighbor for a word is any word thats different by one letter
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # and is inside of word_list
    neighbors = set()
    # Take each letter of alphabet
    string_word = list(word)
    # generate every combination of chars where just change one letter at a time
    for i in range(len(string_word)):
        for letter in letters:
            new_word = list(string_word)
            new_word[i] = letter
            new_word_string = "".join(new_word)
            if new_word_string != word and new_word_string in word_set:
                neighbors.add(new_word_string)
    return neighbors
    # check that the word exists in word list
    # if it does
        # its a neighbor
        # return all neighbors


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
        

def find_word_path(begin_word, end_word):
    # do BFS
    # Create a queue
    q = Queue()
    # Create a visited set
    visited = set()
    # add start word to queue
    queue.enqueue([begin_word])
    # while queue not empty
    while queue.size() > 0:
        # pop current word
        current_path = queue.dequeue()
        current_word = current_path[-1]
        # if word has not been visited
        if current_word not in visited:
            if current_word == end_word:
                return current_path
            # is current word the end word, if yes return path
            # add current word to visited
            visited.add(current_word)
            # add neighbors of current word to queue
            for neighbor_word in get_neighbors(current_word):
                new_path = list(current_path)
                new_path.append(neighbor_word)
                queue.enqueue(new_path)