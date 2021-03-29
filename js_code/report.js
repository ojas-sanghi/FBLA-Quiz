document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems);
});


function showHide(id1, id2) {
    console.log('show hide being called');

    var x = document.getElementById(id1);
    var button = document.getElementById(id2);

    if (x.style.visibility === 'hidden') {
        x.style.visibility = 'visible';
        button.innerText = 'Hide';
    } else {
        x.style.visibility = 'hidden';
        button.innerText = 'Show';
    }
}

function printingMode() {
    console.log('pritbintg mode being called');

    var self = document.getElementById('printingMode');
    var hiding = false;

    if (self.textContent === 'Enable printing mode') {
        hiding = true;
        self.textContent = 'Disable printing mode';
    } else {
        hiding = false;
        self.textContent = 'Enable printing mode';
    }

    for (let i = 1; i < 7; i++) {
        var user = document.getElementById('userAnsButton' + i);
        var correct = document.getElementById('correctAnsButton' + i);
        var result = document.getElementById('resultButton' + i);
        if (hiding) {
            console.log('hiding');
            // user.classList.add("hide")
            // correct.classList.add("hide")
            // result.classList.add("hide")
            user.style.display = 'none';
            correct.style.display = 'none';
            result.style.display = 'none';
        } else {
            console.log('showing');
            self.textContent = 'Enable printing mode';
            // user.classList.remove("hide")
            // correct.classList.remove("hide")
            // result.classList.remove("hide")
            user.style.display = 'block';
            correct.style.display = 'block';
            result.style.display = 'block';
        }

    }
}
