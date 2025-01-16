function submitQuiz() {
  const answers = {
    q1: "b",
    q2: "c"
  };
  
  let score = 0;
  let totalQuestions = Object.keys(answers).length;

  for (let question in answers) {
    const selected = document.querySelector(`input[name="${question}"]:checked`);
    if (selected && selected.value === answers[question]) {
      score++;
    }
  }

  const result = document.getElementById('result');
  result.textContent = `You scored ${score} out of ${totalQuestions}!`;
}
