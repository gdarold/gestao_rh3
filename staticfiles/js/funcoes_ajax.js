function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas_extras/utilizou_hora_extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
            outro_param: 123
        },
        success: function(result){
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}
