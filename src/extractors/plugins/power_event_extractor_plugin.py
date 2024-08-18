from src.extractors.extractor_interface import ExtractorInterface

class PowerEventExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to power events and management.
        """
        snippets = []
        power_event_keywords = ["power_event", "suspend", "resume", "power_save", "pm_"]
        for keyword in power_event_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
