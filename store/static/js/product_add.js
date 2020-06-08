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
                    console.log('no')
                }else{
                    $(".content__row").html(response.result);
                    const popupActive = document.querySelector('.popup.open');
                    popupClose
                    popupClose(popupActive);
                }
            }
        })
    });
    
});