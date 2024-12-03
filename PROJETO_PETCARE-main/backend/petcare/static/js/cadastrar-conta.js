import {makePostRequest, tratamentosDeErros, makeLogin} from './utils/api-utils.js';
import {redirectTo, showAlert} from './utils/site-utils.js';
import {ROUTES_API, ROUTES_SITE} from './utils/global.js';
import {validarCampo} from './utils/form-utils.js';
import {validarSenha, validarConfirmSenha, validarTexto} from './utils/validations.js';


document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registrationForm');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirmPassword');
    const email = document.getElementById('email');
    const feedback_email = document.getElementById("invalid-feedback-email");
    const feedback_password = document.getElementById("invalid-feedback-password");
    const feedback_confirm_password = document.getElementById("invalid-feedback-confirm-password");
    const alertPlaceholder = document.getElementById("liveAlertPlaceholder");

    validarCampo(email, feedback_email, validarTexto);
    validarCampo(password, feedback_password, validarSenha);
    validarCampo(confirmPassword, feedback_confirm_password, (value) => validarConfirmSenha(value, password.value))

    form.addEventListener('submit', async function (event) {
        event.preventDefault();
        if (!form.checkValidity()) {
            event.stopPropagation();
            form.classList.add('was-validated');
            return; 
        }

        const formData = {
            email: email.value,
            password: password.value
        };

        const responseCaseOk = async (response) => {
            await makeLogin(email.value, password.value);
            redirectTo(ROUTES_SITE.cadastrar_informacoes);
        }
        const responseCaseError = (response) => {
            tratamentosDeErros.accounts.register.tratarErroDeEmail(response, (message) => {showAlert(message, 'danger', alertPlaceholder)})
        }

        await makePostRequest(ROUTES_API.register_account, {}, formData, responseCaseOk, responseCaseError)
    });
});
