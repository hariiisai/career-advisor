from project import ask_details,ask_questions,determine_role
import sys
import io

def test_ask_details(monkeypatch):
    simulated_inputs = ('Hari', 'UG')  # Simulated user inputs
    expected_output = ('Hari', 'ug')
    monkeypatch.setattr('sys.stdin', io.StringIO('\n'.join(simulated_inputs)))
    assert ask_details() == expected_output

def test_ask_questions(monkeypatch):
    simulated_inputs = ['yes', 'no', 'no', 'no']  # Simulated user inputs
    expected_output = ['yes', 'no', 'no', 'no']

    # Use monkeypatch to simulate user input
    monkeypatch.setattr('sys.stdin', io.StringIO('\n'.join(simulated_inputs)))

    # Call the function that takes user input
    assert ask_questions() == expected_output

def test_determine_role():
    assert determine_role(['yes', 'no', 'yes', 'no']) == "Software Developer"

