$(document).ready(function(){
    //Automatically initialize all materialize components
    M.AutoInit();
    
    //call side-nav, in mobile
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
        format: "dd, mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});

//check nav elements, hide search bar element if on create page
// and hide navigation bar and footer if on homepage
document.addEventListener('DOMContentLoaded', (event) => {
  //the event occurred
})