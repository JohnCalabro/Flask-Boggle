$form = $('#guess-form')
console.log($form)
$t = $('#test')


async function sendFormData(e) {
    e.preventDefault();
    const $guessVal = $('#guess').val()
    console.log($guessVal)
    const res = await axios.get('/', {params:{term:$guessVal}})
    console.log(res)
    console.log(msg)
    $t.append($guessVal)
}

$form.on('click', sendFormData)

// console.log($guessVal)