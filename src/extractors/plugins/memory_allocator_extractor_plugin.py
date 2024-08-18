from src.extractors.extractor_interface import ExtractorInterface

class MemoryAllocatorExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to memory allocation mechanisms.
        """
        snippets = []
        allocator_keywords = ["kmalloc", "vmalloc", "alloc", "get_free_pages", "kzalloc"]
        for keyword in allocator_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
