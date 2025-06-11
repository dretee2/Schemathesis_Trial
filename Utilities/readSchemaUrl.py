import configparser
import ast


class ReadSchemaProperties:
    def __init__(self, file_path=r"C:\Users\BAB AL SAFA\PycharmProjects\Schemathesis_Project\configurations\config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(file_path)
        self.schema_section = "common Schema data"

    def _get_schema_dict(self, key):
        if self.schema_section not in self.config or key not in self.config[self.schema_section]:
            raise KeyError(f"Schema key '{key}' not found in section '{self.schema_section}'")
        try:
            return ast.literal_eval(self.config[self.schema_section][key])
        except Exception as e:
            raise ValueError(f"Error parsing schema entry '{key}': {e}")

    def get_alerts_schema(self):
        return self._get_schema_dict("Alerts_Schema_Details")

    def get_user_management_schema(self):
        return self._get_schema_dict("User_Management_Schema_Details")

    def get_recommendation_schema(self):
        return self._get_schema_dict("Recommendation_Schema_Details")

    def get_chats_schema(self):
        return self._get_schema_dict("Chats_Schema_Details")
