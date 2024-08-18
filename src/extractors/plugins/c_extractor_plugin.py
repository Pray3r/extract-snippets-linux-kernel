from src.extractors.extractor_interface import ExtractorInterface

class CExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract general C language snippets, such as function definitions, structures, etc.
        """
        snippets = []
        c_keywords = ["void", "int", "char", "struct", "typedef", "enum", "union"]
        for keyword in c_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
