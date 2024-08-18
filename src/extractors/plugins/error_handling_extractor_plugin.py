from src.extractors.extractor_interface import ExtractorInterface

class ErrorHandlingExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to error handling and recovery mechanisms.
        """
        snippets = []
        error_handling_keywords = ["try", "catch", "finally", "error", "fail"]
        for keyword in error_handling_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
