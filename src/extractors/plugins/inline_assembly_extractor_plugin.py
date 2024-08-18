from src.extractors.extractor_interface import ExtractorInterface

class InlineAssemblyExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to inline assembly code within C functions.
        """
        snippets = []
        asm_keywords = ["asm", "__asm__", "__volatile__", "asm volatile"]
        for keyword in asm_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
