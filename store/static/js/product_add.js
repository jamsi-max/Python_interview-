`use strict`

$(document).ready(function(){
    if('function' === typeof importScripts) {
        importScripts('popups.js');
    }

    $("#createProductButton").click(function(evt){
        evt.preventDefault();
        let form = $("#ceateProductForm")[0];

        $.ajax({
            url: $("#ceateProductForm").data('url'),
            type: 'POST',
            data: new FormData(form),
            contentType: false,
            processData: false,
            success: function(response){
                if (!response.result){
                    let err = Object.keys(response.error) // получаем имена полей с ошибками
                    for(let index = 0; index < err.length; index++){ //идем по полям с ошибками циклом и выводим в плесхолдерах ошибки
                        $('input[name="' + err[index] + '"]').attr( 'placeholder', response.error[err[index]]);
                    }
                }else{
                    $(".content__row").append(response.result);
                    const popupActive = document.querySelector('.popup.open'); // получаемоткрытаю модалку
                    popupClose(popupActive); // функция из соседнего скрипта модалок закрывает её и возращает скролы
                    document.getElementById('ceateProductForm').reset();  // очишаем форму после ввода товара
                }
            }
        })
    });
    
});