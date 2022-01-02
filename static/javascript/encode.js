console.log('ENCODE JS')

const useAudio = document.querySelector('#use_audio')
const message = document.querySelector('#message')
const audio = document.querySelector('#audio')
const image = document.querySelector('#image')
const form = document.querySelector('#encodeForm')
const encodeImg = document.querySelector('#encoded_img')
const loader = document.querySelector('#loader')
const alert = document.querySelector('#encodeFormAlert')
const pincode = document.querySelector('#pincode')
const audioText = document.querySelector('#note-textarea')
const audioPart = document.querySelector('#audioPart')
const textPart = document.querySelector('#textPart')
const encodeBtn = document.querySelector('#encode_btn')
// audio.disabled = true
loader.style.display = 'none'
audioText.readOnly = true
audioPart.style.display = 'none'

useAudio.addEventListener('change', (event) => {
    if(event.currentTarget.checked){
        // audio.disabled = false
        // message.disabled = true
        audioPart.style.display = 'block'
        textPart.style.display = 'none'
        
    } else {
        // audio.disabled = true
        // message.disabled = false
        audioPart.style.display = 'none'
        textPart.style.display = 'block'
    }
})

encodeBtn.addEventListener('click',async () => {
    
    // e.preventDefault()
    console.log("Form Submission Btn")
    if(useAudio.checked){
        console.log({'Audio Text': audioText.value})
        console.log({'Image': image.files[0]})
        console.log({'PIN Cide': pincode.value})
        if(audioText.value && image.files[0] && pincode.value){
            let formData = new FormData()
            console.log("LOVE YOU")
            formData.append('use_audio', false)
            formData.append('image', image.files[0])
            formData.append('message', audioText.value)
            formData.append('pin', pincode.value)
            
            sendDataToModal(formData)
        } else {
            alert.classList.remove('hide')
            alert.classList.add('show')
            alert.innerHTML = 'Please Make Sure Image and Audio has been selected'
        }
    } else {
        if(message.value && image.value && pincode.value){
            let formData = new FormData()
            console.log("LOVE YOU")
            formData.append('use_audio', false)
            formData.append('image', image.files[0])
            formData.append('message', message.value)
            formData.append('pin', pincode.value)

            sendDataToModal(formData)
        } else {
            alert.classList.remove('hide')
            alert.classList.add('show')
            alert.innerHTML = 'Please Make Sure to fill all fields'
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
    console.log(result)
    if('error' in result){
        console.log('In Error Part')
        alert.classList.remove('hide')
        alert.classList.add('show')
        alert.innerHTML = result.error
    }
    loader.style.display = 'none'
    if(result.fileName !== undefined){
        encodeImg.src =  `/static/uploads/${result.fileName}`
    }
}

