

function usernametr(str){
    let lst = str.split(/\s+/);
    if (str){
        if (lst.length == 1){
            return true;
        }
        else{
            return false;
        }
    }
    else{
        return false;
    }
}
function fntr(str){
    if (str){
        return true;
    }
    else{
        return false;
    }
}
function lntr(str){
    if (str){
        return true;
    }
    else{
        return false;
    }
}

function mailtr(str){
    if (str){
        return true;
    }
    else{
        return false;
    }
}
function pwtr(str){
    if (str){
        return true;
    }
    else{
        return false;
    }
}
let func = (event)=>{

    let utxt = usertxt.value;
    let fntxt = fnarea.value;
    let lntxt = lnarea.value;
    let matxt = mailarea.value;
    let pwtxt = pwarea.value;
    let isus =usernametr(utxt);
    let isfn = fntr(fntxt);
    let isln = lntr(lntxt);
    let ismail = mailtr(matxt);
    let ispw = pwtr(pwtxt);
    if (isus && isfn && isln && ismail && ispw){
        let pp =document.getElementById('aa');
        pp.innerHTML=`
        <button type="submit" id='sub'>
                            <span></span>
                            <span></span>
                            <span></span>
                            <span></span>
                            Submit
                        </button>
        `
    }
    else{
        let pp =document.getElementById('aa');
        pp.innerHTML=``
    }
    if (isus){
        let wtxt = document.getElementById('warning');
        wtxt.innerText='';
    }
    else{
        let wtxt = document.getElementById('warning');
        wtxt.innerText='**The username should be in one word. No sapces are allowed!**';
    }
}



var usertxt = document.getElementById('uname');
var fnarea = document.getElementById('fn');
var lnarea = document.getElementById('ln');
var mailarea = document.getElementById('mail');
var pwarea = document.getElementById('pw');


let utxt = usertxt.value;
let isus =usernametr(utxt);
if (isus){
    let wtxt = document.getElementById('warning');
    wtxt.innerText='';
}
else{
    let wtxt = document.getElementById('warning');
    wtxt.innerText='**The username should be in one word. No sapces are allowed!**';
}

usertxt.addEventListener('input',func);
fnarea.addEventListener('input',func);
lnarea.addEventListener('input',func);
mailarea.addEventListener('input',func);
pwarea.addEventListener('input',func);


