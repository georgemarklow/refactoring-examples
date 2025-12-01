import unittest
from workflow1 import run_workflow1
from workflow2 import run_workflow2

class TestWorkflow1(unittest.TestCase):

    def test_run_workflow1(self):
        # Arrange
        expected_output = 'criticality: 3, results above 5'

        # Act
        result = run_workflow1()
        
        # Assert
        self.assertEqual(expected_output, result) 

    def test_run_workflow2(self):
        # Arrange
        expected_output = 'd-index: 458.90000000000003'

        # Act
        result = run_workflow2()
        
        # Assert
        self.assertEqual(expected_output, result) 

if __name__ == '__main__':
    unittest.main()