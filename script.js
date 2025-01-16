const questions = [
  {
    category: "Cryo-SPA",
    question: "1. What does 'SPA' in cryo-SPA stand for?",
    options: [
      "Single Particle Analysis",
      "Special Particle Alignment",
      "Structured Phase Alignment",
      "Single Protein Analysis"
    ],
    correct: "Single Particle Analysis"
  },
  {
    category: "Cryo-SPA",
    question: "2. What is the primary purpose of cryo-SPA?",
    options: [
      "Studying small molecules",
      "Determining 3D structures of individual particles",
      "Analyzing large crystals",
      "Observing live cells"
    ],
    correct: "Determining 3D structures of individual particles"
  },
  {
    category: "Cryo-TOMO",
    question: "3. What is cryo-TOMO used for?",
    options: [
      "2D imaging of proteins",
      "3D imaging of cellular environments",
      "Measuring diffraction patterns",
      "Heating samples for imaging"
    ],
    correct: "3D imaging of cellular environments"
  },
  {
    category: "Cryo-TOMO",
    question: "4. Why is thinning a sample important in cryo-TOMO?",
    options: [
      "To improve beam alignment",
      "To ensure electrons can pass through for imaging",
      "To enhance vitrification",
      "To prevent thermal damage"
    ],
    correct: "To ensure electrons can pass through for imaging"
  }
];

function updateProgress(current, total) {
  const progressBar = document.getElementById("progressBar");
  const progress = (current / total) * 100;
  progressBar.style.width = `${progress}%`;
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

  // Update progress to 100% after submission
  updateProgress(questions.length, questions.length);
}

function loadQuiz() {
  const form = document.getElementById("quizForm");

  let currentCategory = ""; // Track the current category
  questions.forEach((q, index) => {
    if (q.category && q.category !== currentCategory) {
      // Add category heading
      const categoryHeading = document.createElement("h2");
      categoryHeading.textContent = q.category;
      categoryHeading.style.color = "#007BFF";
      form.appendChild(categoryHeading);

      currentCategory = q.category; // Update current category
    }

    const questionDiv = document.createElement("div");
    questionDiv.classList.add("question");

    // Add question text
    const questionText = document.createElement("p");
    questionText.innerHTML = `<strong>${q.question}</strong>`;
    questionDiv.appendChild(questionText);

    // Add options
    q.options.forEach((option) => {
      const label = document.createElement("label");
      label.innerHTML = `<input type="radio" name="q${index}" value="${option}" onchange="updateProgressOnAnswer()"> ${option}`;
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

function updateProgressOnAnswer() {
  const answered = document.querySelectorAll('input[type="radio"]:checked').length;
  updateProgress(answered, questions.length);
}

// Load quiz questions on page load
window.onload = loadQuiz;



