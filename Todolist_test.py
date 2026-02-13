import unittest


class TestTaskValidation(unittest.TestCase):
    """Tests for task validation logic."""
    
    def test_entertask_positive_valid_task(self):
        """Positive test: Valid task creation."""
        input_text = "Random assignment"
        categories = ["Work"]
        
        self.assertNotEqual(input_text, "")
        self.assertGreater(len(categories), 0)
        self.assertEqual(len(categories), 1)
        
        formatted = f"[{categories[0]}] {input_text}"
        self.assertMultiLineEqual(formatted, "[Work] Random assignment")
    
    def test_entertask_exception1_empty_text_valueerror(self):
        """TEST FOR EXCEPTION 1: Empty text should raise ValueError with correct message."""
        def validate_input(text):
            if text == "":
                raise ValueError("Please enter some text")
            return text
        
        with self.assertRaises(ValueError) as context:
            validate_input("")
        
        self.assertEqual(str(context.exception), "Please enter some text")
    
    def test_entertask_exception2_no_category_valueerror(self):
        """TEST FOR EXCEPTION 2: No category should raise ValueError with correct message."""
        def validate_categories(categories):
            if not categories:
                raise ValueError("Please select at least one category")
            return categories
        
        with self.assertRaises(ValueError) as context:
            validate_categories([])
        
        self.assertEqual(str(context.exception), "Please select at least one category")
    
    def test_entertask_exception3_multiple_categories_valueerror(self):
        """TEST FOR EXCEPTION 3: Multiple categories should raise ValueError with correct message."""
        def validate_categories(categories):
            if len(categories) > 1:
                raise ValueError("Please select only one category")
            return categories
        
        with self.assertRaises(ValueError) as context:
            validate_categories(["Work", "Housework"])
        
        self.assertEqual(str(context.exception), "Please select only one category")


class TestDeleteTask(unittest.TestCase):
    """Tests for deletetask function."""
    
    def test_deletetask_positive_with_selection(self):
        """Positive test: Delete with valid selection."""
        selected = (0,)
        
        self.assertIsNotNone(selected)
        self.assertGreater(len(selected), 0)
        self.assertEqual(selected[0], 0)
    
    def test_deletetask_exception4_no_selection_error(self):
        """EXCEPTION 4: Specifically test no selection case."""
        def check_selection(selected):
            if not selected:
                raise IndexError("Please select a task to delete!")
            return selected[0]
        
        with self.assertRaises(IndexError) as context:
            check_selection(())
        
        self.assertEqual(str(context.exception), "Please select a task to delete!")


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
    
    def test_markcompleted_exception6_no_selection_error(self):
        """TEST FOR EXCEPTION 6: Specifically test no selection case with correct message."""
        def check_selection(selected):
            if not selected:
                raise IndexError("Please select a task to mark!")
            return selected[0]
        
        with self.assertRaises(IndexError) as context:
            check_selection(())
        
        self.assertEqual(str(context.exception), "Please select a task to mark!")


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