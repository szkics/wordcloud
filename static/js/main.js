function generateWordCloud() {
    var text = document.getElementById('inputText').value;

    fetch('/generate_wordcloud', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'text=' + encodeURIComponent(text),
    })
    .then(response => response.json())
    .then(data => {
        var wordCloudContainer = document.getElementById('wordCloudContainer');
        wordCloudContainer.innerHTML = '<img src="data:image/png;base64,' + data.image + '" alt="Word Cloud">';
    })
    .catch(error => console.error('Error:', error));
}
