import {registrarPrototypes} from "./utils/form-utils.js";
import {user_auth} from "./utils/api-utils.js";
import {redirectTo} from "./utils/site-utils.js";
import {ROUTES_SITE, HTTP_STATUS} from "./utils/global.js";

user_auth((response) => {
    if(response.status == HTTP_STATUS.ok) {
        redirectTo(ROUTES_SITE.pagina_inicial)
    }
})

document.addEventListener("DOMContentLoaded", function(){
    const form = document.getElementById("loginForm");

    registrarPrototypes()

    form.validarFormularioLogin(ROUTES_SITE.pagina_inicial);
});