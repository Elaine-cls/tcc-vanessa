import {validarTexto, validarSenha} from "../utils/validations.js";
import {makeLogin, tratamentosDeErros} from "../utils/api-utils.js";
import {showAlert, redirectTo} from "../utils/site-utils.js";

export function validarCampo(input, feedback, validationMethod = (value) => {}){
    input.addEventListener("blur", () => {
        const validation = validationMethod(input.value);
        if(validation != ""){
            input.setCustomValidity(validation);
            setValidationFeedback(feedback, input.validationMessage);
            invalidClass(input);
        }else{
            input.setCustomValidity("");
            setValidationFeedback(feedback, input.validationMessage);
            validClass(input);
        }
    });
}
export function setValidationFeedback(feedback, message){
    feedback.innerText = message;
}
function invalidClass(input){
    input.classList.add('is-invalid');
    input.classList.remove('is-valid');
}
export function validClass(input){
    input.classList.add("is-valid");
    input.classList.remove("is-invalid");
}

export function registrarPrototypes(){
    HTMLFormElement.prototype.validarFormulario = function(callback = () => {}){
        this.addEventListener("submit", function(event) {
            event.preventDefault();
            if (!this.checkValidity()) {
                event.stopPropagation();
                this.classList.add('was-validated');
                return; 
            }
            callback();
        });
    }
    HTMLFormElement.prototype.validarFormularioLogin = function(redirectCaseSuccess) {
        const email = document.getElementById("email");
        const password = document.getElementById("password");
        const email_feedback = document.getElementById("invalid-feedback-email");
        const password_feedback = document.getElementById("invalid-feedback-password");
        const alertPlaceholder = document.getElementById("liveAlertPlaceholder");
    
        validarCampo(email, email_feedback, validarTexto);
        validarCampo(password, password_feedback, validarSenha);

        this.addEventListener("submit", async function(event) {
            event.preventDefault();
            if (!this.checkValidity()) {
                event.stopPropagation();
                this.classList.add('was-validated');
                return; 
            }
            let canRedirect = true;
            const responseCaseError = async(response) => {
                tratamentosDeErros.default_error(response, (message) => {
                    showAlert(message, "danger", alertPlaceholder);
                });
                canRedirect = false;
            }
            const responseCaseOk = async(response) => {
                canRedirect = true;
            }
            await makeLogin(email.value, password.value, responseCaseError, responseCaseOk);
            if(canRedirect) redirectTo(redirectCaseSuccess);
        });
    }
}