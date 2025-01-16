const questions = [
  {
    question: "1. What does 'SPA' in cryo-SPA stand for?",
    options: ["Single Particle Analysis", "Special Particle Alignment", "Structured Phase Alignment", "Single Protein Analysis"],
    correct: "Single Particle Analysis"
  },
  {
    question: "2. What is the primary purpose of cryo-SPA?",
    options: ["Studying small molecules", "Determining 3D structures of individual particles", "Analyzing large crystals", "Observing live cells"],
    correct: "Determining 3D structures of individual particles"
  },
  {
    question: "3. What is cryo-TOMO used for?",
    options: ["2D imaging of proteins", "3D imaging of cellular environments", "Measuring diffraction patterns", "Heating samples for imaging"],
    correct: "3D imaging of cellular environments"
  },
  {
    question: "4. What is the typical resolution of cryo-SPA structures?",
    options: ["1 µm", "3-5 Å", "100 nm", "10 nm"],
    correct: "3-5 Å"
  },
  {
    question: "5. What does the tilt series in cryo-TOMO help achieve?",
    options: ["High contrast", "Increased magnification", "3D reconstruction", "Faster imaging"],
    correct: "3D reconstruction"
  },
  // Add 10 more questions here
];

function loadQuiz() {
  const form = document.getElementById("quizForm");

  questions.forEach((q, index) => {
    const questionDiv = document.createElement("div");
    questionDiv.classList.add("question");

    // Add question text
    const questionText = document.createElement("p");
    questionText.innerHTML = `<strong>${q.question}</strong>`;
    questionDiv.appendChild(questionText);

    // Add options
    q.options.forEach((option, i) => {
      const label = document.createElement("label");
      label.innerHTML = `<input type="radio" name="q${index}" value="${option}"> ${option}`;
      questionDiv.appendChild(label);
    });

    // Add feedback placeholder
    const feedback = document.createElement("p");
    feedback.classList.add("feedback");
    feedback.id = `q${index}-feedback`;
    questionDiv.appendChild(feedback);

    form.appendChild(questionDiv);
  });
}

function submitQuiz() {
  let correctCount = 0;

  questions.forEach((q, index) => {
    const selected = document.querySelector(`input[name="q${index}"]:checked`);
    const feedback = document.getElementById(`q${index}-feedback`);

    if (selected) {
      if (selected.value === q.correct) {
        correctCount++;
        feedback.textContent = "Correct!";
        feedback.style.color = "green";
      } else {
        feedback.textContent = `Incorrect! The correct answer is: ${q.correct}`;
        feedback.style.color = "red";
      }
    } else {
      feedback.textContent = "You did not select an answer.";
      feedback.style.color = "orange";
    }
  });

  // Display final score
  const result = document.getElementById("result");
  result.textContent = `You scored ${correctCount} out of ${questions.length}!`;
}

// Load quiz questions on page load
window.onload = loadQuiz;


