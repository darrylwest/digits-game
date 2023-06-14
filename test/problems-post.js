//
// this is similar to what is on the client page
//

const postData = async () => {
  try {
    const data = {
      target: 414,
      numbers: [3,4,11,17,21,24],
    };

    const response = await fetch('http://piedmont:9890/problems', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();
    console.log(result);
  } catch (error) {
    console.error('Error:', error);
  }
};

postData();

