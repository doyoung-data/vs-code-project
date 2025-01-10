$(document).ready(function() {
  $('#predict-btn').click(function() {
    var area = $('#area').val();
    var rooms = $('#rooms').val();
    var year = $('#year').val();
    var income = $('#income').val();
    var school_rating = $('#school-rating').val();
    var transit_score = $('#transit-score').val();

    $.get('/api/ai/predict-house-price', {
      area: area,
      rooms: rooms,
      year: year,
      income: income,
      school_rating: school_rating,
      transit_score: transit_score
    }, function(data) {
      // 예측된 가격을 결과로 표시
      $('#result-text-1').text('$' + data.price_by_lin.toFixed(2));  // 선형회귀 예측값
      $('#result-text-2').text('$' + data.price_by_rf.toFixed(2));   // 랜덤포레스트 예측값
    });
  });
});
