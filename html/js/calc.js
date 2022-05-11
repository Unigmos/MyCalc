// 変数定義
let strs = "";
let sym_flag = false;

// 文字列をセットする
function set_data(data){
    var str_data = document.getElementById("str_area");

    // id取得→前方一致→フラグ処理
    if(sym_flag == true){
        if(data.id.indexOf("sym") == 0){
            strs = strs.slice(0, -1);
            strs += data.value;
            sym_flag = true;
        }else{
            strs += data.value;
            sym_flag = false;
        }
    }else{
        if(data.id.indexOf("sym") == 0){
            strs += data.value;
            sym_flag = true;
        }else{
            strs += data.value;
            sym_flag = false;
        }
    }
    // 表記(出力)処理
    str_data.innerHTML = strs;
}

// Clearボタン(全消去)
function clr_data(){
    var str_data = document.getElementById("str_area");
    var ans_data = document.getElementById("ans_area");
    strs = "";
    str_data.innerHTML = strs;
    ans_data.innerHTML = strs;
}

// 演算処理
function calc(){
    try{
        var calc_data = document.getElementById("ans_area");
        calc_data.innerHTML = eval(strs);
    }catch(Error){
        alert("不正な式です。");
        strs = "";
        calc_data.innerHTML = "";
    }
}
