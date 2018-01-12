$(document).ready(function () {
    var $sn = $('#id_body');

    $sn.summernote({
        placeholder: 'Please, type your message',
        tabsize: 2,
        height: 300,
        callbacks: {
            onInit: function () {
                $nEditor = $sn.next();
                $nImageInput = $nEditor.find('.note-image-input');
            },
            onImageUpload: function (files) {
                $nImageInput.fileupload();
                var jqXHR = $nImageInput.fileupload('send', {
                    url: '/upload',
                    files: files
                }).done(function (data, textStatus, jqXHR) {
                    $.each(data.files, function (index, file) {
                        $sn.summernote('insertImage', file.url);

                        $("#files ul").append('<li>' + file.pk + ': <a href="' + file.url + '">' + file.name + '</a></li>');

                        $("<input>", {
                            type: "hidden",
                            name: "attachments",
                            value: file.pk
                        }).appendTo("form");
                    });
                }).fail(function (jqXHR, textStatus, errorThrown) {
                    console.log('Failed to upload');
                });
            }
        }
    })
});