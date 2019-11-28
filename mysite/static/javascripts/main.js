/*
    This javascript file for script function on html file while crawling other web sites
*/

// fetch movie data from webserver at wanted time
let button = document.getElementById('btn-search');
let tableBody = document.getElementById('table-body')

button.addEventListener('click', () => {
    fetch(`http://localhost:8000/crawlingapi`)
        .then(res => res.json())
        .then(datas => {
            console.log(datas)
            for(let i = datas.length - 1; i > -1; i--) {
                let row = tableBody.insertRow(0);
                let numCell = row.insertCell(0)
                let rankCell = row.insertCell(1)
                let titleCell = row.insertCell(2)
                let linkCell = row.insertCell(3)

                numCell.innerHTML = i + 1;
                rankCell.innerHTML = datas[i].movieID
                titleCell.innerHTML = datas[i].title
                linkCell.innerHTML = `<a href=${datas[i].articleLink}>` + datas[i].articleLink + '</a>'
            }
        })
        .catch(error => console.log(error))
})