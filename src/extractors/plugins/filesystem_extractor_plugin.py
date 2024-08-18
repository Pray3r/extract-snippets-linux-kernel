from src.extractors.extractor_interface import ExtractorInterface

class FilesystemExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to file system operations and management.
        """
        snippets = []
        filesystem_keywords = ["inode", "dentry", "super_block", "vfs_", "fs_", "ext4_"]
        for keyword in filesystem_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
