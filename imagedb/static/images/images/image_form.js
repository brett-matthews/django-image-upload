$(function() {

    $( "#frmFileUpload" ).submit(function( event ) {

        $('#btnFormSubmit').attr('disabled', true);
        $('#spanFormSubmit').removeClass('d-none');

    });

});