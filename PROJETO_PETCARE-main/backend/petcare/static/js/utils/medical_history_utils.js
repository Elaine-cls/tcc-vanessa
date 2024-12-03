import {formatarData} from "./site-utils.js";


export function renderizarInformacoesBasicasDoPet(data){
    $("#nome").empty().append(data.name);
    $("#codigo").empty().append(data.id);
    $("#raca").empty().append(data.race);
    $("#especie").empty().append(data.species);
    $("#idade").empty().append(data.age);
    $("#peso").empty().append(`${data.weight} kg`);
    $("#genero").empty().append(data.gender.description);
    $("#obs").empty().append(data.medical_history.obs);
}

export function renderizarListaMedicamentos(data){
    const list = $("#list-medicamentos").empty();

    if (data.length == 0){
        list.append("<h5>Sem medicamentos.</h5>")
    }
    data.forEach((item) => {
        const linha = `
               <div class="border-bottom mb-3">
                    <p>Nome: <strong>${item.name}</strong></p>
                    <p>Tipo: <strong>${item.medicine_type.type}</strong></p>
                    <p>Data da aplicação: <strong>${formatarData(item.date_application)}</strong></p>
                    <p>Data de reforço: <strong>${formatarData(item.date_reinforcement)}</strong></p>
                    <p>Detalhes: <strong>${item.details}</strong></p>
                </div>
        `;
        list.append(linha);
    })
}

export function renderizarListaDoencas(data){
    const list = $("#list-doencas").empty();
    if (data.length == 0){
        list.append("<h5>Sem doenças documentadas.</h5>")
    }
}

export function renderizarNotFound(id){
    $(`#${id}`).empty().append(
        `
            <div class="alert alert-danger m-0" role="alert">
                Não foi encontrado!
            </div>
        `
    );
}