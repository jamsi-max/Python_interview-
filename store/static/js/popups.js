`use strict`

const popupLinks = document.querySelectorAll('.popup-link');
const body = document.querySelector('body');
const lockPadding = document.querySelectorAll(".lock-padding")

let unlock = true;

const timeout = 600;
if (popupLinks.length > 0){
    for(let index = 0; index < popupLinks.length; index++) {
        const popupLink = popupLinks[index];
        popupLink.addEventListener("click", function (e){
            
            const popupName = popupLink.getAttribute('href').replace('#','');
            const curentPopup = document.getElementById(popupName);
            popupOpen(curentPopup);
            e.preventDefault();
        });
    }
}

const popupCloseIcone = document.querySelectorAll('.close-popup');
if (popupCloseIcone.length > 0){
    for(let index = 0; index < popupCloseIcone.length; index++){
        const el = popupCloseIcone[index];
        el.addEventListener('click', function (e){
            popupClose(el.closest('.popup')); // будет искать вверх по родителям класс popup
            e.preventDefault();
        });
    }
}

function popupOpen(curentPopup){
    if(curentPopup && unlock) {
        const popupActive = document.querySelector('.popup.open');
        
        if(popupActive){
            popupClose(popupActive, false);
        } else {
            bodyLock();
        }
        curentPopup.classList.add('open');
        curentPopup.addEventListener("click", function (e){
            if(!e.target.closest('.popup__content')){
                popupClose(e.target.closest('.popup'));
            }
        });
    }
}
function popupClose(popupActive, doUnlock = true){
    if(unlock){
        popupActive.classList.remove('open');
        if(doUnlock){
            bodyUnLock();
        }
    }
}
function bodyLock(){
    const lockPaddingValue = window.innerWidth - document.querySelector('.wrapper').offsetWidth + 'px';
    if(lockPadding.length > 0) {
        for(let index = 0; index < lockPadding.length; index++){
            const el = lockPadding[index];
            el.style.paddingRight = lockPaddingValue;
        }
    }
    body.style.paddingRight = lockPaddingValue;
    body.classList.add('lock');

    unlock = false;
    setTimeout(function(){
        unlock = true;
    }, timeout);
}
function bodyUnLock(){
    setTimeout(function(){
        if (lockPadding.length > 0) {
            for(let index = 0; index < lockPadding.length; index++){
                const el = lockPadding[index];
                el.style.paddingRight = '0px';
            }
        }
        body.style.paddingRight = '0px';
        body.classList.remove('lock');
    }, timeout);

    unlock = false;
    setTimeout(function(){
        unlock = true;
    }, timeout);
}
document.addEventListener('keyup', function (e){
    if(e.which === 27){
        const popupActive = document.querySelector('.popup.open');
        popupClose(popupActive);
    }
})
