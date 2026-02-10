import streamlit as st

def phase_quiz():
    st.title("Interactive Phase Contrast Quiz")

    questions_phase = [
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

    questions_cryoEM = [
        {"question": "1. How many genes does Salmonella have?",
         "options": ["~500", "~1,500", "~4,500", "~20,000"],
         "answer": "~4,500",
         "explanation": "Most Salmonella strains contain roughly 4,000–5,000 genes, reflecting typical bacterial genome complexity."},

        {"question": "2. Approximately how many proteins are present in a typical bacterial cell?",
         "options": ["~1,000", "~100,000", "~2–3 million", "~100 million"],
         "answer": "~2–3 million",
         "explanation": "Cells contain millions of protein molecules, illustrating the dense molecular environment inside living cells."},

        {"question": "3. What is the typical size range of a protein?",
         "options": ["0.1–1 nm", "2–10 nm", "100–500 nm", "1–5 µm"],
         "answer": "2–10 nm",
         "explanation": "Most proteins are only a few nanometers in size, which explains why high-resolution imaging methods are required."},

        {"question": "4. Which radiation source is used in cryo-electron microscopy?",
         "options": ["Visible light", "X-rays", "Electrons", "Ultraviolet light"],
         "answer": "Electrons",
         "explanation": "Electrons have much shorter wavelengths than visible light, allowing atomic-resolution imaging."},

        {"question": "5. Which resolution can modern cryo-EM achieve for high-quality samples?",
         "options": ["~10 Å", "~5 Å", "~2–3 Å", "~0.1 Å"],
         "answer": "~2–3 Å",
         "explanation": "Modern cryo-EM can reach near-atomic resolution under optimal experimental conditions."},

        {"question": "6. What is the typical pH of uranyl acetate staining solution?",
         "options": ["~2–4", "~7", "~10", "~13"],
         "answer": "~2–4",
         "explanation": "Uranyl acetate is acidic and commonly used in negative stain EM to enhance contrast."},

        {"question": "7. Who received the 2017 Nobel Prize in Chemistry for cryo-EM development?",
         "options": ["Jacques Dubochet, Joachim Frank, Richard Henderson",
                     "Ernst Ruska, Max Knoll, Dennis Gabor",
                     "Aaron Klug, Rosalind Franklin, Francis Crick",
                     "Kary Mullis, Frederick Sanger, John Walker"],
         "answer": "Jacques Dubochet, Joachim Frank, Richard Henderson",
         "explanation": "They developed cryo-EM methods enabling high-resolution structure determination of biomolecules."}
    ]

    quiz_choice = st.sidebar.selectbox(
        "Select Quiz",
        ["Phase Contrast", "Quiz Day 1"]
    )

    if quiz_choice == "Phase Contrast":
        st.subheader("Quiz: Phase Contrast")
        render_quiz("Quiz: Phase Contrast", questions_phase, key_prefix="phase")
    else:
        st.subheader("Quiz: CryoEM - Day 1")
        render_quiz("Quiz: CryoEM - Day 1", questions_cryoEM, key_prefix="cryoEM")

    if st.sidebar.button("Reset answers"):
        st.rerun()

if __name__ == "__main__":
    phase_quiz()
