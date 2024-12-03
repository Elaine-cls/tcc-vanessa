import {makeGetRequest, setAuthorizationTokenHeader, user_have_register, tratamentosDeErros} from "./utils/api-utils.js";
import {ROUTES_API, ROUTES_SITE} from "./utils/global.js";
import {capturarUUID } from "./utils/site-utils.js";
import {renderizarInformacoesBasicasDoPet, renderizarListaMedicamentos, renderizarNotFound, renderizarListaDoencas} from "./utils/medical_history_utils.js";

user_have_register(() => {}, 
    (response) => {
        tratamentosDeErros.owner.register.dont_have_register(response);
        tratamentosDeErros.accounts.unauthorized(response, ROUTES_SITE.bem_vindo);
    }
)

document.addEventListener("DOMContentLoaded", async function(){
    const headers = setAuthorizationTokenHeader();
    const id = capturarUUID();

    await makeGetRequest(`${ROUTES_API.get_pets}/${id}`, headers, async(response) => {
        const data = await response.json();

        renderizarInformacoesBasicasDoPet(data);
        renderizarListaMedicamentos(data.medical_history.medicines);
        renderizarListaDoencas(data.medical_history.illnesses);
        
    }, (response) => {
       renderizarNotFound("conteudo");
    }); 
    
});