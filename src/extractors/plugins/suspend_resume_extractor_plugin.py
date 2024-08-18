from src.extractors.extractor_interface import ExtractorInterface

class SuspendResumeExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to suspend and resume operations in the kernel.
        """
        snippets = []
        suspend_resume_keywords = ["suspend", "resume", "hibernate", "pm_", "sleep"]
        for keyword in suspend_resume_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
