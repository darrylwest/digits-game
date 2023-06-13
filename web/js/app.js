const APP_VERSION = "0.1.2"

// define the components
const submitButton = document.querySelector('#submit-button');
const targetInput = document.querySelector('#targetInput');
const numbersInput = document.querySelector('#numbersInput');
const resultOutput = document.querySelector('#resultOutput');
const footerMessage = document.querySelector('#footerMessage');


// application namespace
const app = { };

app.version = () => APP_VERSION;

app.post = (target, numbers) => {
    console.log("post the target/numbers", target, numbers);

    setTimeout(() => {
        console.log("posting")
        resultOutput.innerHTML = "Result: 5*3+16*3";
        submitButton.disabled = false;
        submitButton.value = "Solve"
    }, 1000);
};

app.parse_target = (value) => {
    let target = Number(value);

    console.log('target', target);
    // validate

    return target;
};

app.parse_numbers = (value) => {
    let numbers = value.split(' ').map(v => Number(v));

    console.log('numbers', numbers);

    return numbers;
};

submitButton.addEventListener('click', () => {
    console.log("submit button click");
    submitButton.disabled = true;
    submitButton.value = "Working..."
    // now fire the fetch/post and retrieve the rusults
    let target = app.parse_target(targetInput.value);
    let numbers = app.parse_numbers(numbersInput.value);

    if (target && numbers.length == 6) {
        app.post(target, numbers);
    } else {
        // show the error popup...
        console.log("validation error");
        submitButton.disabled = false;
        submitButton.value = "Solve"
    }

});

footerMessage.innerHTML = "Copyright (c) 2023, Version: " + APP_VERSION;