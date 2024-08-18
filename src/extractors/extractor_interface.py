from abc import ABC, abstractmethod

class ExtractorInterface(ABC):
    @abstractmethod
    def extract_snippets(self, source_code):
        pass
