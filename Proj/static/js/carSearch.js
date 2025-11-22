// used on the cars page. Updates car search results
function searchAndUpdateCars(){
    const searchBar = document.getElementById("search-input");
    const query = searchBar.value;
    const resultsContainer = document.getElementById("results-container");
    const locationId = document.getElementById('current-location-id').value;

    // uses search_cars() in app.py
    const url = `/search_cars?q=${encodeURIComponent(query)}&location_id=${locationId}`;
    
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text(); 
        })
        .then(html => {
            resultsContainer.innerHTML = html;
        })
        .catch(error => {
            console.error('problem', error);
            resultsContainer.innerHTML = '<p class="text-danger mt-4">Could not load results</p>';
        });
}