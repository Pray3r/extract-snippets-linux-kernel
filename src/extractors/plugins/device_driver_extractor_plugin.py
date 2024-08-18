from src.extractors.extractor_interface import ExtractorInterface

class DeviceDriverExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to device drivers.
        """
        snippets = []
        driver_keywords = ["pci_driver", "usb_driver", "platform_driver", "dev_", "driver_register"]
        for keyword in driver_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
