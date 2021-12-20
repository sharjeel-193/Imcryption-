// console.log('hello world')
const send = document.querySelector('#send')
const form = document.querySelector('#encodeForm')
const upFile = document.querySelector('#image')
let page = 0;
console.log(form);

const sendToModal = async () => {
    page = page + 1
    const body = new FormData(form)
    
    body.append('image', upFile.files[0], upFile.files[0].filename)

    console.log(body)
    
    const res = await fetch('/encode', {
        method: 'POST',
        body
    })
    const result = await res.json();
    console.log(result)
}
form.addEventListener('submit', async (e) => {
    // console.log(form)
    e.preventDefault();
    sendToModal()
});
