from models.schemas import NetSalaryResponse

class NetSalaryCalculator:
    # Statutory constants
    SI_RATE = 0.08
    HI_RATE = 0.015
    UI_RATE = 0.01

    PERSONAL_ALLOWANCE = 11_000_000
    DEPENDENT_ALLOWANCE = 4_400_000

    TAX_TABLE = [
        (5_000_000, 0.05),
        (10_000_000, 0.1),
        (18_000_000, 0.15),
        (32_000_000, 0.2),
        (52_000_000, 0.25),
        (80_000_000, 0.3),
        (float("inf"), 0.35)
    ]

    @classmethod
    def calculate(cls, gross: float, dependents: int) -> NetSalaryResponse:
        insurance = cls._compute_insurance(gross)
        deductions = cls._compute_deductions(dependents)
        taxable = max(gross - insurance - deductions, 0)
        tax = cls._compute_tax(taxable)
        net = gross - insurance - tax

        return NetSalaryResponse(
            gross_salary=gross,
            net_salary=net,
            insurance_fee=insurance,
            tax_due=tax
        )

    @classmethod
    def _compute_insurance(cls, gross: float) -> float:
        return gross * (cls.SI_RATE + cls.HI_RATE + cls.UI_RATE)

    @classmethod
    def _compute_deductions(cls, dependents: int) -> float:
        return cls.PERSONAL_ALLOWANCE + dependents * cls.DEPENDENT_ALLOWANCE

    @classmethod
    def _compute_tax(cls, income: float) -> float:
        tax = 0
        prev_limit = 0
        for threshold, rate in cls.TAX_TABLE:
            if income > prev_limit:
                amount = min(income, threshold) - prev_limit
                tax += amount * rate
                prev_limit = threshold
            else:
                break
        return tax
