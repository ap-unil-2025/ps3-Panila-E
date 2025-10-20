"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""


def get_numbers_from_user():
    """Get numbers from user until they type 'done'."""
    numbers = []
    while True:
        text = input("Please enter a number (or 'done' to finish): ").strip()
        if text.lower() == "done":
            break
        try:
            numbers.append(float(text))
        except ValueError:
            print("Invalid input; enter a numeric value or 'done'.")
    return numbers
        

    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
   
    numbers = []




def analyze_numbers(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    analysis = {
        "count": count,
        "sum": total,
        "average": total / count,
        "minimum": min(numbers),
        "maximum": max(numbers),
        "even_count": sum(1 for x in numbers if x.is_integer() and int(x) % 2 == 0),
        "odd_count":  sum(1 for x in numbers if x.is_integer() and int(x) % 2 != 0),
    }
    return analysis
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """



def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        print("No analysis to display.")
        return
    print("\nAnalysis Results:")
    print("-" * 20)

    for key,val in analysis.items():
        print(f"{key}: {val}")





def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()