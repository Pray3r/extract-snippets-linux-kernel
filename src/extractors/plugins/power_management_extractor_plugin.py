from src.extractors.extractor_interface import ExtractorInterface

class PowerManagementExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to power management like suspend, resume, and power-saving features.
        """
        snippets = []
        power_keywords = ["suspend", "resume", "power_save", "pm_", "device_pm"]
        for keyword in power_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
