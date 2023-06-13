const APP_VERSION = "1.0"

// namespace
const app = { };

app.version = () => APP_VERSION;

app.post = (target, numbers) => {
    console.log("post the target/numbers", target, numbers);
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

// define the components
const submitButton = document.querySelector('#submit-button');
const targetInput = document.querySelector('#targetInput');
const numbersInput = document.querySelector('#numbersInput');

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

