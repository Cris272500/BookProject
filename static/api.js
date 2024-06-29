

export const fetchBooks = async (query) => {
    try {
        const response = await fetch('/api', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: query })
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("El error fue: " +error);
    }
};

document.addEventListener('DOMContentLoaded', () => {
    //alert("API");

    // guardamos el elemento formulario
    //const searchForm = document.getElementById("search-form");

    // capturamos el evento 'submit'
    document.getElementById("search-form").addEventListener('submit', async (event) => {
        // evitamos recargar la pagina
        event.preventDefault();

        // obtenemos el input, el div donde iran los resultados
        const query = document.getElementById("query").value;
        const resultsDiv = document.getElementById("results");

        // limpiar el anterior resultado
        resultsDiv.innerHTML = "";

        // obtener la informacion
        const data = await fetchBooks(query);

        // si devolvio algo
        if (data.items) {
            // foreach
            data.items.forEach(book => {
                // el titulo de cada libro
                const title = book.volumeInfo.title;
                resultsDiv.innerHTML += `<p>${title}</p>`
            });
        } else {
            resultsDiv.innerHTML = '<p>No se encontro</p>'
        }
    });
})