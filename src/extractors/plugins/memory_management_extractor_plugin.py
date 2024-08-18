from src.extractors.extractor_interface import ExtractorInterface

class MemoryManagementExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to memory management such as page tables, memory allocation, etc.
        """
        snippets = []
        memory_keywords = ["kmalloc", "vmalloc", "memset", "memcpy", "get_free_pages"]
        for keyword in memory_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
