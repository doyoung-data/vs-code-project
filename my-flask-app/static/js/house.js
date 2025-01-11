$(document).ready(function () {
   $("#predict-btn").on("click", function () {
     var area = $("#area").val();
     var year = $("#year").val();
     var income = $("#income").val();
     var school_rating = $("#school-rating").val();
     var transit_score = $("#transit-score").val();
     var rooms = $("#rooms").val();
 
     // 유효성 검사
     if (!area || area <= 0) {
       alert("면적을 올바르게 입력해주세요.");
       return;
     }
     if (!year || year < 1900 || year > 2024) {
       alert("건축 연도을 1900~2024 사이로 입력해주세요.");
       return;
     }
     if (!income || income <= 0) {
       alert("소득을 올바르게 입력해주세요.");
       return;
     }
     if (!school_rating || school_rating < 1 || school_rating > 10) {
       alert("학교 평점을 1~10 사이로 입력해주세요.");
       return;
     }
     if (!transit_score || transit_score < 1 || transit_score > 10) {
       alert("교통 점수를 1~10 사이로 입력해주세요.");
       return;
     }
     if (!rooms || rooms <= 0) {
       alert("방 개수(rooms)를 선택해주세요.");
       return;
     }
 
     var postData = {
       area: area,
       year: year,
       income: income,
       school_rating: school_rating,
       transit_score: transit_score,
       rooms: rooms,
     };
 
     console.log(postData);
 
     // 가격 예측
     $.ajax({
       url: "./api/ai/predict-house-price",
       type: "get",
       data: postData,
       success: function (response) {
         var price_by_lin = convert_to_comma(response.price_by_lin, "$");
         var price_by_rf = convert_to_comma(response.price_by_rf, "$");
 
         $("#result-text-1").text(price_by_lin);
         $("#result-text-2").text(price_by_rf);
         alert("예측 완료");
 
         // 데이터 저장
         $.ajax({
           url: "./api/ai/add-house",
           type: "post",
           contentType: "application/json",
           data: JSON.stringify({
             area: area,
             year: year,
             income: income,
             school_rating: school_rating,
             transit_score: transit_score,
             rooms: rooms,
             pred_lin: response.price_by_lin,
             pred_rf: response.price_by_rf,
           }),
           success: function (response) {
             if (response.message == "ok") {
               alert("데이터 저장 완료");
               location.href = "./house";
             } else {
               alert("데이터 저장 실패");
             }
           },
           error: function (error) {
             console.log(error);
           },
         });
       },
       error: function (error) {
         console.log(error);
       },
     });
   });
 
   function convert_to_comma(number, simbol) {
     number = Math.floor(number);
     return simbol + number.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
   }
 });
 