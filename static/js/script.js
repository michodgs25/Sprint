$(document).ready(function(){
    //Trigger accordian collapse
    $('.collapsible').collapsible();
    
    //trigger an autoresize for textarea 1& 2
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
            
    //Trigger select box options
    $('select').formSelect();
            
    //call datepicker
    $('.datepicker').datepicker();
});