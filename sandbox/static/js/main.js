// Set a custom X-CSRFToken header to the value of the CSRF token on each XMLHttpRequest
// https://docs.djangoproject.com/en/2.0/ref/csrf/#acquiring-the-token-if-csrf-use-sessions-is-false
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(function () {
    $('#fileupload').fileupload({
        // A string containing the URL to which the request is sent. (URL pointing Django view)
        url: 'upload',

        // The type of data that is expected back from the server. (default: 'json')
        dataType: 'json',

        // By default, each file of a selection is uploaded using an individual request for XHR type uploads.
        // Set this option to false to upload file selections in one request each. (default: true)
        singleFileUploads: false,

        // Callback for modification of the jqXHR object before it is sent.
        // Use this to set custom headers, etc. The jqXHR and settings objects are passed as arguments.
        beforeSend: function (xhr, data) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },

        // Callback for the start of each file upload request.
        // If this callback returns false, the file upload request is aborted.
        send: function (e, data) {
            return data.files.length < 10;
        },

        // Callback for successful upload requests.
        done: function (e, data) {
            $.each(data.result.files, function (index, file) {
                console.log(data);
                $("#files ul").append('<li>' + file.name + '</li>');
            });
        },

        // Callback for failed (abort or error) upload requests.
        fail: function (e, data) {
            console.log(data);
        }
    });
});