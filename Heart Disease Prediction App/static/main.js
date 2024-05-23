// Get the select element
var select = document.querySelector('select[name="AgeCategory"]');

// Listen for changes
select.addEventListener('change', function() {
  // Create an object to hold the one-hot encoding
  var oneHot = {};

  // Loop through each option
  for (var i = 0; i < select.options.length; i++) {
    var option = select.options[i];

    // If the option is selected, set its value in the object to 1, otherwise 0
    oneHot[option.value] = option.selected ? 1 : 0;
  }

  // Now `oneHot` is an object with a one-hot encoding of the select options
  console.log(oneHot);
});