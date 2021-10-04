import request from './tools.js';

const AUTH_FORM_CLASS = ".auth-form"

function onAuthError(response) {
    var message = "";
    for(var key in response) {
        if(response.hasOwnProperty(key)) {
            var value = response[key];
            message += value + "\n";
        }
    }
    window.alert(message);
}

async function onUserAuth(event) {
    event.preventDefault();
    var data = new FormData(event.target);
    var response = await request("post", window.location.href, data);
    var responseData = await response.json();
    if (response.ok) {
        window.location.href = responseData["redirect"];
        return;
    }
    onAuthError(responseData);
}

var authForm = document.querySelector(AUTH_FORM_CLASS)
authForm.addEventListener("submit", function(event) {
    onUserAuth(event);
});
