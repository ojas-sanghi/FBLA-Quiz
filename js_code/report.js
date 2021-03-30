document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems);
});

function showText(textId, buttonId) {
    var text = document.getElementById(textId);
    var button = document.getElementById(buttonId);

    text.style.visibility = 'visible';
    button.innerText = 'Hide';
}

function hideText(textId, buttonId) {
    var text = document.getElementById(textId);
    var button = document.getElementById(buttonId);

    text.style.visibility = 'hidden';
    button.innerText = 'Show';
}

function showHide(textId, buttonId) {
    var text = document.getElementById(textId);

    if (text.style.visibility === 'hidden') {
        showText(textId, buttonId);
    } else {
        hideText(textId, buttonId);
    }
}

function printingMode() {
    console.log('pritbintg mode being called');

    var self = document.getElementById('printingMode');
    var enabled = false;

    if (self.textContent === 'Enable printing mode') {
        enabled = true;
        self.textContent = 'Disable printing mode';
    } else {
        enabled = false;
        self.textContent = 'Enable printing mode';
    }

    for (let i = 1; i < 7; i++) {
        var userAnswerId = 'userAnswer' + i
        var correctAnswerId = 'correctAnswer' + i
        var resultAnswerId = 'resultText' + i

        var userButtonId = 'userAnsButton' + i
        var correctButtonId = 'correctAnsButton' + i
        var resultButtonId = 'resultButton' + i

        
        // Hide all the buttons
        var userButton = document.getElementById(userButtonId);
        var correctButton = document.getElementById(correctButtonId);
        var resultButton = document.getElementById(resultButtonId);
        
        var buttonCols = document.getElementsByName("buttonCol");
        var answerCols = document.getElementsByName("answerCol");
        if (enabled) {
            // Show all the answers
            showText(userAnswerId, userButtonId);
            showText(correctAnswerId, correctButtonId);
            showText(resultAnswerId, resultButtonId);

            for (var j = 0; j < buttonCols.length; j++) {
                buttonCols[j].classList.add('hide');
            }
            for (var k = 0; k < answerCols.length; k++) {
                console.log(answerCols[k].classList);
                answerCols[k].classList.remove('col');
                answerCols[k].classList.remove('s10');
                answerCols[k].classList.remove('pull-s5');
            }
            userButton.classList.add('hide');
            correctButton.classList.add('hide');
            resultButton.classList.add('hide');
        } else {
            self.textContent = 'Enable printing mode';

            // Hide all the answers
            hideText(userAnswerId, userButtonId);
            hideText(correctAnswerId, correctButtonId);
            hideText(resultAnswerId, resultButtonId);

            for (var j = 0; j < buttonCols.length; j++) {
                buttonCols[j].classList.remove('hide');
            }
            for (var k = 0; k < answerCols.length; k++) {
                answerCols[k].classList.add('col');
                answerCols[k].classList.add('s10');
                answerCols[k].classList.add('pull-s5');
            }
            userButton.classList.remove('hide')
            correctButton.classList.remove('hide')
            resultButton.classList.remove('hide')
        }

    }
}
