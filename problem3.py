"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""
import statistics

def get_numbers_from_user():
    text=input("Please enter a number : ")
    res=[]
    while text != "done":
        try:
            res.append(float(text))
            text=input("Please enter a number : ")
        except ValueError:
            text=input("Please enter a number : ")
    return (res)
        

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
    dic={}
    dic["count"]=len(numbers)
    dic["sum"]=sum(numbers)
    dic["average"]=sum(numbers)/len(numbers)
    dic["mini"]=min(numbers)
    dic["maxi"]=max(numbers)
    dic["even_count"]=len([x for x in numbers if x % 2 == 0])
    dic["odd_count"]=len([x for x in numbers if x % 2 != 0])
    return dic
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

    print("\nAnalysis Results:")
    print("-" * 20)

    for key,val in analysis.items():
        print(key, ": ", val)
    if not analysis:
        return




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