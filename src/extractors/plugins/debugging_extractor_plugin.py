from src.extractors.extractor_interface import ExtractorInterface

class DebuggingExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to debugging mechanisms.
        """
        snippets = []
        debugging_keywords = ["printk", "pr_debug", "dump_stack", "BUG_ON", "WARN_ON"]
        for keyword in debugging_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
