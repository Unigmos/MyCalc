let strs = "";

function set_data(data){
    var str_data = document.getElementById("str_area");
    strs += data.value;
    str_data.innerHTML = strs;
}

function clr_data(){
    var str_data = document.getElementById("str_area");
    strs = "";
    str_data.innerHTML = strs;
}

function calc(){
    var calc_data = document.getElementById("str_area");
    calc_data.innerHTML = eval(strs);
}
