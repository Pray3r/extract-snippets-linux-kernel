from src.extractors.extractor_interface import ExtractorInterface

class SecurityHooksExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to security hooks.
        """
        snippets = []
        hooks_keywords = ["security_", "lsm_", "hook", "selinux_", "smack_"]
        for keyword in hooks_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
