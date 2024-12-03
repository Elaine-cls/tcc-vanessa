import {removeToken} from "./api-utils.js";

export function redirectTo(url, time = 0) {
    setTimeout(() => {
        window.location = url
    }, time)
}

export function showAlert(message, type, placeholder){
    placeholder.innerHTML = "";
    var wrapper = document.createElement('div');
    wrapper.innerHTML = '<div class="alert alert-' + type + ' alert-dismissible" role="alert">' + message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';

    placeholder.append(wrapper)
}

export function logout(button){
    button.addEventListener("click", () => {
        removeToken();
        redirectTo(window.location);
    })
}

export function capturarUUID(){
    const pathname = window.location.pathname;

    // Define uma expressão regular para capturar o UUID
    const uuidRegex = /[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/;

    // Executa a regex no caminho
    const match = pathname.match(uuidRegex);

    if (match !== null) {
        return match[0]
    }

    return false;
}

export function formatarData(value){
    return value
}

