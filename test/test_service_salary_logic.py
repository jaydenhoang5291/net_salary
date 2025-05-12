import pytest
from backend.services.calculator import NetSalaryCalculator
from backend.models.schemas import NetSalaryResponse

class TestSalaryLogic:
    def test_insurance_deduction(self):
        income = 15000000
        value = NetSalaryCalculator._compute_insurance(income)
        expected = income * (0.08 + 0.015 + 0.01)
        assert round(value, 2) == round(expected, 2)

    def test_deduction_dependents(self):
        assert NetSalaryCalculator._compute_deductions(0) == 11000000
        assert NetSalaryCalculator._compute_deductions(3) == 11000000 + 3 * 4400000

    def test_tax_computation(self):
        assert NetSalaryCalculator._compute_tax(0) == 0
        assert NetSalaryCalculator._compute_tax(4000000) == 4000000 * 0.05

        income = 15000000
        tax = NetSalaryCalculator._compute_tax(income)
        assert tax > 0

    def test_full_conversion(self):
        gross = 25000000
        dependents = 2
        result = NetSalaryCalculator.calculate(gross, dependents)
        assert result.__class__.__name__ == "NetSalaryResponse"
        assert result.net_salary < gross
