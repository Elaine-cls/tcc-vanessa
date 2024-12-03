import {getCurrentScript} from "./base-script.js";
import {removeToken} from "../utils/api-utils.js";
import {redirectTo} from "../utils/site-utils.js";

document.addEventListener('DOMContentLoaded', function () {
    const script = getCurrentScript("logout-script.js");
    const button = document.getElementById(script.getAttribute("data-button-id"));
    
    button.addEventListener("click", () => {
        removeToken();
        redirectTo(window.location);
    })
});
