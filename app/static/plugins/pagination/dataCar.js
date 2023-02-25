var dataCar = []

$.ajax({
    url: '/carros',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp){
           dataresp = {
            placa: resp[x].cod,
            modelo: resp[x].loja,
            ano: resp[x].nome,
            status: resp[x].status,  
            vizualizar: `<a href="/lista-clientes/${resp[x].cod}" class="btn btn-outline-primary btn-sm">Vizualizar</a>` 
           }
           dataCar.push(dataresp)
        }
    }
});

var columnsCar = {
    placa: 'Placa',
    modelo: 'Modelo',
    ano: 'Ano',
    status: 'Status',
    vizualizar: "Vizualizar"
}