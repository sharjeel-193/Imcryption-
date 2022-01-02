
console.log('DECODE JS')

const hidMsg = document.querySelector('#hidMsg')
const image = document.querySelector('#encImg')
const form = document.querySelector('#decodeForm')
const loader = document.querySelector('#loader')
const msgBox = document.querySelector('#hidMsgBox')
const decodeBtn = document.querySelector('#decode_btn')
const pincode = document.querySelector('#pincode')
const alert = document.querySelector('#decodeFormAlert')

loader.style.display = 'none'
msgBox.style.display = 'none'

// form.addEventListener('submit', async (e) => {
//     e.preventDefault()
//     let formData = new FormData()
//     formData.append('encImg', image.files[0])
//     sendDataToModal(formData)
// })

decodeBtn.addEventListener('click', async () => {
    if(image.value && pincode.value){
        let formData = new FormData()
        formData.append('encImg', image.files[0])
        formData.append('pin', pincode.value)
        sendDataToModal(formData)
    } else {
        alert.classList.remove('hide')
        alert.classList.add('show')
        alert.innerHTML = 'Please Make Sure to Fill All Fields'
    }
    
})

const sendDataToModal = async (formData) => {
    loader.style.display = 'block'
    for(let [name, value] of formData) {
        console.log(`${name} = ${value}`); // key1 = value1, then key2 = value2
    }
    const res = await fetch('/decode', {
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
    } else {
        hidMsg.innerHTML = result.message
    }
    loader.style.display = 'none'
    msgBox.style.display = 'block'

    
    // hidMsg.text(result.message)
    
}

// modalBtn.addEventListener('click', () => {
//     console.log('Open Modal')
//     $('#passwordModal').modal()
// })
