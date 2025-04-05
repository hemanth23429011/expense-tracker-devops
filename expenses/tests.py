from django.test import TestCase
from datetime import date
from expenses.models import Expense  # Replace 'expenses' with your app name

class ExpenseModelTest(TestCase):

    def setUp(self):
        self.expense = Expense.objects.create(
            title="Grocery Shopping",
            amount=120.50,
            category="Food",
            date=date(2024, 4, 5)
        )

    def test_expense_creation(self):
        self.assertEqual(self.expense.title, "Grocery Shopping")
        self.assertEqual(self.expense.amount, 120.50)
        self.assertEqual(self.expense.category, "Food")
        self.assertEqual(self.expense.date, date(2024, 4, 5))

    def test_expense_str_method(self):
        self.assertEqual(str(self.expense), "Grocery Shopping - 120.50")
