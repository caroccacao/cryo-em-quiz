function submitQuiz() {
  const answers = {
    q1: "b",
    q2: "c"
  };

  let totalQuestions = Object.keys(answers).length;
  let correctCount = 0;

  // Iterate through the answers
  for (let question in answers) {
    const selected = document.querySelector(`input[name="${question}"]:checked`);
    const feedbackElement = document.getElementById(`${question}-feedback`);

    if (selected) {
      if (selected.value === answers[question]) {
        correctCount++;
        feedbackElement.textContent = "Correct!";
        feedbackElement.style.color = "green";
      } else {
        feedbackElement.textContent = `Incorrect! The correct answer is: ${answers[question]}`;
        feedbackElement.style.color = "red";
      }
    } else {
      feedbackElement.textContent = "You did not select an answer.";
      feedbackElement.style.color = "orange";
    }
  }

  // Display final score
  const result = document.getElementById("result");
  result.textContent = `You scored ${correctCount} out of ${totalQuestions}!`;
}

