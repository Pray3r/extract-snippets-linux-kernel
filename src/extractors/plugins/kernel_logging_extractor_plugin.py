from src.extractors.extractor_interface import ExtractorInterface

class KernelLoggingExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to kernel logging mechanisms.
        """
        snippets = []
        logging_keywords = ["printk", "pr_info", "pr_err", "pr_debug", "log_buf"]
        for keyword in logging_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
