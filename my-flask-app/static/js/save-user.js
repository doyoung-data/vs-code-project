$(document).ready(function() {
    $("#save-btn").click(function() {
        var id = $('#id').val();
        var pw = $('#pw').val();
        var pwCheck = $('#pw-check').val();
        var nick = $('#nick').val();
        var addr = $('#addr').val();
        var type = $('#type-slt').val();

        if (id == "") {
            alert("아이디를 입력하세요");
            return;
        }
        if (pw == "") {
            alert("비밀번호를 입력하세요");
            return;
        }
        if (pw !== pwCheck) {
            alert("비밀번호가 일치하지 않습니다.");
            return;
        }
        if (nick == "") {
            alert("닉네임을 입력하세요");
            return;
        }
        if (addr == "") {
            alert("주소를 입력하세요");
            return;
        }

        // JSON 형식으로 데이터 전송
        $.ajax({
            url: "/user/save-user",  // 경로 확인
            type: "POST",
            contentType: "application/json",  // JSON 형식으로 전송
            data: JSON.stringify({
                id: id,
                pw: pw,
                nick: nick,
                addr: addr,
                type: type
            }),
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
