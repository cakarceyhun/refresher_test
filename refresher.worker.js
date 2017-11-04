function ajaxSend(data) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            postMessage(this.responseText);
        }
    };
    xhttp.open("GET", "refresher.py?" + data, true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send();
}

onmessage = function(e) {
    ajaxSend(e.data)
}

