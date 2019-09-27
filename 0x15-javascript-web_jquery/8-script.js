const url = 'https://swapi.co/api/films/?format=json';
$.getJSON(url, function (data) {
  $(data.results).each(function (index, result) {
    $('UL#list_movies').append('<li>' + result.title + '</li>');
  });
});
