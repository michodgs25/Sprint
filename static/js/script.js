 //call document function
  $(document).ready(function(){
    //collapsible navigation
    $('.collapsible').collapsible();

    // trigger an autoresize for textarea 1& 2
    $('#textarea1', '#textarea2').val('New Text');
    M.textareaAutoResize($('#textarea1', '#textarea2'));
    
    //create sprint text form function
    M.updateTextFields();
    
    //call slider
    $( "slider" ).slider();
    
    //call datepicker
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
  });
  
  //jQuery method for select boxes no longer a materialize library dependency, applied custom javascript
    document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
  });

   var instance = M.FormSelect.getInstance(elem);

   document.getElementById("matfix").addEventListener("click", function(e) {
	e.stopPropagation();
});