var wifiCount = 0;
var globalData;

function getIp(ssid){
    console.log('ok')
    $.ajax({
        type: "GET",
        url: "http://172.24.1.1:1234/get/local/ip",
        dataType: "json",
        success: function(res, stat, xhrr){
            swal("Ссылка на страницу вашего принтера", "http://" + res["ip"], {
                buttons: {
                    text: "GO"
                },
                closeOnClickOutside: false,
                closeOnEsc: false,
            }).then(name => {
                $(location).attr("href", "http://" + res["ip"] + "/");
            });
        }
    });
}

function connectTo(ssid){
    swal("Введите пароль", {
        content: "input",
        background: "#212124",
        confirmButtonColor: "#212124",
    }).then((value) => {
        connect(ssid, value.toString());
    });
}

function autorization(data){
    globalData = data;
    $.ajax({
        type: "GET",
        url: "http://172.24.1.1:1234/get/password",
        dataType: "json",
        success: function(result, status, xhr, data){
            swal(globalData, {
                content: "input",
                background: "#212124",
                confirmButtonColor: "#212124",
            }).then((value) => {
                if (value == result["pass"]){
                    get_ssid();
                }
                else {
                    autorization("Введён неверный пароль!");
                }
            });
        }
    });
}

function connect(ssid, password){
    $.ajax({
        type: "POST",
        url: "http://172.24.1.1:1234/connect?" + "ssid=" + ssid + "&password=" + password,
        dataType: "json",
        beforeSend: function(){
            $("#wifiContainer").empty();
            $(".spinner-grow").css("display", "block");
        },
        success: function(result, status, xhr){
            get_ssid();
            if (result["status"] == "0"){
                swal("Пароль введён неверно!", "Если у сети нет пароля оставьте графу ввода пустой");
            }
            else if (result["status"] == "1"){
                swal("Ссылка на страницу вашего принтера", "http://" + result["ip"], {
                    button: {
                        text: "GO",
                    },
                    closeOnClickOutside: false,
                    closeOnEsc: false
                }).then(name => {
                    $(location).attr("href", "http://" + result["ip"] + "/");
                });
            }
        }
    });
}

function get_ssid(){
    $.ajax({
        type: "GET",
        url: "http://172.24.1.1:1234/get/list/ssid",
        dataType: "json",
        beforeSend: function(){
            $("#wifiContainer").empty();
            $(".spinner-grow").css("display", "block");
        },
        success: function(result, status, xhr){
            wifiCount = result["ssid"].length;
            $(".spinner-grow").css("display", "none");
            if (result["connected"] != 0){
                $('#wifiContainer').append(`<div class="enterWifi row mb-2 d-flex align-items-center" onclick="getIp('${result["connected"].toString()}')">
                                                <div class="col-10">
                                                    <font>${result["connected"].toString()}</font>
                                                </div>
                                                <div class="col">
                                                    Подключено
                                                </div>
                                            </div>`)
            }
            for(var i = 0; i < result["ssid"].length; i++){
                $("#ssid-table").append($('<tr><td class="line-td"><div class="line"></div</td></tr><tr class="text-tr ' + 'wifi' + (i + 1).toString() + '" ><td class="text-td">' + result["ssid"][i].toString() + '</td></tr>'));
                $('#wifiContainer').append(`<div class="enterWifi row mb-2 d-flex align-items-center" onclick="connectTo('${result["connected"].toString()}')">
                                                <div class="col">
                                                    <font>${result["connected"].toString()}</font>
                                                </div>
                                            </div>`)
            }
            // for (var i = 1; i <= wifiCount; i++){
            //     $("body").on("click", "tr.wifi" + i.toString(), function(){
            //         swal("Введите пароль", {
            //             content: "input",
            //             background: "#212124",
            //             confirmButtonColor: "#212124",
            //         }).then((value) => {
            //             connect($(this).text(), value.toString());
            //         });
            //     });
            // }
            // $("body").on("click", "tr.local-ip", function(){
            //     $.ajax({
            //         type: "GET",
            //         url: "http://172.24.1.1:1234/get/local/ip",
            //         dataType: "json",
            //         success: function(res, stat, xhrr){
            //             swal("Ссылка на страницу вашего принтера", "http://" + res["ip"], {
            //                 buttons: {
            //                     text: "GO"
            //                 },
            //                 closeOnClickOutside: false,
            //                 closeOnEsc: false,
            //             }).then(name => {
            //                 $(location).attr("href", "http://" + res["ip"] + "/");
            //             });
            //         }
            //     });
            // });
        }
    });
}

$(document).ready(function(){
    autorization("Введите пароль от вашего принтера");
});












