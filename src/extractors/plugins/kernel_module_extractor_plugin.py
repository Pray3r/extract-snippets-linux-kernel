from src.extractors.extractor_interface import ExtractorInterface

class KernelModuleExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to kernel module initialization and cleanup.
        """
        snippets = []
        module_keywords = ["module_init", "module_exit", "MODULE_LICENSE", "MODULE_AUTHOR"]
        for keyword in module_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
