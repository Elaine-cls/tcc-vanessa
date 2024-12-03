import {makeGetRequest, makePostRequest, setAuthorizationTokenHeader, tratamentosDeErros, user_is_vet_registered} from "./utils/api-utils.js";
import {ROUTES_API, ROUTES_SITE} from "./utils/global.js";
import {registrarPrototypes, validarCampo} from "./utils/form-utils.js";
import {validarTexto} from "./utils/validations.js"; 
import { capturarUUID, redirectTo, showAlert } from "./utils/site-utils.js";
import {renderizarInformacoesBasicasDoPet, renderizarListaDoencas, renderizarListaMedicamentos, renderizarNotFound} from "./utils/medical_history_utils.js";

user_is_vet_registered(async(response) => {
}, (response) => {
    tratamentosDeErros.accounts.unauthorized(response, ROUTES_SITE.bem_vindo);
    tratamentosDeErros.vet.is_not_a_vet(response);
});

document.addEventListener("DOMContentLoaded", async function(){
    const form = document.getElementById("formSearch");
    const codigo = document.getElementById("codigo-input");
    const codigo_feedback = document.getElementById("invalid-feedback-codigo");

    registrarPrototypes();
        
    validarCampo(codigo, codigo_feedback, validarTexto);

    form.validarFormulario(() => {
        redirectTo(`${ROUTES_SITE.pesquisar_pet}/${codigo.value}`)
    })


    iniciar();

    async function iniciar(){
        const id = capturarUUID();
        if (id){
            preencherDadosDoPet(id);
            validarFormularioMedicamento(id);
        }else{
            $("#hm-container").empty();
        }
    }
    async function preencherDadosDoPet(id){
        const headers = setAuthorizationTokenHeader();
        const url = `${ROUTES_API.vet_pets}/${id}`;
        codigo.value = id;
            

        await makeGetRequest(url, headers, async(response) => {
            const data = await response.json();
            renderizarInformacoesBasicasDoPet(data);
            renderizarListaMedicamentos(data.medical_history.medicines);
            renderizarListaDoencas(data.medical_history.illnesses);
        }, (response) => {
            renderizarNotFound("hm-container");
        })
    }

    function validarFormularioMedicamento(id){
        const form = document.getElementById("form-medicamento");
        const nome = document.getElementById("nome-medicamento-input");
        const nome_feedback = document.getElementById("invalid-feedback-nome-medicamento");
        const data_aplicacao = document.getElementById("data-aplicacao-medicamento");
        const data_aplicacao_feedback = document.getElementById("invalid-feedback-data-aplicacao-medicamento");
        const data_reforco = document.getElementById("data-reforco-medicamento");
        const data_reforco_feedback = document.getElementById("invalid-feedback-data-reforco-medicamento");
        const tipo_medicamento = document.getElementById("tipo-medicamento");
        const tipo_medicamento_feedback = document.getElementById("invalid-feedback-tipo-medicamento");
        const detalhes = document.getElementById("detalhes-medicamento");
        const placeholder = document.getElementById("placeholder-medicamento");

        validarCampo(nome, nome_feedback, validarTexto);
        validarCampo(data_aplicacao, data_aplicacao_feedback, validarTexto);
        validarCampo(data_reforco, data_reforco_feedback, validarTexto);
        validarCampo(tipo_medicamento, tipo_medicamento_feedback, validarTexto);

        form.validarFormulario(async () => {
            const headers = setAuthorizationTokenHeader();
            const url = `${ROUTES_API.vet_pets}/${id}/medicine/add/`;

            const formData = {
                name: nome.value,
                date_application: data_aplicacao.value,
                date_reinforcement: data_reforco.value,
                details: detalhes.value || "",
                medicine_type: tipo_medicamento.value
            }

            await makePostRequest(url, headers, formData, (response) => {
                if(response.ok){
                    showAlert("Medicamento cadastrado com sucesso!", "success", placeholder);
                    redirectTo(window.location, 3000);
                }
            }, async(response) => {
                const data = await response.json();
                console.log(data);
            })
        })
    }
    
});