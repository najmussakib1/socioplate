function likefunc(sno){
    let endpoint = 'http://127.0.0.1:8000/'+'likepost/'+ String(sno);
    let xhr = new  XMLHttpRequest();
    xhr.open('GET',endpoint,true);
    xhr.onload = function(){
        if (this.status===200){
            a = JSON.parse(this.response)
            let buttn = document.getElementById(String(sno));
            buttn.innerHTML = `<span></span>
    <span></span>
    <span></span>
    <span></span>`+'Like: '+String(a["nooflikes"])
        }
    }
    xhr.send()
}