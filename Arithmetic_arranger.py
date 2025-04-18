def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = []
    second_line = []
    dash_line = []
    result_line = []
    
    for problem in problems:
        num1, operator, num2 = problem.split()
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(num1), len(num2)) + 2
        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        dash_line.append('-' * width)
        
        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            result_line.append(result.rjust(width))
    
    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dash_line)
    
    if show_answers:
        arranged_problems += "\n" + "    ".join(result_line)
    
    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))