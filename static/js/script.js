$(document).ready(function(){
    //Automatically initialize all materialize components
    M.AutoInit();
    
    //call side-nav
    $('.sidenav').sidenav();

    /*tool tip, inform user to use search bar 
    to help find specific sprints*/
    $('.tooltipped').tooltip();

    //trigger feature discovery on explore page
    $('.tap-target').tapTarget();

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
    $('.datepicker').datepicker({
        format: "dd, mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});

//alert box, asks user whether they want to delete post
function myFunction() {
  alert("I am an alert box!");