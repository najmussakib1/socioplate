function likefunc(sno){
    let endpoint = 'http://127.0.0.1:8000/'+'likepost/'+ String(sno);
    fetch(endpoint)
    .then(response => response.json())
    .then(data => {
        let buttn = document.getElementById(String(sno));
        buttn.innerHTML = `<span></span>
        <span></span>
        <span></span>
        <span></span>`+'Like: '+String(data["nooflikes"]);
    });
}