$(document).ready(function(){
    //Automatically initialize all materialize components
    M.AutoInit();
    
    //call side-nav, in mobile
    $('.sidenav').sidenav();

    //trigger feature discovery on explore page
    $('.tap-target').tapTarget();

    //Trigger accordian collapse
    $('.collapsible').collapsible();

    //sidenav select and collapse functions
    $('select').material_select();
    $(".button-collapse").sideNav();
    
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

    //dialog box, asks user whether they want to delete post
    $( "#dialog-message" ).dialog({
      modal: true,
      buttons: {
        Ok: function() {
          $( this ).dialog( "close" );
        }
      }
    });

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

document.addEventListener('DOMContentLoaded', (event) => {
  if (window.location.pathname == '/get_home') {
    document.querySelector('.navbar-fixed').style.display = "none";
  } else {
    document.querySelector('.navbar-fixed').style.display = "block";
  }
});

document.addEventListener('DOMContentLoaded', (event) => {
  if (window.location.pathname == '/get_home') {
    document.querySelector('.page-footer').style.display = "none";
  } else {
    document.querySelector('.page-footer').style.display = "block";
  }
});