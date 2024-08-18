from src.extractors.extractor_interface import ExtractorInterface

class WorkqueueExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to workqueue mechanisms in the kernel.
        """
        snippets = []
        workqueue_keywords = ["workqueue", "queue_work", "INIT_WORK", "flush_work", "schedule_work"]
        for keyword in workqueue_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
