document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.chips');
  var instances = M.Chips.init(elems, options);
});

// Or with jQuery

$('.chips').chips();
$('.chips-initial').chips({
  data: [{
    tag: 'precondition',
  }, {
    tag: 'action',
  }, {
    tag: 'solution',
  }],
});
$('.chips-placeholder').chips({
  placeholder: 'Enter a tag',
  secondaryPlaceholder: '+Tag',
});
$('.chips-autocomplete').chips({
  autocompleteOptions: {
    data: {
      'precondition': null,
      'action': null,
      'solution': null,
      'other': null
    },
    limit: 1,
    minLength: 1
  }
});

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.autocomplete');
  var instances = M.Autocomplete.init(elems, options);
});


// Or with jQuery

$(document).ready(function(){
  $('input.autocomplete').autocomplete({
    data: {
      "precondition": null,
      "solution": null,
      "action": null,
      'other': null
    },
  });
});