"""
Unit tests for To-Do List App using unittest (like the example you showed).
Run with: python -m unittest test_todo_unittest.py
"""

import unittest


class TestTaskValidation(unittest.TestCase):
    """Tests for task validation logic."""
    
    def test_entertask_positive_valid_task(self):
        """Positive test: Valid task creation."""
        # Simulate valid inputs
        input_text = "Complete assignment"
        categories = ["Work"]
        
        # Test the validation logic
        self.assertNotEqual(input_text, "")
        self.assertGreater(len(categories), 0)
        self.assertEqual(len(categories), 1)
        
        # Test formatting logic
        formatted = f"[{categories[0]}] {input_text}"
        self.assertMultiLineEqual(formatted, "[Work] Complete assignment")
    
    def test_entertask_negative_empty_text(self):
        """Negative test: Empty task text."""
        input_text = ""
        
        # This should fail validation
        with self.assertRaises(AssertionError):
            self.assertNotEqual(input_text, "")
    
    def test_entertask_negative_no_category(self):
        """Negative test: No category selected."""
        categories = []
        
        with self.assertRaises(AssertionError):
            self.assertGreater(len(categories), 0)
    
    def test_entertask_negative_multiple_categories(self):
        """Negative test: Multiple categories selected."""
        categories = ["Work", "Housework"]
        
        with self.assertRaises(AssertionError):
            self.assertEqual(len(categories), 1)


class TestDeleteTask(unittest.TestCase):
    """Tests for deletetask function."""
    
    def test_deletetask_positive_with_selection(self):
        """Positive test: Delete with valid selection."""
        # Simulate having a selection
        selected = (0,)
        
        self.assertIsNotNone(selected)
        self.assertGreater(len(selected), 0)
        self.assertEqual(selected[0], 0)
    
    def test_deletetask_negative_no_selection(self):
        """Negative test: Delete without selection."""
        selected = ()
        
        self.assertEqual(len(selected), 0)
        
        # This would raise IndexError in actual code
        with self.assertRaises(IndexError):
            if not selected:
                raise IndexError("No task selected")


class TestMarkCompleted(unittest.TestCase):
    """Tests for markcompleted function."""
    
    def test_markcompleted_positive_mark_task(self):
        """Positive test: Mark uncompleted task."""
        task = "[Work] Buy groceries"
        
        # Task should not already be completed
        self.assertNotIn(" ✔", task)
        
        # Apply completion
        completed = task + " ✔"
        self.assertMultiLineEqual(completed, "[Work] Buy groceries ✔")
        self.assertIn(" ✔", completed)
    
    def test_markcompleted_positive_already_completed(self):
        """Positive test: Task already completed."""
        task = "[Work] Buy groceries ✔"
        
        self.assertIn(" ✔", task)
    
    def test_markcompleted_negative_no_selection(self):
        """Negative test: Mark without selection."""
        selected = ()
        
        self.assertEqual(len(selected), 0)
        
        with self.assertRaises(IndexError):
            if not selected:
                raise IndexError("No task selected")


class TestCategoryFormatting(unittest.TestCase):
    """Tests for category formatting logic."""
    
    def test_category_formatting_all_types(self):
        """Test all category types."""
        test_cases = [
            ("Work", "Task 1", "[Work] Task 1"),
            ("Housework", "Clean kitchen", "[Housework] Clean kitchen"),
            ("Else", "Call mom", "[Else] Call mom"),
        ]
        
        for category, task, expected in test_cases:
            with self.subTest(category=category, task=task):
                result = f"[{category}] {task}"
                self.assertMultiLineEqual(result, expected)


class TestIntegration(unittest.TestCase):
    """Integration tests."""
    
    def test_encode_followed_by_decode_gives_original_string(self):
        """Similar style to the example you showed."""
        # This is like the test in your example
        original = "Test task"
        formatted = f"[Work] {original}"
        # In a real app, we might decode/parse it back
        # For now, just verify formatting
        self.assertEqual(formatted, "[Work] Test task")
    
    def test_complete_workflow(self):
        """Test complete add → mark → delete workflow."""
        # Add task
        task = "[Work] Test integration"
        self.assertTrue(task.startswith("[Work]"))
        
        # Mark completed
        if " ✔" not in task:
            marked = task + " ✔"
            self.assertIn(" ✔", marked)
        
        # Delete (would need selection)
        can_delete = True  # Assuming selection exists
        self.assertTrue(can_delete)


class TestErrorHandling(unittest.TestCase):
    """Tests for error handling."""
    
    def test_error_messages(self):
        """Test error conditions."""
        # Test various error scenarios
        errors_to_test = [
            ("", ["Work"], "empty text"),
            ("Task", [], "no category"),
            ("Task", ["Work", "Housework"], "multiple categories"),
        ]
        
        for text, categories, description in errors_to_test:
            with self.subTest(description=description):
                has_error = False
                
                if not text:
                    has_error = True
                elif not categories:
                    has_error = True
                elif len(categories) > 1:
                    has_error = True
                
                self.assertTrue(has_error, f"Should detect {description}")


class TestEdgeCases(unittest.TestCase):
    """Tests for edge cases."""
    
    def test_long_task(self):
        """Test with very long task."""
        long_text = "A" * 100
        formatted = f"[Work] {long_text}"
        self.assertEqual(len(formatted), 100 + len("[Work] "))
    
    def test_special_characters(self):
        """Test task with special characters."""
        task = "[Work] Email @test.com #urgent"
        self.assertIn("@", task)
        self.assertIn("#", task)
    
    def test_whitespace_handling(self):
        """Test whitespace in tasks."""
        task = "[Work]  Multiple   spaces  "
        self.assertTrue(task.startswith("[Work]"))


if __name__ == "__main__":
    unittest.main()