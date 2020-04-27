function LoadImageModal(trigger){

    trigger.attr('disabled', true);

    $.ajax({
        url: 'download/',
        type : 'GET'
    })
    .done(function(d) {
        $('#downloadModal .modal-content').html(d);
        $('#downloadModal').modal('show');
    })
    .always(function(d) {
        trigger.attr('disabled', false);
    });

}

$(function() {

    $('#btnDownload').click(function() {
      LoadImageModal($(this));
    });

});
