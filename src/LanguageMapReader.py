import json

class LanguageMapReader:
    """
    A class that reads the language map and retains a dictionary for easy translation later.
    Expects a json file. Will throw an error otherwise.
    """
    def __init__(self, language_map_path):
        self.language_map_path = language_map_path
        self.map = {}
        try:
            file_reader = open(self.language_map_path, "r")
            self.map = json.loads(file_reader.read())
        except FileNotFoundError:
            print("File at " + language_map_path + " was not found.")
        except json.JSONDecodeError:
            print("The language map provided is not valid json.")
        finally:
            file_reader.close()