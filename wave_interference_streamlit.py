import streamlit as st

def phase_quiz():
    st.title("Interactive Phase Contrast Quiz")
    
    questions = [
        {"question": "1. What happens when two waves meet in a medium?", 
         "options": ["They pass through each other unchanged", "They interfere, either constructively or destructively", "They stop moving", "They disappear"],
         "answer": "They interfere, either constructively or destructively",
         "explanation": "When two waves meet, their amplitudes combine due to the principle of superposition, leading to constructive or destructive interference."},
        
        {"question": "2. What determines whether interference is constructive or destructive?", 
         "options": ["The amplitude of the waves", "The phase difference between the waves", "The frequency of the waves", "The speed of the waves"],
         "answer": "The phase difference between the waves",
         "explanation": "Interference type is determined by phase difference: in-phase waves reinforce (constructive), out-of-phase waves cancel (destructive)."},
        
        {"question": "3. When light passes through a transparent material, what changes?", 
         "options": ["Its color", "Its intensity", "Its phase", "Its wavelength"],
         "answer": "Its phase",
         "explanation": "Transparent materials shift the phase of light without significantly absorbing it, making phase contrast microscopy useful for visualization."},
        
        {"question": "4. In cryo-EM, what happens when electrons pass through a biological sample?", 
         "options": ["They slow down", "They get absorbed", "They experience a phase shift", "They change color"],
         "answer": "They experience a phase shift",
         "explanation": "Electrons do not slow down significantly but experience phase shifts when interacting with the electrostatic potential of biological samples."},
        
        {"question": "5. Why do we need phase contrast techniques in cryo-EM?", 
         "options": ["Because biological samples strongly absorb electrons", "Because biological samples mainly cause phase shifts, not amplitude changes", "Because electrons cannot interfere", "Because it increases sample temperature"],
         "answer": "Because biological samples mainly cause phase shifts, not amplitude changes",
         "explanation": "Biological samples in cryo-EM cause phase shifts rather than absorbing electrons, making phase contrast methods necessary for visualization."}
    ]
    
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    
    for q in questions:
        st.subheader(q["question"])
        selected_answer = st.radio("Choose an answer:", q["options"], key=q["question"], index=None)
        
        if selected_answer:
            st.session_state.answers[q["question"]] = selected_answer
            
            if selected_answer == q["answer"]:
                st.success(f"✅ Correct: {q['explanation']}")
            else:
                st.error(f"❌ Incorrect. Correct answer: {q['answer']}. {q['explanation']}")
    
    if st.button("Try Again"):
        st.session_state.answers = {}
        st.rerun()

if __name__ == "__main__":
    phase_quiz()
