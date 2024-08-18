from src.extractors.extractor_interface import ExtractorInterface

class SchedulerClassExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to scheduler classes in the kernel.
        """
        snippets = []
        scheduler_class_keywords = ["sched_class", "sched_entity", "task_struct", "sched", "load_balance"]
        for keyword in scheduler_class_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
