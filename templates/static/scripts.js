function initialize_dashboard() {

    // URL do arquivo JSON
    const jsonUrl = 'data/data.json'; // Atualize o caminho conforme necessário

    // Fazer uma requisição para obter os dados JSON
    fetch(jsonUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(parsedData => {
            switch(parsedData.dollar_state){
                case "increase":
                    var dollar_state_img = ""
                    break;
                case "decrease":
                    var dollar_state_img = ""
                    break;
                case "stable":
                    var dollar_state_img = ""
                    break;
            }
            switch(parsedData.euro_state){
                case "increase":
                    var eur_state_img = ""
                    break;
                case "decrease":
                    var eur_state_img = ""
                    break;
                case "stable":
                    var eur_state_img = ""
                    break;
            }
            document.getElementById('dollar').innerHTML = `<p id="dollar" class="card-text">${parsedData.dollar_rate || "N/A"} <img src="${dollar_state_img}" alt=""></p>`
            document.getElementById('weather').textContent = parsedData.weather || "N/A";
            document.getElementById('weather_img').src = parsedData.weather_img;
            document.getElementById('temperature').textContent = parsedData.temperature || "N/A";
            document.getElementById('date').textContent = parsedData.date || "N/A";
            document.getElementById('euro').innerHTML = `<p id="euro" class="card-text">${parsedData.euro_rate || "N/A"} <img src="${eur_state_img}" alt=""></p>`;
        })
}