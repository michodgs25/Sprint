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
  });
  
  //jQuery method for select boxes no longer a materialize library dependency, applied custom javascript
    document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
  });

   var instance = M.FormSelect.getInstance(elem);

    
   
   // create instance of datepicker
   var instance = M.Datepicker.getInstance(elem);
       //call date-picker
    $('.datepicker').datepicker(format,'mmm dd, yyyy');
    
    // open date picker
    instance.open(defaultDate, 'null');
    
    //close date picker
    instance.close();
    
    //get date instance
    instance.toString();
    
    //destroy date
    instance.destroy();
    
    //get instance of string date
    instance.toString();
    
    //set new date
    instance.setDate(new Date());
    
    //Date to show on the datepicker
    instance.gotoDate(new Date());