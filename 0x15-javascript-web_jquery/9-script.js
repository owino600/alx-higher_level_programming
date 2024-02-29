// Fetch the translation of "hello" from the given URL using jQuery
$.getJSON("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
  const helloTranslation = data.hello;
  $("#hello").text(helloTranslation);
});