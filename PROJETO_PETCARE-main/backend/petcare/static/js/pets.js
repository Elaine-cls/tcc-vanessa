import {makeGetRequest, setAuthorizationTokenHeader, tratamentosDeErros, user_have_register} from "./utils/api-utils.js";
import {ROUTES_API, ROUTES_SITE} from "./utils/global.js";

user_have_register(() => {}, 
    (response) => {
        tratamentosDeErros.owner.register.dont_have_register(response);
        tratamentosDeErros.accounts.unauthorized(response, ROUTES_SITE.bem_vindo);
    }
)

document.addEventListener("DOMContentLoaded", async function(){
    const headers = setAuthorizationTokenHeader();
    const listaPets = $("#list").empty(); 
    const total = $("#total");

    await makeGetRequest(ROUTES_API.get_pets, headers, async(response) => {
        const data = await response.json();
        if(data.length == 0){
            listaPets.append(`
                <h3 class="col-lg-6">Sem pets cadastrados.</h3>
                `);
            total.append("0");
        }else{
            data.forEach(function(item){
                const linha = `
    
                     <div class="card p-1 mb-2">
                        <div class="card-header bg-transparent d-flex align-items-center justify-content-center">
                            <p class="m-0">Código: <strong>${item.id}</strong></p> 
                        </div>
                        <div class="card-body">
                            <div class="d-flex justify-content-between ">
                                <div>
                                    <p>Nome: <strong>${item.name}</strong></p>
                                    <p>Raça: <strong>${item.race}</strong></p>
                                    <p>Idade: <strong>${item.age}</strong></p>
                                    <p>Peso: <strong>${item.weight} kg</strong></p>
                                    <p>Genero: <strong>${item.gender.description}</strong></p>
                                </div>
                                <p class="text-muted fs-6">${item.species}</p>
                            </div>
                        </div>
                        <div class="card-footer bg-transparent">
                            <a class="btn btn-orange" href="/pets/${item.id}">Historico medico</a>
                        </div>
                    </div>
                
                `;
                listaPets.append(linha);
            })
            total.append(data.length);
        }
    });
    
});