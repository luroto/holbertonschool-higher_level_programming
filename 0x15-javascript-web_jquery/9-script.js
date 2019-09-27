const url = "https://fourtonfish.com/hellosalut/?lang=fr";
$.getJSON(url, function(data) {
  $("DIV#hello").append(data.hello);
})
