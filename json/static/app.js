// 

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('question-form');
    const resultContainer = document.getElementById('result-container');
    const predictionResult = document.getElementById('prediction-result');

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        // Send the form data to the Flask app using fetch API
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.text())
        .then(result => {
            // Display the prediction result
            resultContainer.style.display = 'block';
            predictionResult.textContent = `The prediction result is: ${result}`;
        })
        .catch(error => console.error('Error:', error));
    });
});
