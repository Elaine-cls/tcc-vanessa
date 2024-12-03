import {tratamentosDeErros, user_is_vet_registered} from './utils/api-utils.js';
import {ROUTES_SITE} from "./utils/global.js";

document.addEventListener("DOMContentLoaded", async function(){

    user_is_vet_registered(async(response) => {
        const data = await response.json();
        preencherInformacoes(data);
    }, (response) => {
        tratamentosDeErros.accounts.unauthorized(response, ROUTES_SITE.bem_vindo);
        tratamentosDeErros.vet.is_not_a_vet(response);
    });


    function preencherInformacoes(data){
        const name = $("#name-vet").empty();
        name.append(data.name);
    }

});