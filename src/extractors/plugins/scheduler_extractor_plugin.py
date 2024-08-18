from src.extractors.extractor_interface import ExtractorInterface

class SchedulerExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to scheduling mechanisms in the kernel.
        """
        snippets = []
        scheduler_keywords = ["schedule", "sched_init", "sched_yield", "wake_up", "task_struct"]
        for keyword in scheduler_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
