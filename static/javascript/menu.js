
let menuOpen = 0

$('.menu-list-mbl').slideUp()

$('#openBtn').click(function(){
    $('.menu-list-mbl').slideDown()
    $('#openBtn').hide()
    $('#closeBtn').show()
})
$('#closeBtn').click(function(){
    $('.menu-list-mbl').slideUp()
    $('#closeBtn').hide()
    $('#openBtn').show()
})


console.log('hello world')
const send = document.querySelector('#send')
const form = document.querySelector('#myform')
const show = document.querySelector('#show')
let page = 0;
console.log(form);

const load_images = async () => {
    page = page + 1
    const body = new FormData(form)
    body.append('resultLimit', page * 20)
    const res = await fetch('/uploadFile', {
        method: 'POST',
        body
    })
    const result = await res.json();
    console.log(result)
}
form.addEventListener('submit', async (e) => {
    console.log(form)
    e.preventDefault();
    show.innerHTML = ''
    load_images()
});
