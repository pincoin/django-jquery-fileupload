// Acquiring the token when CSRF_USE_SESSIONS is False
var csrftoken = getCookie('csrftoken');

// Acquiring the token when CSRF_USE_SESSIONS is True
// var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

$(function () {
    $('#id_files').fileupload({
        // A string containing the URL to which the request is sent. (URL pointing Django view)
        url: '/upload',

        // The type of data that is expected back from the server. (default: 'json')
        dataType: 'json',

        // By default, each file of a selection is uploaded using an individual request for XHR type uploads.
        // Set this option to false to upload file selections in one request each. (default: true)
        singleFileUploads: false,

        // Callback for setting the token on the AJAX request
        beforeSend: function (xhr, data) {
            if (!csrfSafeMethod(data.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },

        // Callback for the start of each file upload request.
        // If this callback returns false, the file upload request is aborted.
        send: function (e, data) {
            return data.files.length < 10;
        },

        // Callback for successful upload requests.
        done: function (e, data) {
            $.each(data.result.files, function (index, file) {
                $("#files ul").append('<li>' + file.pk + ': <a href="' + file.url + '">' + file.name + '</a></li>');
            });
        },

        // Callback for failed (abort or error) upload requests.
        fail: function (e, data) {
        }
    });
});