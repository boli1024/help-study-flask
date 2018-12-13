function getname(obj) {
    var name = obj.name
    $.post("http://127.0.0.1:5000/video/src",
        {
            name:name
        },
        function (data, status) {
            if (status == "success"){
                document.getElementById("video").src = data
                //document.getElementById("video").play()
            }
        })
}

function change(obj) {
    $(document).ready(function () {
        var name = $(obj).text()
        $(obj).addClass('on')
        //alert(name)
        $.post("http://127.0.0.1:5000/detail",
            {
                name:name
            },
            function (data, status) {
                if (status == "success"){
                    $("p#p-detail").text(data)
                }
                if (status != "success"){
                    alert('请求失败！')
                }
            })
        }
    )
}


function refresh(){
window.location.reload();//强制刷新
}

function get_html(obj) {
    $(document).ready(function () {
        var id = $(obj).attr('id')
        var frame_src = '/static/html/html' + id +'.html'
        $("#frame").attr('src', frame_src)
        $("body").scrollTop = 0
    })
}