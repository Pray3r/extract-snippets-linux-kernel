import unittest
from src.utils.control_flow_analyzer import ControlFlowAnalyzer

class TestControlFlowAnalyzer(unittest.TestCase):
    def test_analyze_control_flow(self):
        snippet = "if (x > 0) { y = 1; } else { y = -1; }"
        analysis_result = ControlFlowAnalyzer.analyze_control_flow(snippet)
        self.assertIn("Control flow analysis results", analysis_result)

if __name__ == '__main__':
    unittest.main()
