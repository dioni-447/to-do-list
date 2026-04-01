function criarCard(tarefa) {
    const card = document.createElement('div')
    card.className='card'
    card.innerHTML = ` <h3>${tarefa.titulo}</h3>
        <p>${tarefa.descricao}</p>
        <p>Prazo: ${tarefa.prazo}</p>
        <p>Status: ${tarefa.status}</p>`
    
    const btnDeletar = document.createElement('button')
            btnDeletar.className='btnDeletar'
            btnDeletar.textContent = 'Deletar'
            btnDeletar.addEventListener('click', () => {
                titulo= document.getElementById("titulo")
                fetch(`http://localhost:5000/tarefas/${tarefa.id}`, {
                method: 'DELETE'
                })
                .then(() => card.remove())
                alert("Tarefa deletada com sucesso!");
            })
            card.appendChild(btnDeletar)
    
    const btnEditar = document.createElement('button')
            btnEditar.className='btnEditar'
            btnEditar.textContent='Editar'
            btnEditar.addEventListener('click', () =>{
                card.innerHTML = `
                    <input id="edit-titulo" value="${tarefa.titulo}"><br>
                    <input id="edit-descricao" value="${tarefa.descricao}"><br>
                    <input id="edit-prazo" type="date" value="${tarefa.prazo}"><br>
                    <select id="edit-status" name="edit-status">
                        <option value="pendente"  ${tarefa.status === 'pendente' ? 'selected' : ''}>pendente</option>
                        <option value="ativo" ${tarefa.status === 'ativo' ? 'selected' : ''}>ativo</option>
                        <option value="completado" ${tarefa.status === 'completado' ? 'selected' : ''}>completado</option>
                    </select> <br>
                    `;
                
                const btnSalvar=document.createElement('button')
                btnSalvar.className='btnSalvar'
                btnSalvar.textContent='Salvar'
                btnSalvar.addEventListener('click', () =>{

                    novoTitulo= document.getElementById('edit-titulo').value
                    novoDescricao= document.getElementById('edit-descricao').value
                    novoprazo= document.getElementById('edit-prazo').value
                    novoStatus=document.getElementById('edit-status').value
                    if (titulo === "") {
                        alert("O título não pode estar vazio!");
                        return; // impede o fetch
                    }

                    fetch(`http://localhost:5000/tarefas/${tarefa.id}`, {
                        method: 'PUT',
                        headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        titulo: novoTitulo,
                        descricao: novoDescricao,
                        prazo: novoprazo,
                        status:novoStatus
                    })
    
    })
                .then(response => response.json())   
                .then(tarefaEditada => {
                    card.replaceWith(criarCard(tarefaEditada))
                alert("Tarefa editada com sucesso!");
                })
            })
            card.appendChild(btnSalvar)
        })
        card.appendChild(btnEditar)
    
    return card  // ← retorna o card pronto
}  


document.addEventListener('DOMContentLoaded', () => {

fetch('http://localhost:5000/tarefas')
    .then(response => response.json())
    .then(dados => {
        dados.itens.forEach(tarefa => {
        const card = criarCard(tarefa)
        document.getElementById('lista-tarefas').appendChild(card)
        })
    })
        
        
    
    document.getElementById('criar').addEventListener('click',()=> {
        const titulo= document.getElementById("titulo").value;
        const descricao= document.getElementById("descricao").value;
        const prazo= document.getElementById("prazo").value;
        if (titulo === "") {
        alert("O título não pode estar vazio!");
        return; // impede o fetch
    }
       fetch(`http://localhost:5000/tarefas`,{
        method: 'POST',
        headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ titulo, descricao, prazo })
       })
        .then(response => response.json())
        .then(novaTarefa => {
        const card = criarCard(novaTarefa)
        document.getElementById('lista-tarefas').appendChild(card)
        alert("Tarefa criada com sucesso!");
})



    })
});