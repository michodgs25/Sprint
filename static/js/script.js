 //navigation function 
  $(document).ready(function(){
    $('.collapsible').collapsible();
  });

  //create sprint form function
    $(document).ready(function() {
    M.updateTextFields();
  });
  
  //jQuery method for select box, not longer a dependency, applied custom javascript
    document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
  });

   var instance = M.FormSelect.getInstance(elem);

   //slider jquery
   $( "#slider" ).slider();
 