/*
    This javascript file for script function on html file while crawling other web sites
*/

// fetch movie data from webserver at wanted time
let movieDatas = [];
let button = document.getElementById('btn-search');

button.addEventListener('click', () => {
    fetch(`http://localhost:8000/crawlingapi/movie/${document.getElementById('date').value}`)
        .then(res => res.json())
        .then(datas => {
            for(data in datas) {
                movieDatas.push(data)
            }
        })
        .catch(error => console.log(error))
})