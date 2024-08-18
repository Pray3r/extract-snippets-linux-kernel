from src.extractors.extractor_interface import ExtractorInterface

class RealtimeSchedulerExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to real-time scheduling mechanisms.
        """
        snippets = []
        realtime_keywords = ["rt_", "sched_rt", "rt_sched", "sched_fifo", "sched_rr"]
        for keyword in realtime_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
