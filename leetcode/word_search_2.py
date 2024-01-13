from typing import Dict, List, Tuple


class WordDictionary(object):
    def __init__(self):
        self.mapping = {}

    def insert(self, word: str) -> None:
        chars = [char for char in word]
        mapping = self.mapping

        for char in chars:
            if char not in mapping:
                mapping[char] = {}

            mapping = mapping[char]

        mapping['word'] = word

    def search_word(self, word: str) -> bool:
        chars = [char for char in word]
        mapping = self.mapping

        for char in chars:
            if char not in mapping:
                return False

            mapping = mapping[char]

        if mapping.get('word', None) == word:
            return True
        else:
            return False

    def starts_with(self, prefix: str) -> bool:
        chars = [char for char in prefix]
        mapping = self.mapping

        for char in chars:
            if char not in mapping:
                return False

            mapping = mapping[char]

        return True

    def add_word(self, word: str) -> None:
        self.insert(word)

    def search_subword(self, word: str, mapping=None) -> bool:
        chars = [char for char in word]
        if mapping is None:
            mapping = self.mapping

        if not chars:
            return 'word' in mapping

        char = chars[0]
        next_chars = chars[1:]
        subword = ''.join(next_chars)

        if char == '.':
            for char in mapping:
                if char == 'word':
                    continue

                if self.search_subword(subword, mapping[char]):
                    return True

            return False
        elif char not in mapping:
            return False
        else:
            return self.search_subword(
                subword, mapping[char]
            )


class Solution:
    def searchWords(
        self, board, trie_mapping, char_map,
        used_coords=None, found_words=None, word=''
    ):
        # print('WORD', word, trie_mapping)
        height, width = len(board), len(board[0])
        word_found = False

        if found_words is None:
            found_words = set()
        if used_coords is None:
            used_coords = []

        if 'word' in trie_mapping:
            found_words.add(trie_mapping['word'])
            word_found = True
            # print('ADDED', found_words)

        if len(used_coords) == 0:
            for char in trie_mapping:
                if char == 'word':
                    continue
                if char not in char_map:
                    continue

                usable_coords = char_map[char]
                for coord in usable_coords:
                    self.searchWords(
                        board, trie_mapping=trie_mapping[char],
                        char_map=char_map, used_coords=[coord],
                        found_words=found_words, word=char
                    )
        else:
            last_coord = used_coords[-1]
            del_chars = set()

            for (k, i) in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                new_coord_orig = (
                    last_coord[0] + i, last_coord[1] + k
                )
                new_coord = (
                    max(0, min(last_coord[0] + i, height - 1)),
                    max(0, min(last_coord[1] + k, width - 1))
                )

                if new_coord_orig != new_coord:
                    continue

                new_char = board[new_coord[0]][new_coord[1]]
                if new_char not in trie_mapping:
                    continue
                if new_coord in used_coords:
                    continue

                word_found, _ = self.searchWords(
                    board, trie_mapping=trie_mapping[new_char],
                    char_map=char_map, used_coords=used_coords + [new_coord],
                    found_words=found_words, word=word+new_char
                )

                if word_found:
                    del_chars.add(new_char)

            for char in del_chars:
                # del trie_mapping[char]
                pass

        return found_words, word_found

    def findWords(
        self, board: List[List[str]], words: List[str]
    ) -> List[str]:
        char_map = {}
        char_counts = {}
        board_charset = set()
        trie = WordDictionary()

        for word in words:
            trie.add_word(word)

        for k in range(len(board)):
            for i in range(len(board[0])):
                char = board[k][i]
                board_charset.add(char)

                if char not in char_map:
                    char_map[char] = []
                    char_counts[char] = 0

                char_map[char].append((k, i))
                char_counts[char] += 1

        found_words = self.searchWords(
            board=board, trie_mapping=trie.mapping,
            char_map=char_map
        )[0]

        return list(found_words)


if __name__ == '__main__':
    board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
    words = ["oa","oaa"]

    soln = Solution()
    valid_words = soln.findWords(board, words)
    print(valid_words)
