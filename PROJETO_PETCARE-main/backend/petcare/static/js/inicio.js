import {makeGetRequest, setAuthorizationTokenHeader, tratamentosDeErros, user_have_register} from "./utils/api-utils.js";
import {ROUTES_API, ROUTES_SITE} from "./utils/global.js";

user_have_register((response) => {}, (response) => {
    tratamentosDeErros.owner.register.dont_have_register(response);
    tratamentosDeErros.accounts.unauthorized(response, ROUTES_SITE.bem_vindo);
});

document.addEventListener("DOMContentLoaded", async function(){
    const headers = setAuthorizationTokenHeader();
    const totalpets = $("#total-pets").empty(); 

    await makeGetRequest(ROUTES_API.get_pets, headers, async(response) => {
        const data = await response.json();
        totalpets.append(data.length);
    });
    
});

//<img src="static/imgs/pluto.png" class="card-img-top align-self-center mt-2" alt="..." style="width: 50%;">