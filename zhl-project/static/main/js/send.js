
        function send () {
            if (document.getElementById("text").value.length == 0) {
                // alert("aaaa")
                var param = document.getElementById("text2").value;
            } else {
                // alert("bbb")
                var param = document.getElementById("text").value;
            }


            var patt = /^(\d{1,3}.){3}\d{1,3}$/
            var patt2 = /^[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?$/
            var patt3 = /^[a-zA-Z0-9]{32}|[a-zA-Z0-9]{40}|[a-zA-Z0-9]{64}$/
            var re = param.match(patt);
            var re2 = param.match(patt2);
            var re3 = param.match(patt3);

            if (re == null && re2 == null && re3 == null) {
                alert("请输入正确格式");
                window.location.reload();
            } else {
                // alert("aaaa")
                if (param.length > 0) {
                    // alert(param);
                    var api_num = $("#api_num").val()

                    location.href = "/index/?search-index="+param+"&msgs="+api_num
                }
            }
        }
        document.onkeydown = function (e) {
          var keyNum=window.event ? e.keyCode :e.which;
          if(keyNum==13){
            send()
          }
        };