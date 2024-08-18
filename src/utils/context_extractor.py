class ContextExtractor:
    @staticmethod
    def extract_context(snippet, source_code, lines_before=5, lines_after=5):
        """Extract context around a snippet in the source code."""
        snippet_start = source_code.find(snippet)
        snippet_end = snippet_start + len(snippet)
        
        before_start = max(0, snippet_start - lines_before)
        after_end = min(len(source_code), snippet_end + lines_after)
        
        return source_code[before_start:snippet_start] + snippet + source_code[snippet_end:after_end]
