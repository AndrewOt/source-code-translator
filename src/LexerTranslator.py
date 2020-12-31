class LexerTranslator:
    """A class that lexes the input and translates it and returns the translated code."""

    """
    Constructor.
    @param input_stream - <String> The code to be translated
    @param language_map - <Dictionary> The dictionary mapping the foreign language keywords
        to english keywords.
    """
    def __init__(self, input_stream, language_map):
        self.input_stream = input_stream
        self.language_map = language_map
        self.token_queue = []

    """
    Funtion that tokenizes the file and while building a token will check if the word has a translation,
    translate it if able, and add it to the buffer.
    """
    def tokenize(self):
        i = 0
        word_buffer = ""
        for c in self.input_stream:
            if c == ":" or c == "" or c == " " or c == '(' or c == ')':
                if self._is_keyword(word_buffer):
                    word_buffer = self._translate_keyword(word_buffer)
                self.token_queue.append(word_buffer)
                self.token_queue.append(c)
                word_buffer = ""
                i += 1
            else:
                word_buffer += c
                i += 1

    def _is_keyword(self, token_to_check):
        return token_to_check in self.language_map.map

    def _translate_keyword(self, token_to_translate):
        return self.language_map.map[token_to_translate]