class InvalidFormulaException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def evaluate_formula(formula):
    try:
        operand1, operator, operand2 = formula.split()
    except ValueError as e:
        raise InvalidFormulaException(e)
        
    if not operand1.isdigit() or not operand2.isdigit():
        raise InvalidFormulaException("Operands should be int numbers")

    if operator == "+":
        return int(operand1) + int(operand2)
    elif operator == "-":
        return int(operand1) - int(operand2)
    elif operator == "*":
        return int(operand1) * int(operand2)
    elif operator == "/":
        return int(operand1) / int(operand2)
    else:
        raise InvalidFormulaException("Invalid operator")


if __name__ == "__main__":
    try:
        formula = input("Enter the formula: ")
        result = evaluate_formula(formula)
    except InvalidFormulaException as e:
        print(f"Invalid formula: {e}")
    except Exception as e:
        print(f"Error: {e}, type: {type(e)}")
    else:
        print(f"Result: {result}")

