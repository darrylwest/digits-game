const APP_VERSION = "0.2.7"

// define the components
const submitButton = document.querySelector('#submit-button');
const targetInput = document.querySelector('#targetInput');
const numbersInput = document.querySelector('#numbersInput');
const resultOutput = document.querySelector('#resultOutput');
const footerMessage = document.querySelector('#footerMessage');

targetInput.value = "271";
numbersInput.value = "3 4 6 7 8 11";

// application namespace
const app = { };

app.version = () => APP_VERSION;

async function ping() {
    console.log("ping the app server");

    const response = await fetch('http://127.0.0.1:9890/');
    console.log(response);
    const jdata = await response.json();
    console.log(jdata);
}

app.solve = (data = {}) => {
    url = 'http://127.0.0.1:9890/problems';
    console.log(url, data);

    fetch(url, {
      method: "POST",
      mode: "cors",
      cache: "no-cache",
      credentials: "omit",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
        submitButton.disabled = false;
        submitButton.value = "Solve"

        resultOutput.innerHTML = result.result;
    })
    .catch(error => {
        resultOutput.innerHTML = error;
        throw new Error(error)
    });
}

app.post = (target, numbers) => {
    console.log("post the target/numbers", target, numbers);

    data = { target, numbers };
    console.log("posting", data);

    app.solve(data);
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