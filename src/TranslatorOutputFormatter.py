class TranslatorOutputFormatter:
    def __init__(self, translator):
        self.translator = translator

    def output_string(self):
        return "".join(self.translator.token_queue)