from src.LanguageMapReader import LanguageMapReader
from src.LexerTranslator import LexerTranslator
from src.TranslatorOutputFormatter import TranslatorOutputFormatter

# Get the code to translate
test_code = open("test_cases/spanish/spanish_script.py").read()
# Get the language map
language_map = LanguageMapReader('test_cases/spanish/spanish_language_map_python.json')
# translate and output
translator = LexerTranslator(test_code, language_map)
# Get output formatter
formatter = TranslatorOutputFormatter(translator)

translator.tokenize()
print(formatter.output_string())
