import unittest
from src.utils.data_flow_analyzer import DataFlowAnalyzer

class TestDataFlowAnalyzer(unittest.TestCase):
    def test_analyze_data_flow(self):
        snippet = "int a = b + c; int d = a + e;"
        analysis_result = DataFlowAnalyzer.analyze_data_flow(snippet)
        self.assertIn("Data flow analysis results", analysis_result)

if __name__ == '__main__':
    unittest.main()
