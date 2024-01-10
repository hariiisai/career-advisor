def ask_details():
    # Welcome message 
    print("Welcome to the Career Advisor!")
    print("Please answer the following questions to find the best-suited role for you.")

    name = input("Please Enter Your Name: ").title()
    higher_edu = input("Please Enter Your Highest Education Qualification (UG/G/PG):").lower()
    while higher_edu not in ['ug', 'g', 'pg']:
            print("Please enter 'UG', 'G' or 'PG'.")
            higher_edu = input("Please Enter Your Highest Education Qualification (UG/G/PG):").lower()
    return name,higher_edu

def ask_questions():

    questions = [
        "Do you enjoy programming? (Yes/No): ",
        "Are you more interested in data analysis? (Yes/No): ",
        "Do you prefer creating something new? (Yes/No): ",
        "Are you good at deriving insights from large amounts of data? (Yes/No): ",
        # We can add more questions here...
    ]

    user_responses = []

    for question in questions:
        response = input(question).strip().lower()
        while response not in ['yes', 'no']:
            print("Please enter 'Yes' or 'No'.")
            response = input(question).strip().lower()
        user_responses.append(response)

    return user_responses


def determine_role(responses):
    programming_interest, data_analysis, creating_new, deriving_insights = responses

    # Logic to determine the best-suited role based on user responses
    # We can implement one more logic with user's higher education
    if programming_interest == 'yes':
        if creating_new == 'yes':
            return "Software Developer"
        else:
            return "Software Engineer"
    else:
        if data_analysis == 'yes':
            if deriving_insights == 'yes':
                return "Data Scientist"
            else:
                return "Data Engineer"
        else:
            return "Support Engineer"

def main():
    name, higher_edu = ask_details()
    user_responses = ask_questions()
    recommended_role = determine_role(user_responses)
    print(f"Hi {name}, Based on your responses, the recommended role for you is: {recommended_role}")

if __name__ == "__main__":
    main()
