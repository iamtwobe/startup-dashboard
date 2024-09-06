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
                    var usd_state_img = "assets/icons/increase_icon.png"
                    break;
                case "decrease":
                    var usd_state_img = "assets/icons/decrease_icon.png"
                    break;
                case "stable":
                    var usd_state_img = "assets/icons/decrease_icon.png"
                    break;
            }
            switch(parsedData.euro_state){
                case "increase":
                    var eur_state_img = "assets/icons/increase_icon.png"
                    break;
                case "decrease":
                    var eur_state_img = "assets/icons/decrease_icon.png"
                    break;
                case "stable":
                    var eur_state_img = "assets/icons/decrease_icon.png"
                    break;
            }
            document.getElementById('weather').textContent = parsedData.weather || "N/A";
            document.getElementById('weather_img').src = parsedData.weather_img;
            document.getElementById('temperature').textContent = parsedData.temperature || "N/A";
            document.getElementById('date').textContent = parsedData.date || "N/A";
            document.getElementById('dollar').innerHTML = `<p id="dollar" class="card-text">R$ ${parsedData.dollar_rate || "N/A"}</p>`
            document.getElementById('usd_title').innerHTML = `<h5 id="usd_title" class="card-title"> Dollar </h5><img src="${usd_state_img}" height="56" width="60">`
            document.getElementById('euro').innerHTML = `<p id="euro" class="card-text">R$ ${parsedData.euro_rate || "N/A"}</p>`;
            document.getElementById('euro_title').innerHTML = `<h5 id="euro_title" class="card-title"> Euro </h5><img src="${eur_state_img}" height="56" width="60">`
        })
}