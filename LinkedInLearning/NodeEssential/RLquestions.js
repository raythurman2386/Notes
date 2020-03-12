const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const questions = [
  "What is your name? ",
  "Where do you live? ",
  "Whatcha doing with Node? "
]

const collectAnswers = (questions, done) => {
  const answers = []
  const [firstQuestion] = questions

  const questionAnswered = answer => {
    answers.push(answer)
    answers.length < questions.length 
      ? rl.question(questions[answers.length], questionAnswered ) 
      : done(answers)
  }

  rl.question(firstQuestion, questionAnswered)
}

collectAnswers(questions, answers => {
  console.log("Thank you for your answers.")
  console.log(answers)
  process.exit()
})