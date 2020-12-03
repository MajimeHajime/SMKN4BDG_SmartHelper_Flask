function populate() {
    if(quiz.isEnded()) {
        showScores();
    }
    else {
    // show question
        var element = document.getElementById("question");
        element.innerHTML = quiz.getQuestionIndex().text;

    // show options
        var choices = quiz.getQuestionIndex().choices;
        for(var i = 0; i < choices.length; i++) {
            var element = document.getElementById("choice" + i);
            element.innerHTML = choices[i];
            guess("btn" + i, choices[i]);
        }

        showProgress();
    }
};

function guess(id, guess) {
    var button = document.getElementById(id);
    button.onclick = function() {
        quiz.guess(guess);
        populate();
    }
};


function showProgress() {
    var currentQuestionNumber = quiz.questionIndex + 1;
    var element = document.getElementById("progress");
    element.innerHTML = "Pertanyaan " + currentQuestionNumber + " dari " + quiz.questions.length;
};

function showScores() {
    var gameOverHTML = "<h1>Result</h1>";
    gameOverHTML += "<h2 id='score'> Your scores: " + quiz.score + "</h2>";
    var element = document.getElementById("quiz");
    if(quiz.score <= 2){
        gameOverHTML += "<p id='checkResult' >Kesimpulan Anda kemungkinan besar tidak terinfeksi oleh COVID-19, Namun anda disarankan untuk tetap tinggal dirumah. Infeksi anda mungkin disebabkan virus selain COVID-19, Oleh karena itu anda tidak perlu dites oleh COVID-19. Meskipun demikian, hindarilah keluar rumah jika memungkinkan. Penyakit anda akan sembuh sendiri dengan cukup makan dan istirahat. Apabila anda mengalami gejala atau mendapatkan informasi baru tentang perjalanan penyakit anda, anda bisa membuka web ini lagi. <p>";
    } else if (quiz.score <= 5){
        gameOverHTML += "<p id='checkResult'> Sebagai tindakan pencegahan, siapa saja yang mengalami gejala (demam, batuk, bersin, sakit tenggorokan, atau sulit bernapas) untuk tinggal di rumah selama 14 hari untuk mencegah penyebaran. Anda disarankan untuk tidak keluar ke tempat publik, tinggal dirumah saja dan tidak boleh ada tamu. Di mohon anda jangan berangkat ke UGD, Rumah sakit, atau klinik, kecuali kalau gejala anda semakin buruk segera pergi ke dokter terdekat.</p>"
    } else if (quiz.score >= 6){
        gameOverHTML += "<p id='checkResult' >Gejala-gejala ini membutuhkan perhatian segera. Anda harus segera menelepon Rumah Sakit Terdekat, atau langsung pergi ke instalasi gawat darurat terdekat.</p>";
    }
    element.innerHTML = gameOverHTML;
};

// create questions
var questions = [
    new Question("1. Apakah Anda mengalami salah satu dari yang berikut: <br> -Kesulitan bernafas yang parah (Bernafas dengan sangat cepat atau berbicara dalam satu kata) <br> -Nyeri dada yang parah <br> -Sulit untuk bangun <br> -Merasa kebingungan <br> -Penurunan kesadaran", ["Ya", "Tidak"], "Ya", 6),
    new Question("2. Apakah Anda mengalami salah satu dari yang berikut: <br> -Nafas yang pendek saat istirahat <br> -Ketidakmampuan untuk berbaring karena kesulitan bernafas <br> -Kondisi kesehatan kronis yang anda alami dirasakan lebih berat karena kesulitan bernapas", ["Ya", "Tidak"], "Ya", 6),
    new Question("3. Apakah Anda mengalami salah satu dari yang berikut: <br> -Demam <br> -Batuk <br> -Bersin <br> -Sakit Tenggorokan <br> -Sulit Bernafas", ["Ya", "Tidak"], "Ya", 3),
    new Question("4. Apakah anda pernah muncul gejala sekitar 14 hari setelah travelling ke luar negeri? (China, Italy, Iran, Korea Selatan, Prancis, Spanyol, Jerman, USA) atau ke kota terjangkit (Jakarta, Bali, Solo, Yogyakarta, Pontianak, Manado, Bandung dll)?", ["Ya", "Tidak"], "Ya", 1),
    new Question("5. Apakah Anda memberikan perawatan atau melakukan kontak dekat dengan seseorang dengan COVID-19 (kemungkinan atau dikonfirmasi) saat mereka sakit (batuk, demam, bersin, atau sakit tenggorokan)?", ["Ya", "Tidak"], "Ya", 1),
    new Question("6. Apakah Anda memiliki kontak dekat dengan seseorang yang bepergian ke luar Negeri dalam 14 hari terakhir yang menjadi sakit (batuk, demam, bersin, atau sakit tenggorokan)?", ["Ya", "Tidak"], "Ya", 1)
];

// create quiz
var quiz = new Quiz(questions);

// display quiz
populate();