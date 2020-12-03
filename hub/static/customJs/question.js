function Question(text, choices, answer, scoreque) {
    this.text = text;
    this.choices = choices;
    this.answer = answer;
    this.scoreque = scoreque;
};

Question.prototype.isCorrectAnswer = function(choice) {
    return this.answer === choice;
}