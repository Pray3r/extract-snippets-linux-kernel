from src.extractors.extractor_interface import ExtractorInterface

class LinkedListExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to linked list operations in the kernel.
        """
        snippets = []
        linked_list_keywords = ["list_head", "list_add", "list_del", "list_for_each", "hlist_"]
        for keyword in linked_list_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
