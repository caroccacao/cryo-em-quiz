from IPython.display import display, clear_output

def phase_quiz():
    questions = [
        {"question": "1. What happens when two waves meet in a medium?", 
         "options": ["A) They pass through each other unchanged", "B) They interfere, either constructively or destructively", "C) They stop moving", "D) They disappear"],
         "answer": "B",
         "explanation": "When two waves meet, their amplitudes combine due to the principle of superposition, leading to constructive or destructive interference."},
        
        {"question": "2. What determines whether interference is constructive or destructive?", 
         "options": ["A) The amplitude of the waves", "B) The phase difference between the waves", "C) The frequency of the waves", "D) The speed of the waves"],
         "answer": "B",
         "explanation": "Interference type is determined by phase difference: in-phase waves reinforce (constructive), out-of-phase waves cancel (destructive)."},
        
        {"question": "3. When light passes through a transparent material, what changes?", 
         "options": ["A) Its color", "B) Its intensity", "C) Its phase", "D) Its wavelength"],
         "answer": "C",
         "explanation": "Transparent materials shift the phase of light without significantly absorbing it, making phase contrast microscopy useful for visualization."},
        
        {"question": "4. In cryo-EM, what happens when electrons pass through a biological sample?", 
         "options": ["A) They slow down", "B) They get absorbed", "C) They experience a phase shift", "D) They change color"],
         "answer": "C",
         "explanation": "Electrons do not slow down significantly but experience phase shifts when interacting with the electrostatic potential of biological samples."},
        
        {"question": "5. Why do we need phase contrast techniques in cryo-EM?", 
         "options": ["A) Because biological samples strongly absorb electrons", "B) Because biological samples mainly cause phase shifts, not amplitude changes", "C) Because electrons cannot interfere", "D) Because it increases sample temperature"],
         "answer": "B",
         "explanation": "Biological samples in cryo-EM cause phase shifts rather than absorbing electrons, making phase contrast methods necessary for visualization."}
    ]
    
    student_answers = {}
    score = 0
    
    for q in questions:
        clear_output(wait=True)
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        student_answers[q["question"]] = answer
        
        if answer == q["answer"]:
            score += 1
            print("Correct!", q["explanation"])
        else:
            print(f"Incorrect. The correct answer is {q['answer']}. {q['explanation']}")
        input("Press Enter to continue...")
    
    clear_output(wait=True)
    print("Quiz Completed! Here are the correct answers:\n")
    
    for q in questions:
        print(q["question"])
        print(f"Your answer: {student_answers[q['question']]} | Correct answer: {q['answer']}")
        print(f"Explanation: {q['explanation']}\n")
    
    print(f"Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("Excellent! You fully understand phase contrast in cryo-EM.")
    elif score >= len(questions) * 0.7:
        print("Good job! You have a solid understanding, but review some details.")
    else:
        print("Keep practicing! Reviewing phase contrast will help.")

# Run the quiz
phase_quiz()
