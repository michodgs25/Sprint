 //call document function
  $(document).ready(function(){
    //collapsible navigation
    $('.collapsible').collapsible();

    //nav follows user scroll
    $('body').scrollspy({ target: '#navbar-scrollspy' })

    // trigger an autoresize for textarea 1& 2
if ($('#textarea1').length > 0) {
    $('#textarea1').val('New Text');
    M.textareaAutoResize($('#textarea1'));
}

if ($('#textarea2').length > 0) {
    $('#textarea2').val('New Text');
    M.textareaAutoResize($('#textarea2'));
}
    
    //create sprint text form function
    M.updateTextFields();
    
    //call slider
    $( "slider" ).slider();

    //call form select
    $('select').formSelect();
    
    //call datepicker
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
      //jQuery method for select boxes no longer a materialize library dependency, applied custom javascript
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});

   var instance = M.FormSelect.getInstance(elems);

   if (document.getElementById("matfix")!== null) {
   document.getElementById("matfix").addEventListener("click", function(e) {
    e.stopPropagation();
});}
  });

