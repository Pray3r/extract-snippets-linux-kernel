from src.extractors.extractor_interface import ExtractorInterface

class VFSExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to the Virtual File System (VFS).
        """
        snippets = []
        vfs_keywords = ["vfs_", "dentry", "inode", "super_block", "mnt_", "file_"]
        for keyword in vfs_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
