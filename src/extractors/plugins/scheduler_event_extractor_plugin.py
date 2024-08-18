from src.extractors.extractor_interface import ExtractorInterface

class SchedulerEventExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to scheduler events.
        """
        snippets = []
        event_keywords = ["wake_up", "sleep", "schedule", "sched_event", "cpu_idle"]
        for keyword in event_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
