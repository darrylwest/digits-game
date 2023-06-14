#!/usr/bin/env node --no-warnings

//
// ping with node
//

'use strict';
const postData = async () => {
  try {
    const data = {
      name: 'John Doe',
      email: 'johndoe@example.com'
    };

    const response = await fetch('http://piedmont:9890');

    const result = await response.json();

    console.log(result);
  } catch (error) {
    console.error('Error:', error);
  }
};

postData();

