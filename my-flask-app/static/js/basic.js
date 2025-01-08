//var, let, const


//var : 재정의 O, 재할당 O
var a = 10;
var a =20;
a = 'aasdsa';
var a1 = '안녕';

console.log(a);

//let : 재정의 X, 재할당 O
let b = 1;
b = 2;

//const : 재정의X, 재할당 X, 반드시 초기값
const serverAdderss = 'http://127.0.0.1:5000';

//여러개 받는 데이터 : 배열(리스트), 오브젝트(딕셔너리)
var members = ['a','b','c'];
var one = members[0];
alert(one);

var man = {
  name:'철수',
  age:24,
  asset:['노트북','펜','폰']
};

var name = man['name'];
var name = man.name;
var phone = man.asset;


// 함수

function add(){
  var sum = 10 + 20;
  alert(sum);
}

add();

function add2(num1, num2){
  var sum = num1 + num2;
  
  return sum;
}


var r = add2(1,30);

alert(r)

if(r==100){
  
}else if(r==200){

}else{

}


var users = [
  {
    id:'www1231',
    pw:'1234',
    nick:'wwww'
  },
  {
    id:'sadpfa',
    pw:'ajhf',
    nick:'sad'
  },
  {
    id:'hap',
    pw:'abchap',
    nick:'hapgang'
  }  
]


for (var i=0;i<users.length;i++){
  var user = users[i];
  console.log(user.nick);
}
