
//get Stars for Rating
const onestar = document.getElementById('star1')
const twostars = document.getElementById('star2')
const threestars = document.getElementById('star3')
const fourstars = document.getElementById('star4')
const fivestars = document.getElementById('star5')

const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-rating')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handleStarSelect = (size)=>{
    const children = form.children
    for (let i=0;i<children.length;i++) {
        if(i<= size) {
            children[i].classList.add('checked')
        }
        else {
            children[i].classList.remove('checked')
        }
    }
}


const handleSelect = (selection) =>{
    switch(selection){
        case 'star1': {
//onestar.classList.add('checked')
//twostars.classList.remove('checked')
//threestars.classList.remove('checked')
//fourstars.classList.remove('checked')
//fivestars.classList.remove('checked')
           handleStarSelect(1)
            return
        }
        case 'star2': {
            handleStarSelect(2)
            return
        }
        case 'star3': {
            handleStarSelect(3)
            return
        }
        case 'star4': {
            handleStarSelect(4)
            return
        }
        case 'star5': {
            handleStarSelect(5)
            return
        }
    }
}

const getNumericValue =(stringValue)=>{
    let numericValue;
    if (stringValue == 'star1'){
        numericValue = 1
    }
    else if (stringValue == 'star2'){
        numericValue = 2
    }
    else if (stringValue == 'star3'){
        numericValue = 3
    }
    else if (stringValue == 'star4'){
        numericValue = 4
    }
    else if (stringValue == 'star5'){
        numericValue = 5
    }
    else {
        numericValue = 0
    }
    return numericValue
}

const arr = [onestar, twostars, threestars, fourstars, fivestars]

arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
    handleSelect(event.target.id)
}))

arr.forEach(item=> item.addEventListener('click', (event)=>{
    const val = event.target.id
    let isSubmit = false

    form.addEventListener('submit', e => {
        e.preventDefault()
        if (isSubmit) {
            return
        }
        isSubmit = true
        const id = e.target.id
        console.log(id)
        const val_num = getNumericValue(val)

        $.ajax({
            type: 'POST',
            url: '/rate/',
            data:{
                'csrfmiddlewaretoken': csrf[0].value,
                'el_id': id,
                'val': val_num,
            },
            success: function(response){
                console.log(response)
                confirmBox.innerHTML = `<h1>Successfully rated with ${response.score} stars</h1>`
            },
            error: function(error){
                console.log(error)
                confirmBox.innerHTML = '<h1>Something went wrong</h1>'
            }
        })

    })
}))