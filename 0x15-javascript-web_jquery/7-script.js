// Fetch the character name from the given URL using jQuery
$.getJSON("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
  const characterName = data.name;
  $("#character").text(characterName);
});