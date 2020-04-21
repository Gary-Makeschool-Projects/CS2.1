#!python3

from prefixtreenode import PrefixTreeNode
from typing import List, Tuple


class PrefixTree(object):
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None) -> object:
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self) -> bool:
        """Return True if this prefix tree is empty (contains no strings).
        Time Complexity:
        Space Complexity:
        """
        return self.size == 0

    def contains(self, string) -> bool:
        """Return True if this prefix tree contains the given string.
        Time Complexity:
        Space Complexity:
        """
        # one liner via alex :)
        return string in self.strings()

    def insert(self, string) -> None:
        """Insert the given string into this prefix tree.
        Time Complexity:
        Space Complexity:
        """
        # current
        current = self.root

        for character in string:

            # if the child exists
            if current.has_child(character):
                # traverse to next node
                current = current.get_child(character)
            else:
                # create new node
                new_node = PrefixTreeNode(character)
                current.add_child(character, new_node)
                # traverse to next node
                current = current.get_child(character)

        if not current.is_terminal():
            self.size += 1
            current.terminal = True

    def _find_node(self, string) -> Tuple[PrefixTreeNode, int]:
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:
            return self.root, 0

        # Start with the root node
        node = self.root
        index = 0

        # loop through letters of string
        while index < len(string) and node.has_child(string[index]):
            # traverse
            node = node.get_child(string[index])
            index += 1

        # return node and index
        return node, index

    def complete(self, prefix) -> list:
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""

        completions = []

        # return all items if empty string
        if prefix == '':
            return self.strings()

        # traverse to base
        node = self._find_node(prefix)

        # if not empty lawl
        if node[0].character is not '':
            self._traverse(node[0], prefix, completions.append)

        return completions

    def strings(self) -> list:
        """Return a list of all strings stored in this prefix tree.
        Time Complexity: O(logn) The tree is already balanced
        Space Complexity: O(n) we return a new array of size n"""
        # list of all the string in out prefix tree
        strings = []

        # add all the strings using our traverses
        self._traverse(self.root, '', strings.append)
        # return all combos
        return strings

    def _traverse(self, node, prefix, visit) -> None:
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function.
        Time Complexity: 
        Space Complexity:
        """
        # check if the current node is terminal
        if node.is_terminal():
            # add
            visit(prefix)

        # continue to check
        for char in node.children.keys():
            # traverse to the next node and build string recursivly
            child = node.get_child(char)
            string = self._traverse(child, prefix + char, visit)

    def _iterative_traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function.
        Time Complexity: 
        Space Complexity:
        """
        # iterativley traverse through tree
        # todo Alan will owe me $50
        pass


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def main():
    # Simpe test case of string with partial substring overlaps
    strings = ['ABC', 'ABD', 'A', 'XYZ']
    create_prefix_tree(strings)

    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        'Woodchuck': ('How much wood would a wood chuck chuck'
                      ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
        if len(tongue_twisters) > 1:
            print('\n' + '='*80 + '\n')


if __name__ == '__main__':
    main()
