
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


