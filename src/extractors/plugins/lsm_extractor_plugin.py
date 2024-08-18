from src.extractors.extractor_interface import ExtractorInterface

class LSMExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to Linux Security Modules (LSM).
        """
        snippets = []
        lsm_keywords = ["security_", "selinux_", "smack_", "apparmor_", "lsm_"]
        for keyword in lsm_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
