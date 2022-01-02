console.log('hello world')
// const send = document.querySelector('#send')
// const form = document.querySelector('#encodeForm')
// const upFile = document.querySelector('#image')
// let page = 0;
// console.log(form);

// const sendToModal = async () => {
//     page = page + 1
//     const body = new FormData(form)
    
//     body.append('image', upFile.files[0], upFile.files[0].filename)

//     console.log(body)
    
//     const res = await fetch('/encode', {
//         method: 'POST',
//         body
//     })
//     const result = await res.json();
//     console.log(result)
// }
// form.addEventListener('submit', async (e) => {
//     // console.log(form)
//     e.preventDefault();
//     sendToModal()
// });

const useAudio = document.querySelector('#use_audio')
const message = document.querySelector('#message')
const audio = document.querySelector('#audio')
const image = document.querySelector('#image')
const form = document.querySelector('#encodeForm')
const encodeImg = document.querySelector('#encoded_img')
const loader = document.querySelector('#loader')

audio.disabled = true
loader.style.display = 'none'
useAudio.addEventListener('change', (event) => {
    if(event.currentTarget.checked){
        audio.disabled = false
        message.disabled = true
    } else {
        audio.disabled = true
        message.disabled = false
    }
})

form.addEventListener('submit',async (e) => {
    
    e.preventDefault()
    if(useAudio.checked){
        if(audio.value && image.value){
            let formData = new FormData()
            console.log("LOVE YOU")
            formData.append('use_audio', true)
            formData.append('image', image.files[0])
            formData.append('audio', audio.files[0])
            
            sendDataToModal(formData)
        } else {
            console.log("Please Make Sure Image and Audio File has been selected")
        }
    } else {
        if(message.value && image.value){
            let formData = new FormData()
            console.log("LOVE YOU")
            formData.append('use_audio', false)
            formData.append('image', image.files[0])
            formData.append('message', message.value)
            
            sendDataToModal(formData)
        } else {
            console.log("Please Make Sure Image and Message has been selected")
        }
    }
})

const sendDataToModal = async (formData) => {
    loader.style.display = 'block'
    for(let [name, value] of formData) {
        console.log(`${name} = ${value}`); // key1 = value1, then key2 = value2
    }
    const res = await fetch('/encode', {
        method: 'POST',
        body: formData
    })
    const result = await res.json();
    console.log(result.fileName)
    loader.style.display = 'none'
    if(result.fileName !== undefined){
        encodeImg.src =  `/static/uploads/${result.fileName}`
    }
}
