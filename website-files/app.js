// Get the form element
const form = document.querySelector('form');

// Add an event listener to the form's submit event
form.addEventListener('submit', (event) => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the input elements
  const inputs = form.elements;

  // Create an object to store the input values
  const values = {};

  // Loop through each input element
  for (let i = 0; i < inputs.length; i++) {
    const input = inputs[i];

    // If the input element has a name attribute, add its value to the values object
    if (input.name) {
      values[input.name] = input.value;
    }
  }

  // Display the values under the form
  //const output = document.createElement('div');
  //output.innerHTML = JSON.stringify(values, null, 2);
  //form.parentNode.appendChild(output);
  fetch('https://ee8603-red-wine-project-501219860.onrender.com/predict', {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(values, null, 2)
})
.then(response => response.json())
.then(data => {
    const final_output = document.createElement('div');
    final_output.id = "wine-quality";
    const x = data.quality;
    final_output.textContent = `The quality of redwine is: ${x}`;
    form.parentNode.appendChild(final_output);
})
.catch(error => console.error(error));
});