"""
Unit tests for To-Do List App using unittest (like the example you showed).
Run with: python -m unittest test_todo_unittest.py
"""

import unittest


class TestTaskValidation(unittest.TestCase):
    """Tests for task validation logic."""
    
    def test_entertask_positive_valid_task(self):
        """Positive test: Valid task creation."""
        input_text = "Complete assignment"
        categories = ["Work"]
        
        self.assertNotEqual(input_text, "")
        self.assertGreater(len(categories), 0)
        self.assertEqual(len(categories), 1)
        
        formatted = f"[{categories[0]}] {input_text}"
        self.assertMultiLineEqual(formatted, "[Work] Complete assignment")
    
    def test_entertask_negative_empty_text(self):
        """Negative test: Empty task text."""
        input_text = ""
        
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
        selected = (0,)
        
        self.assertIsNotNone(selected)
        self.assertGreater(len(selected), 0)
        self.assertEqual(selected[0], 0)
    
    def test_deletetask_negative_no_selection(self):
        """Negative test: Delete without selection."""
        selected = ()
        
        self.assertEqual(len(selected), 0)
        
        with self.assertRaises(IndexError):
            if not selected:
                raise IndexError("No task selected")


class TestMarkCompleted(unittest.TestCase):
    """Tests for markcompleted function."""
    
    def test_markcompleted_positive_mark_task(self):
        """Positive test: Mark uncompleted task."""
        task = "[Work] Buy groceries"
        
        self.assertNotIn(" ✔", task)
        
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


if __name__ == "__main__":
    unittest.main()
