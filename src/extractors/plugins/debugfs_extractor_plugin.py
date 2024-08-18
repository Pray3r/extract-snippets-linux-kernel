from src.extractors.extractor_interface import ExtractorInterface

class DebugfsExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to debugfs operations.
        """
        snippets = []
        debugfs_keywords = ["debugfs_create", "debugfs_remove", "debugfs_", "file_operations", "seq_file"]
        for keyword in debugfs_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
