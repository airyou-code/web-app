function getCookie(name, json = false) {
    if (!name) {
        return undefined;
    }
    /*
    Returns cookie with specified name (str) if exists, else - undefined
    if returning value is JSON and json parameter is true, returns json, otherwise str
    */
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([.$?*|{}()\[\]\\\/+^])/g, '\\$1') + "=([^;]*)"
    ));
    if (matches) {
        let res = decodeURIComponent(matches[1]);
        if (json) {
            try {
                return JSON.parse(res);
            }
            catch (e) { }
        }
        return res;
    }

    return undefined;
}

String.prototype.replaceAt = function (index, replacement) {
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}

function next() {
    // var link = "{% url 'iqtest' 0 %}";
    // link = link.substring(0, link.length - 1);
    // idTask = Number('{{ test.id }}') + 1;
    // deleteCooki('ask');
    a = Number(getCookie('ask')) + 1;
    document.cookie = "ask=" + a + "; path=/";
    return location.href = "/test";
}

function select(id_select) {
    list_answer = getCookie('ask_list');
    document.cookie = "ask_list=" + list_answer.replaceAt(Number(getCookie('ask')), String(id_select)) + "; path=/";
    // console.log(list_answer.charAt(0));
    next();
}

function previous() {
    id_ask = Number(getCookie('ask')) - 1;
    if (id_ask < 0) { id_ask = 0 };
    document.cookie = "ask=" + id_ask + "; path=/";
    // list_answer = getCookie('ask_list');
    // document.getElementById(list_answer.charAt(Number(getCookie('ask')))).className = "select";
    return location.href = "/test";
    // var link = "{% url 'iqtest' 0 %}";
    // link = link.substring(0, link.length - 1);
    // idTask = Number('{{ test.id }}') - 1;
    // return location.href = link + idTask;
}

function send_test(){
    return location.href = "/result";
}

function check_select() {
    list_answer = getCookie('ask_list');
    if (Number(getCookie('ask')) >= 0){
        document.getElementById(list_answer.charAt(Number(getCookie('ask')))).className = "select";
    }
    if (Number(getCookie('ask')) >= 9) {
        var button = document.getElementById("next_b");
        button.onclick = send_test;
        document.getElementById("next").innerHTML = "SEND TEST";
    }
}