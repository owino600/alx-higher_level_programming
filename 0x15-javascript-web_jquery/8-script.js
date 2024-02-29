// Fetch movie titles from the given URL using jQuery
$.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
  const movieTitles = data.results.map(movie => movie.title);
  const listElement = $("<ul>").attr("id", "list_movies");
  
  movieTitles.forEach(title => {
    const listItem = $("<li>").text(title);
    listElement.append(listItem);
  });
  
  $("body").append(listElement);
});