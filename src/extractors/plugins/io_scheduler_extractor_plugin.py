from src.extractors.extractor_interface import ExtractorInterface

class IOSchedulerExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to I/O scheduling mechanisms.
        """
        snippets = []
        io_scheduler_keywords = ["elevator", "io_schedule", "blk_", "rq_", "bio_"]
        for keyword in io_scheduler_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
