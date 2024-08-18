from src.extractors.extractor_interface import ExtractorInterface

class BufferManagementExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to buffer management.
        """
        snippets = []
        buffer_keywords = ["buffer", "ring_buffer", "page_buffer", "buf", "kfifo"]
        for keyword in buffer_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
