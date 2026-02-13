import streamlit as st


def render_quiz(title: str, questions: list[dict], key_prefix: str = "quiz"):
    st.subheader(title)

    correct = 0
    answered = 0

    for i, q in enumerate(questions, start=1):
        st.markdown(f"**{q['question']}**")

        key = f"{key_prefix}_q{i}"
        choice = st.radio(
            label="",
            options=q["options"],
            key=key,
            index=None,
        )

        if choice is None:
            st.divider()
            continue

        answered += 1
        is_correct = (choice == q["answer"])
        correct += int(is_correct)

        if is_correct:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Not quite. Correct answer: **{q['answer']}**")

        st.caption(q.get("explanation", ""))
        st.divider()

    # Sidebar score
    st.sidebar.markdown("### Score")
    st.sidebar.write(f"Answered: **{answered}/{len(questions)}**")
    st.sidebar.write(f"Correct: **{correct}/{len(questions)}**")
    st.sidebar.progress(correct / max(len(questions), 1))


def phase_quiz():
    st.title("CryoEM Course 2026 Quizzes")

    # ----------------------
    # Question banks
    # ----------------------
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
         "explanation": "They developed cryo-EM methods enabling high-resolution structure determination of biomolecules."},
    ]

    questions_phase = [
        {"question": "1. What happens when two waves meet in a medium?",
         "options": ["They pass through each other unchanged",
                     "They interfere, either constructively or destructively",
                     "They stop moving", "They disappear"],
         "answer": "They interfere, either constructively or destructively",
         "explanation": "When two waves meet, their amplitudes add up (superposition), leading to constructive or destructive interference."},

        {"question": "2. What determines whether interference is constructive or destructive?",
         "options": ["The amplitude of the waves", "The phase difference between the waves", "The frequency of the waves", "The speed of the waves"],
         "answer": "The phase difference between the waves",
         "explanation": "In-phase waves reinforce (constructive), out-of-phase waves cancel (destructive)."},
        
        {"question": "3. When light passes through a transparent material, what changes?",
         "options": ["Its color", "Its intensity", "Its phase", "Its wavelength"],
         "answer": "Its phase",
         "explanation": "Transparent materials typically shift phase without strong absorption."},

        {"question": "4. In cryo-EM, what happens when electrons pass through a biological sample?",
         "options": ["They slow down", "They get absorbed", "They experience a phase shift", "They change color"],
         "answer": "They experience a phase shift",
         "explanation": "Electrons mainly experience phase shifts from the sample’s electrostatic potential."},

        {"question": "5. Why do we need phase contrast techniques in cryo-EM?",
         "options": ["Because biological samples strongly absorb electrons",
                     "Because biological samples mainly cause phase shifts, not amplitude changes",
                     "Because electrons cannot interfere",
                     "Because it increases sample temperature"],
         "answer": "Because biological samples mainly cause phase shifts, not amplitude changes",
         "explanation": "Biological samples are weak-phase objects, so phase contrast is essential."},
    ]

    questions_modelling = [
        {"question": "1. In cryo-EM, a molecular model is best described as:",
         "options": ["A raw experimental image",
                     "A mathematical filter applied to images",
                     "An interpretation of the density map based on prior structural knowledge",
                     "A list of amino acid sequences"],
         "answer": "An interpretation of the density map based on prior structural knowledge",
         "explanation": "A molecular model is an interpreted atomic representation fitted to the cryo-EM density map."},

        {"question": "2. Which of the following is NOT a common application of molecular modelling?",
         "options": ["Comparing molecular structures",
                     "Visualizing macromolecular complexes",
                     "Predicting molecular interactions",
                     "Measuring gene expression levels"],
         "answer": "Measuring gene expression levels",
         "explanation": "Gene expression is measured with transcriptomics/proteomics methods, not modelling."},

        {"question": "3. What does “de novo” modelling refer to?",
         "options": ["Building a model without prior structural templates",
                     "Refining an existing crystal structure",
                     "Simulating molecular motion over time",
                     "Aligning protein sequences"],
         "answer": "Building a model without prior structural templates",
         "explanation": "De novo modelling means building a model from scratch without a template."},

        {"question": "4. Which resolution range typically allows backbone tracing in cryo-EM maps?",
         "options": [">10 Å", "~5 Å or better", "~20 Å", "Only atomic resolution (<1 Å)"],
         "answer": "~5 Å or better",
         "explanation": "Around ~5 Å (and better), backbone tracing becomes feasible; side chains need higher resolution."},

        {"question": "5. Which of the following is a software package used for molecular modelling (and NOT a ninja turtle)?",
         "options": ["Modelnatello", "Modelphael", "Modelnardo", "Modelangelo"],
         "answer": "Modelangelo",
         "explanation": "ModelAngelo is a real cryo-EM model-building tool."},
    ]

    # ----------------------
    # Quiz selection
    # ----------------------
    quiz_choice = st.sidebar.selectbox(
        "Select Quiz",
        ["Quiz Day 1 - CryoEM Warm-up", "Quiz Day 2 - Phase Contrast", "Quiz Day 3 - Molecular Modelling"],
    )

    if quiz_choice == "Quiz Day 2 - Phase Contrast":
        render_quiz("Quiz: Phase Contrast", questions_phase, key_prefix="phase")
        prefixes = ("phase_",)
    elif quiz_choice == "Quiz Day 3 - Molecular Modelling":
        render_quiz("Quiz: Molecular Modelling", questions_modelling, key_prefix="model")
        prefixes = ("model_",)
    else:
        render_quiz("Quiz: CryoEM - Day 1", questions_cryoEM, key_prefix="cryoEM")
        prefixes = ("cryoEM_",)

    # ----------------------
    # Reset
    # ----------------------
    if st.sidebar.button("Reset answers"):
        for k in list(st.session_state.keys()):
            if k.startswith(prefixes):
                del st.session_state[k]
        st.rerun()


if __name__ == "__main__":
    phase_quiz()
