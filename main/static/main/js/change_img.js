function change_img() {
    var number = document.getElementById('candidate_number').value;
    if(number <= 0 || number > 5)
        document.getElementById('candidate_img').src='/static/main/img/unknown.jpg';
    else
        document.getElementById('candidate_img').src=`/static/main/img/${number}.jpg`;
}
