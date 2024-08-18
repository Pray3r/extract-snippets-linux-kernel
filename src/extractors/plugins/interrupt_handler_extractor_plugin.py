from src.extractors.extractor_interface import ExtractorInterface

class InterruptHandlerExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to interrupt handlers.
        """
        snippets = []
        interrupt_keywords = ["irqreturn_t", "request_irq", "free_irq", "handle_irq"]
        for keyword in interrupt_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
