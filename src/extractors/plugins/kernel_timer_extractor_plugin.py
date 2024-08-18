from src.extractors.extractor_interface import ExtractorInterface

class KernelTimerExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to kernel timer operations.
        """
        snippets = []
        timer_keywords = ["init_timer", "mod_timer", "del_timer", "add_timer", "hrtimer"]
        for keyword in timer_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
