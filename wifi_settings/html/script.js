var wifiCount = 0;
var globalData;

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
            $("#ssid-table tr").remove();
            $("#loading-indicator").css("display", "block");
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
            $("#ssid-table tr").remove();
            $("#loading-indicator").css("display", "block");
        },
        success: function(result, status, xhr){
            wifiCount = result["ssid"].length;
            $("#loading-indicator").css("display", "none");
            if (result["connected"] != 0){
                $("#ssid-table").append($('<tr id="connected-ssid-tr" class="text-tr local-ip"> <td class="text-td" style="padding-bottom: 1%; padding-top: 1%;"><table><td style="width: 260px;"><p id="connected-ssid">' + result["connected"].toString() + '</p></td><td><p style="font-size: 14px; opacity: 0.8;">Подключено</p></td></table></td></tr>'));
            }
            for(var i = 0; i < result["ssid"].length; i++){
                $("#ssid-table").append($('<tr><td class="line-td"><div class="line"></div</td></tr><tr class="text-tr ' + 'wifi' + (i + 1).toString() + '" ><td class="text-td">' + result["ssid"][i].toString() + '</td></tr>'));
            }
            for (var i = 1; i <= wifiCount; i++){
                $("body").on("click", "tr.wifi" + i.toString(), function(){
                    swal("Введите пароль", {
                        content: "input",
                        background: "#212124",
                        confirmButtonColor: "#212124",
                    }).then((value) => {
                        connect($(this).text(), value.toString());
                    });
                });
            }
            $("body").on("click", "tr.local-ip", function(){
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
            });
        }
    });
}

$(document).ready(function(){
    if ($(window).width() < 500){
        $("div.general-div").css("width", "80%")
    }
    autorization("Введите пароль от вашего принтера");
});












