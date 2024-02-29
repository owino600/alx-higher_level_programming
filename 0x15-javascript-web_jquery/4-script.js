// Toggle the class of the <header> element between red and green
$("#toggle_header").click(function() {
    const headerElement = $("header");
    if (headerElement.hasClass("red")) {
      headerElement.removeClass("red").addClass("green");
    } else {
      headerElement.removeClass("green").addClass("red");
    }
  });  