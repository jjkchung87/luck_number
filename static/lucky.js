const API_URL = 'http://127.0.0.1:5000/api/get-lucky-num'


/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
    evt.preventDefault()
    const name = $('#name').val()
    const birth_year = parseInt($('#year').val(),10)
    const email = $('#email').val()
    const color = $('#color').val()
 
    
    data = {name, email, birth_year, color}
    console.log(data)
    const res = await axios.post(API_URL, data)
    console.log(res)

    handleResponse(res);

}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(res) {
    if (res.data.errors){
        
        const {name, color, email, birth_year} = res.data.errors
        
        console.log(name, color, email, birth_year)
        
        $('b').text('')
        $('#lucky-results').text('')
        $('#name-err').text(name)
        $('#color-err').text(color)
        $('#email-err').text(email)
        $('#year-err').text(birth_year)
    }
    
    else {
        const numFact = res.data.num.fact
        const luckyNum = res.data.num.num
        const yearFact = res.data.year.fact
        const birthYear = res.data.year.num
        
        $('#lucky-results').text('')
        $('b').text('')
        $('#lucky-results').text(`Your luck number is ${luckyNum} (${numFact}).
        Your birth year (${birthYear}) fact is ${yearFact}.`)
    }
    
}


$("#lucky-form").on("submit", processForm);
