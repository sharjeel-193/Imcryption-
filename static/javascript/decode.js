
console.log('DECODE JS')

const hidMsg = document.querySelector('#hidMsg')
const image = document.querySelector('#encImg')
const form = document.querySelector('#decodeForm')
const loader = document.querySelector('#loader')
const msgBox = document.querySelector('#hidMsgBox')

loader.style.display = 'none'
msgBox.style.display = 'none'

form.addEventListener('submit', async (e) => {
    e.preventDefault()
    let formData = new FormData()
    formData.append('encImg', image.files[0])
    sendDataToModal(formData)
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
    loader.style.display = 'none'
    msgBox.style.display = 'block'

    hidMsg.innerHTML = result.message
    // hidMsg.text(result.message)
    
}

