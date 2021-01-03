import logging
from business_logic import LanguageMapReader
from business_logic import TranslatorOutputFormatter
from business_logic import LexerTranslator
 
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    # Get parameters from request
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("The correct fields were not found in the request body. Please reference the API documentation.", status_code=400)
    else:
        natural_language = req_body.get('naturalLanguage')
        source_code = req_body.get('sourceCode')
        programming_language = req_body.get('programmingLanguage')

    if natural_language and source_code and programming_language:
        language_map = LanguageMapReader('source-code-translations/spanish/spanish_language_map_python.json')
        translator = LexerTranslator(source_code, language_map)
        translator.tokenize()
        formatter = TranslatorOutputFormatter(translator)
        return func.HttpResponse({ translated_source: formatter.output_string()}, status_code=200)
    else:
        return func.HttpResponse(
             "Shouldn't hit this.",
             status_code=500
        )
