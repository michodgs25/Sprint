 //navigation function 
  $(document).ready(function(){
    $('.collapsible').collapsible();
  });

  //create sprint form function
    $(document).ready(function() {
    M.updateTextFields();
  });
  
  //jQuery method for select boxes, not longer a dependency, applied custom javascript
    document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
  });

   var instance = M.FormSelect.getInstance(elem);

   // trigger an autoresize for textarea 1& 2
    $('#textarea1', '#textarea2').val('New Text');
  M.textareaAutoResize($('#textarea1', '#textarea2'));

   //call slider
   $( "slider" ).slider();
   
   //Initialize the slider with the slide callback 
   $( ".selector" ).slider({
  start: function( event, ui ) {}
});
//Bind an event listener to the slidestart event
$( ".selector" ).on( "slidestart", function( event, ui ) {} );

//Initialize the slider with the stop callback
$( ".selector" ).slider({
  stop: function( event, ui ) {}
});

//Bind an event listener to the slidestop event
$( ".selector" ).on( "slidestop", function( event, ui ) {} );

//call date-picker
  $(document).ready(function(){
    $('.datepicker').datepicker();
  });