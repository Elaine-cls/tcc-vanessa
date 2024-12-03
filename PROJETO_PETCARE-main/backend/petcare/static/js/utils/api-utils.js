import {getMessageOrDefault} from './tradutor.js';
import {redirectTo} from './site-utils.js';
import {variables, HTTP_STATUS, ROUTES_SITE, ROUTES_API} from './global.js';

export async function makePostRequest(url, headers = {}, formData = {}, responseCaseOk = (response) => {}, responseCaseError = (response) => {}, responseCaseErrorCatch = () => {}){
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            ...headers
            },
            body: JSON.stringify(formData)
        });
        if (response.ok) {
            return responseCaseOk(response);
        } else {
            return responseCaseError(response);
        }
    } catch (error) {
        console.error('Erro na requisição:', error);
        return responseCaseErrorCatch()
    }
}
export async function makeGetRequest(url, headers = {}, responseCaseOk = (response) => {}, responseCaseError = (response) => {}, responseCaseErrorCatch = () => {}) {
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
            'Content-Type': 'application/json',
            ...headers
            }
        });
        if (response.ok) {
            return responseCaseOk(response);
        } else {
            return responseCaseError(response);
        }
    } catch (error) {
        console.error('Erro na requisição:', error);
        return responseCaseErrorCatch()
    }
}

export const tratamentosDeErros = {
    accounts: {
        register : {
            tratarErroDeEmail : async(response, callback) => {
                const data = await response.json();
                if (data.email && data.email.length > 0) {
                    const message = data.email[0]; 
                    const messageTraduzida = getMessageOrDefault(message);
                    
                    callback(messageTraduzida.message);
    
                    if (messageTraduzida.id == 1 ) {
                        redirectTo(ROUTES_SITE.login, 3000);
                    }
                }
            }
        },
        unauthorized: (response, redirect = ROUTES_SITE.login) => {
            if(response.status == HTTP_STATUS.not_authorized) {
                redirectTo(redirect)
            }
        },
    },
    owner : {
        register : {
            already_registered: (response, callback = (message) => {}) => {
                if(response.status == HTTP_STATUS.not_acceptable){
                    callback("Usuário já está cadastrado. Você será redirecionado para a página de login.");
                    redirectTo(ROUTES_SITE.login, 3000);
                }
            },
            dont_have_register: (response) => {
                if(response.status == HTTP_STATUS.bad_request){
                    redirectTo(ROUTES_SITE.cadastrar_informacoes);
                }
            }
        }
    },
    vet: {
        is_not_a_vet: (response) => {
            if(response.status == HTTP_STATUS.forbidden){
                redirectTo(ROUTES_SITE.bem_vindo);
            }
        }
    },
    default_error: async(response, callback = (message) => {}) => {
        const data = await response.json();
        const message = data.error || "";
        callback(getMessageOrDefault(message).message);
    }
}

export async function user_auth(callbackOk = (response) => {}, callbackError = (response) => {}){
    const headers = setAuthorizationTokenHeader();
    await makeGetRequest(ROUTES_API.account_me, headers, callbackOk, callbackError);
}

export async function user_have_register(callbackOk = (response) => {}, callbackError = (response) => {}) {
    const headers = setAuthorizationTokenHeader();
    return await makeGetRequest(ROUTES_API.owner_me, headers, callbackOk, callbackError);
}

export async function user_is_vet_registered(callbackOk = (response) => {}, callbackError = (response) => {}) {
    const headers = setAuthorizationTokenHeader();
    return await makeGetRequest(ROUTES_API.vet_me, headers, callbackOk, callbackError)
}

export async function makeLogin(email, password, callbackResponseCaseError = (response) => {}, callbackResponseCaseOk = (response) => {}) {
    const data = {
        email,
        password
    };
    const responseCaseOk = async(response) => {
        const data = await response.json();
        const token = data.token;
        setToken(token);
        return callbackResponseCaseOk();
    }
    return await makePostRequest(ROUTES_API.login, {}, data, responseCaseOk, callbackResponseCaseError);
}

export function getToken() {
    return localStorage.getItem(variables.localStorageKeyAccessToken);
}

export function setToken(token) {
    localStorage.setItem(variables.localStorageKeyAccessToken, token);
}
export function removeToken(){
    localStorage.removeItem(variables.localStorageKeyAccessToken);
}

export function setAuthorizationTokenHeader(){
    return {"Authorization": `Token ${getToken()}`};
}