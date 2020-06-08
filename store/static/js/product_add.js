$(document).ready(function(){

    $("#createProductButton").click(function(evt){
        // let serializedData = $("#ceateProductForm").serialize();
        evt.preventDefault();
        let form = $("#ceateProductForm")[0];

        $.ajax({
            url: $("#ceateProductForm").data('url'),
            // data: serializedData,
            type: 'post',
            data: new FormData(form),
            // cache: false,
            contentType: false,
            processData: false,
            success: function(response){
                $(".content__row").append('<div class="content__column"><div class="content__item"><div class="content__img"><img src="/media/' + 
                response.product.image + '" alt=""></div><div class="subtitle">' + 
                response.product.name + '</div><div class="price">' + response.product.price + '</div><div class="description"><p>' + 
                response.product.desc + '</p></div><a href="#" class="add__btn">Buy</a></div></div>')
            }
        })
        

        // $.ajax({
        //     url: $("#ceateProductForm").data('url'),
        //     data: serializedData,
        //     type: 'post',
        //     success: function(response){
        //         $(".content__row").append('<div class="content__column"><div class="content__item"><div class="content__img"><img src="/media/' + 
        //         response.product.image + '" alt=""></div><div class="subtitle">' + 
        //         response.product.name + '</div><div class="price">' + response.product.price + '</div><div class="description"><p>' + 
        //         response.product.desc + '</p></div><a href="#" class="add__btn">Buy</a></div></div>')
        //     }
        // })

    });



});