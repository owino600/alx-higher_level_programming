// Add an <li> element with the text "Item" to UL.my_list when the user clicks on DIV#add_item
$("#add_item").click(function() {
    const newItem = $("<li>").text("Item");
    $("UL.my_list").append(newItem);
  });  