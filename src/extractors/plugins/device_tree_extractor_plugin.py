from src.extractors.extractor_interface import ExtractorInterface

class DeviceTreeExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to device tree operations and management.
        """
        snippets = []
        device_tree_keywords = ["of_", "device_tree", "dt_", "of_find", "of_node"]
        for keyword in device_tree_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
