from src.extractors.extractor_interface import ExtractorInterface

class SecurityExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to security mechanisms.
        """
        snippets = []
        security_keywords = ["capable", "security_", "selinux_", "smack_", "apparmor_"]
        for keyword in security_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
