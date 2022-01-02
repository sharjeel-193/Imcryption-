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

// audio.disabled = true
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
        if(audio.value && image.value & pincode.value){
            let formData = new FormData()
            console.log("LOVE YOU")
            formData.append('use_audio', true)
            formData.append('image', image.files[0])
            formData.append('audio', audio.files[0])
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

