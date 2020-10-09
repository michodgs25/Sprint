$(document).ready(function(){
    //Automatically initialize all materialize components
    M.AutoInit();
    
    //call side-nav, for mobile& tablet
    $('.sidenav').sidenav();

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

    //call datepicker, user can select date
    $('.datepicker').datepicker({
        format: "dd, mmmm yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});

//Hide search bar when on create page
document.addEventListener('DOMContentLoaded', (event) => {
  if (window.location.pathname == '/activity/add') {
    document.querySelector('.search-form').style.display = "none";
  } else {
    document.querySelector('.search-form').style.display = "block";
  }
});

//Hide search bar on create page mobile screen
document.addEventListener('DOMContentLoaded', (event) => {
  if (window.location.pathname == '/activity/add') {
    document.querySelector('.side-form').style.display = "none";
  } else {
    document.querySelector('.side-form').style.display = "block";
  }
});