$(function () {
    $('#fileupload').fileupload({
        // A string containing the URL to which the request is sent. (URL pointing Django view)
        url: 'upload',

        // The type of data that is expected back from the server. (default: 'json')
        dataType: 'json',

        // By default, each file of a selection is uploaded using an individual request for XHR type uploads.
        // Set this option to false to upload file selections in one request each. (default: true)
        singleFileUploads: false,

        // Callback for the start of each file upload request.
        // If this callback returns false, the file upload request is aborted.
        send: function (e, data) {
            return data.files.length < 10;
        },

        // Callback for successful upload requests.
        done: function (e, data) {
            $.each(data.result.files, function (index, file) {
                console.log(data);
                $("#files ul").append('<li>' + file.pk + ': <a href="' + file.url + '">' + file.name + '</a></li>');
            });
        },

        // Callback for failed (abort or error) upload requests.
        fail: function (e, data) {
            console.log(data);
        }
    });
});