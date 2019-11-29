/*
    This javascript file for script function on html file while crawling other web sites
*/

// fetch movie data from webserver at wanted time
let button = document.getElementById('btn-search'); // 클릭하면 입력한 날짜에 맞는 영화 순위를 호출하는 버튼을 찾아옴
let tableBody = document.getElementById('table-body') // 서버로 부터 받은 영화 순위 데이터가 입력될 테이블의 위치를 id로 받아옴
let prevDay = null // 이전에 받아온 영화 데이터가 있을때 테이블을 다 지우고 다시 입력하기 위해 그 날짜를 저장해둘 변수
button.addEventListener('click', () => { 
    // 버튼에 이벤트 리스너를 달아 callback 함수를 다음과 같이 정의
    if(prevDay === null) {
        prevDay = document.getElementById('date').value
    }
    else {
        for(let k = 0; k < 50; k++) {
            tableBody.deleteRow(0)
        }
        prevDay = document.getElementById('date').value
    }
    // 만약 prevDay에 null이 아닌 값이 저장되어 있다면 이전에 데이터를 받아온 적이 있는 것이므로 테이블에 입력된 값들을 삭제
    fetch(`http://localhost:8000/crawlingapi/?search=${document.getElementById('date').value}`) 
        .then(res => res.json())
        .then(datas => {
            for(let i = 49; i > -1; i--) {
                let row = tableBody.insertRow(0);
                let dateCell = row.insertCell(0)
                let rankCell = row.insertCell(1)
                let titleCell = row.insertCell(2)
                let linkCell = row.insertCell(3)
    
                dateCell.innerHTML = datas[i].date;
                rankCell.innerHTML = datas[i].ID
                titleCell.innerHTML = datas[i].title
                linkCell.innerHTML = `<a href=${datas[i].Link}>` + datas[i].Link + '</a>'
            }
        })
        .catch(error => console.log(error))
    // 서버로 부터 데이터를 받는 fecth메소드 사용
})